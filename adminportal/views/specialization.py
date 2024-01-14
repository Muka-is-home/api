from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from api.models import Specialization
from api.serializers import SpecializationSerializer
from adminportal.views import user_is_superuser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@user_passes_test(user_is_superuser, login_url="user_login")
def create_specialization(request):
    if request.method == 'POST':

        tag_name = request.POST.get("tag_name")
        description = request.POST.get("description")
        on_homepage = request.POST.get("on_homepage")
        
        if on_homepage is not None:
          on_homepage = True
        else:
          on_homepage = False
        
        Specialization.objects.create(
          tag_name=tag_name,
          description=description,
          on_homepage=on_homepage
        )
        
        specializations = Specialization.objects.all()
        specialization_data = SpecializationSerializer(specializations, many=True).data
        
        return redirect('specialization_list')
    
    else:

        homepage_count = Specialization.objects.filter(on_homepage=True).count()
        return render(request, "adminportal/specialization_form.html", {
          "homepage_limit": homepage_count >= 6
        })

@user_passes_test(user_is_superuser, login_url="user_login")
def edit_specialization(request, pk):
    specialization = Specialization.objects.get(pk=pk)
    
    if request.method == 'POST':
      
        tag_name = request.POST.get("tag_name")
        description = request.POST.get("description")
        on_homepage = request.POST.get("on_homepage")
        
        if on_homepage is not None:
          on_homepage = True
        else:
          on_homepage = False
        
        specialization.tag_name = tag_name
        specialization.description = description
        specialization.on_homepage = on_homepage
        specialization.save()
        
        specializations = Specialization.objects.all()
        specialization_data = SpecializationSerializer(specializations, many=True)
        
        return redirect('specialization_list')
    
    specialization_data = SpecializationSerializer(specialization).data
    homepage_count = Specialization.objects.filter(on_homepage=True).count()
    
    return render(request, "adminportal/specialization_form.html", {
      "specialization": specialization_data,
      "homepage_limit": homepage_count >= 6
    })

@user_passes_test(user_is_superuser, login_url="user_login")
def specialization_list(request):
    specialization_list = Specialization.objects.all()
    paginator = Paginator(specialization_list, 10)
    page = request.GET.get('page')

    try:
        specializations = paginator.page(page)
    except PageNotAnInteger:
        specializations = paginator.page(1)
    except EmptyPage:
        specializations = paginator.page(paginator.num_pages)
    return render(request, "adminportal/specialization_list.html", {
        "specializations": specializations
    })

@user_passes_test(user_is_superuser, login_url="user_login")
def delete_specialization(request, pk):
    specialization = Specialization.objects.get(pk=pk)
    specialization.delete()
    
    return redirect('specialization_list')
        