from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from adminportal.views import user_list, update_approval, edit_blog, create_blog, blog_list, delete_blog, create_shop_item, edit_shop_item, shop_list, delete_shop_item, create_specialization, edit_specialization, specialization_list, delete_specialization

app_name = "muka"

urlpatterns = [
  path(f"{app_name}/user_list", user_list, name="user_list"),
  path(f"{app_name}/update_approval", update_approval, name="update_approval"),
  path(f"{app_name}/access_denied", TemplateView.as_view(template_name="adminportal/access_denied.html"), name="access_denied"),
  path(f"{app_name}/edit_blog/<int:pk>", edit_blog, name="edit_blog"),
  path(f"{app_name}/create_blog", create_blog, name="create_blog"),
  path(f"{app_name}/blogs", blog_list, name="blogs"),
  path(f"{app_name}/delete_blog/<int:pk>", delete_blog, name="delete_blog"),
  path(f"{app_name}/create_shop_item", create_shop_item, name="create_shop_item"),
  path(f"{app_name}/edit_shop_item/<int:pk>", edit_shop_item, name="edit_shop_item"),
  path(f"{app_name}/shop_list", shop_list, name="shop_list"),
  path(f"{app_name}/delete_shop_item/<int:pk>", delete_shop_item, name="delete_shop_item"),
  path(f"{app_name}/create_specialization", create_specialization, name="create_specialization"),
  path(f"{app_name}/edit_specialization/<int:pk>", edit_specialization, name="edit_specialization"),
  path(f"{app_name}/specialization_list", specialization_list, name="specialization_list"),
  path(f"{app_name}/delete_specialization/<int:pk>", delete_specialization, name="delete_specialization"),
]
