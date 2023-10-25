# https://www.django-rest-framework.org/api-guide/routers/
from django.urls import path
from adminapp.views import UserLoginView, user_detail, signup, edit_profile, create_profile
app_name = "adminapp"

urlpatterns = [
  path(f"{app_name}/login", UserLoginView.as_view(), name="user_login"),
  path(f"{app_name}/user_detail/<int:pk>", user_detail, name="user_detail"),
  path(f"{app_name}/signup", signup, name="signup"),
  path(f"{app_name}/profile/<str:type>", create_profile, name="profile"),
  path(f"{app_name}/edit_profile", edit_profile, name="edit_profile")
]
