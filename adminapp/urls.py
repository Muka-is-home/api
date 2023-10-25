# https://www.django-rest-framework.org/api-guide/routers/
from django.urls import path
from adminapp.views import UserLoginView, user_detail, signup

app_name = "adminapp"

urlpatterns = [
  path(f"{app_name}/login", UserLoginView.as_view(), name="user_login"),
  path(f"{app_name}/user_detail/<int:pk>", user_detail, name="user_detail"),
  path(f"{app_name}/signup", signup, name="signup"),
  path(f"{app_name}/realtor_profile", name="realtor_profile"),
  path(f"{app_name}/vendor_profile", name="vendor_profile")
]
