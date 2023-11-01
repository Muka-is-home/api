from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from adminportal.views import user_list, update_approval

app_name = "adminportal"

urlpatterns = [
  path(f"{app_name}/user_list", user_list, name="user_list"),
  path(f"{app_name}/update_approval", update_approval, name="update_approval"),
  path(f"{app_name}/access_denied", TemplateView.as_view(template_name="adminportal/access_denied.html"), name="access_denied")
]
