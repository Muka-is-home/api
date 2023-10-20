from django.contrib import admin
from django.urls import path
from adminportal.views import MyLoginView, user_list, update_approval

urlpatterns = [
  path("login", MyLoginView.as_view(), name="login"),
  path("user_list", user_list, name="user_list"),
  path("update_approval", update_approval, name="update_approval")
]
