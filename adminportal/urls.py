from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from adminportal.views import user_list, update_approval, edit_blog, create_blog, blog_list, delete_blog

app_name = "adminportal"

urlpatterns = [
  path(f"{app_name}/user_list", user_list, name="user_list"),
  path(f"{app_name}/update_approval", update_approval, name="update_approval"),
  path(f"{app_name}/access_denied", TemplateView.as_view(template_name="adminportal/access_denied.html"), name="access_denied"),
  path(f"{app_name}/edit_blog/<int:pk>", edit_blog, name="edit_blog"),
  path(f"{app_name}/create_blog", create_blog, name="create_blog"),
  path(f"{app_name}/blogs", blog_list, name="blogs"),
  path(f"{app_name}/delete_blog/<int:pk>", delete_blog, name="delete_blog")
]
