# https://www.django-rest-framework.org/api-guide/routers/
from django.urls import path
from django.views.generic import TemplateView
from adminapp.views import UserLoginView, user_detail, profile_signup, edit_profile, create_profile, signup, user_licenses
app_name = "adminapp"

urlpatterns = [
  path(f"{app_name}/login", UserLoginView.as_view(), name="user_login"),
  path(f"{app_name}/user_detail/<int:pk>", user_detail, name="user_detail"),
  path(f"{app_name}/profile_signup", profile_signup, name="profile_signup"),
  path(f"{app_name}/profile/<str:type>", create_profile, name="profile"),
  path(f"{app_name}/edit_profile", edit_profile, name="edit_profile"),
  path(f"{app_name}/signup", signup, name="signup"),
  path(f"{app_name}/user_licenses", user_licenses, name="user_licenses"),
  path(f"{app_name}/thank_you", TemplateView.as_view(
    template_name = "adminapp/thank_you.html"
  ), name="thank_you"),
  path(f"{app_name}/rejected", TemplateView.as_view(template_name="adminapp/rejection.html"), name="rejection")
]
