from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from api.models import Content, ContentTag, ContentType, User, Tag
from api.serializers import ContentSerializer, ContentTypeSerializer, TagSerializer
from adminportal.views import user_is_superuser
from adminportal.serializers.serializers import UserListSerializer

def create_blog(request):
    if request.method == "POST":
        
        content_type = ContentType.objects.get(pk=request.POST.get("content_type"))
        title = request.POST.get("title")
        content = request.POST.get("content")
        date = request.POST.get("date")            
        tag_ids = request.POST.getlist("tags")
        author = User.objects.get(user=request.user)                            
        
        new_post = Content.objects.create(
            title = title,
            body = content,
            author = author,
            content_type = content_type,
            date = date
        )
            
        for tag_id in tag_ids:
            tag = Tag.objects.get(pk=tag_id)
            ContentTag.objects.create(
                tag = tag,
                content = new_post
            )
            
        users = User.objects.exclude(user__is_superuser=True)
        user_data = UserListSerializer(users, many=True).data
            
        return render(request, "adminportal/user_list.html", {
        "users": user_data
        })

    content_types = ContentType.objects.all()
    content_type_data = ContentTypeSerializer(content_types, many=True).data
    
    tags = Tag.objects.all()
    tag_data = TagSerializer(tags, many=True).data
    
    return render(request, "adminportal/create_blog_form.html", {
      "content_types": content_type_data,
      "tags": tag_data
    })

def edit_blog(request, pk):
    
    blog = Content.objects.get(pk=pk)

    if request.method == 'POST':
        
        tag_ids = request.POST.getlist("tags")
        content_type = ContentType.objects.get(pk=request.POST.get("content_type"))
            
        blog.title = request.POST.get("title")
        blog.body = request.POST.get("content")
        blog.date = request.POST.get("date")
        blog.content_type = content_type
            
        blog.save()
            
        for content_tag in ContentTag.objects.filter(content=blog):
            content_tag.delete()
            
        for tag_id in tag_ids:
            tag = Tag.objects.get(pk=tag_id)
            ContentTag.objects.create(
                tag = tag,
                content = blog
            )            
        
        blog_posts = Content.objects.all()
        blog_data = ContentSerializer(blog_posts, many=True).data           
        return render(request, "adminportal/blog_list.html", {
        "blogs": blog_data
        })

    content_types = ContentType.objects.all()
    content_type_data = ContentTypeSerializer(content_types, many=True).data
    
    tags = Tag.objects.all()
    tag_data = TagSerializer(tags, many=True).data
    
    blog_data = ContentSerializer(blog).data
    blog_tags = blog.tags.values_list('tag_id', flat=True)
    
    return render(request, "adminportal/edit_blog_form.html", {
      "content_types": content_type_data,
      "tags": tag_data,
      "blog": blog_data,
      "blog_tags": blog_tags
    })

@user_passes_test(user_is_superuser, login_url="access_denied")
def blog_list(request):
    blog_list = Content.objects.all().order_by('-date')

    paginator = Paginator(blog_list, 10)
    page = request.GET.get('page')

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, "adminportal/blog_list.html", {
        "blogs": blogs
    })

def delete_blog(request, pk):
    
    blog = Content.objects.get(pk=pk)
    blog.delete()
    
    return blog_list(request)
    

    