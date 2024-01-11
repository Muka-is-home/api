from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from cloudinary import uploader, CloudinaryImage
from api.models import ShopItem
from adminportal.views import user_is_superuser
from adminportal.serializers import ShopItemSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@user_passes_test(user_is_superuser, login_url="user_login")
def create_shop_item(request):

    if request.method == 'POST':

        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        link = request.POST.get("link")
        
        image_file = request.FILES["image"]
        image_id = name.replace(" ", "_")
        
        uploader.upload(image_file, public_id=image_id, unique_filename=False, overwrite=True)
        image_url = CloudinaryImage(image_id).build_url()
        
        ShopItem.objects.create(
          name=name,
          price=float(price),
          description=description,
          link=link,
          image=image_url
        )
        
        shop_items = ShopItem.objects.all()
        shop_item_data = ShopItemSerializer(shop_items, many=True).data
        
        return redirect('shop_list')
    else:
        return render(request, "adminportal/shop_form.html")
    

@user_passes_test(user_is_superuser, login_url="user_login")
def edit_shop_item(request, pk):
    
    item = ShopItem.objects.get(pk=pk)
    
    if request.method == 'POST':

        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        link = request.POST.get("link")
        image_file = request.FILES.get("image")
        image_id = name.replace(" ", "_")
        
        uploader.upload(image_file, public_id=image_id, unique_filename=False, overwrite=True)
        image_url = CloudinaryImage(image_id).build_url()
        
        item.name = name
        item.price = price
        item.description = description
        item.link = link
        item.image = image_url
        
        item.save()
        shop_items = ShopItem.objects.all()
        shop_item_data = ShopItemSerializer(shop_items, many=True).data 
        
        return redirect('shop_list')

    item_data = ShopItemSerializer(item).data
    
    return render(request, "adminportal/shop_form.html", {
      "item": item_data
    })

@user_passes_test(user_is_superuser, login_url="user_login")
def shop_list(request):
    shop_list = ShopItem.objects.all().order_by('-price')
    paginator = Paginator(shop_list, 5)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, "adminportal/shop_list.html", {
        "items": items
    })

@user_passes_test(user_is_superuser, login_url="user_login")
def delete_shop_item(request, pk):
    item = ShopItem.objects.get(pk=pk)
    item.delete()
    
    return redirect('shop_list')
