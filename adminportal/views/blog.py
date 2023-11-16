from django.shortcuts import render
from django.contrib.auth.models import User as AuthUser
from api.models import Content, ContentTag, ContentType, User, Tag
from api.serializers import ContentSerializer, ContentTypeSerializer, TagSerializer
from adminportal.serializers.serializers import UserListSerializer

def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        date = request.POST.get("date")
        
        tag_ids = request.POST.getlist("tags")
        content_type = ContentType.objects.get(pk=request.POST.get("content_type"))
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
    
    return render(request, "adminportal/blog_form.html", {
      "content_types": content_type_data,
      "tags": tag_data
    })
