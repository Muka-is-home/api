from django.contrib import admin
from django.urls import path
from adminportal.views import MyLoginView, user_list, update_approval

app_name = "adminportal"

urlpatterns = [
  path(f"{app_name}/login", MyLoginView.as_view(), name="login"),
  path(f"{app_name}/user_list", user_list, name="user_list"),
  path(f"{app_name}/update_approval", update_approval, name="update_approval")
]