# https://www.django-rest-framework.org/api-guide/routers/
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from adminapp.views import UserLoginView, user_detail, profile_signup, edit_profile, create_profile, signup, user_licenses, user_logout, edit_licenses, update_profile_picture
app_name = "muka"

urlpatterns = [
  path(f"{app_name}/login", UserLoginView.as_view(), name="user_login"),
  path(f"{app_name}/logout", user_logout, name="logout"),
  path(f"{app_name}/user_detail/<int:pk>", user_detail, name="user_detail"),
  path(f"{app_name}/profile_signup", profile_signup, name="profile_signup"),
  path(f"{app_name}/profile/<str:type>", create_profile, name="profile"),
  path(f"{app_name}/edit_profile/<int:pk>/<str:type>", edit_profile, name="edit_profile"),
  path(f"{app_name}/signup", signup, name="signup"),
  path(f"{app_name}/user_licenses", user_licenses, name="user_licenses"),
  path(f"{app_name}/thank_you", TemplateView.as_view(
    template_name = "adminapp/thank_you.html"
  ), name="thank_you"),
  path(f"{app_name}/rejected", TemplateView.as_view(template_name="adminapp/rejection.html"), name="rejection"),
  path(f"{app_name}/edit_licenses/<int:pk>", edit_licenses, name="edit_licenses"),
  path(f"{app_name}/update_profile_image/<int:pk>", update_profile_picture, name='update_profile_image')
]

password_reset_paths = [
  path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "adminapp/password_reset/reset_password.html"), name ='reset_password'),
  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "adminapp/password_reset/password_reset_sent.html"), name ='password_reset_done'),
  path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "adminapp/password_reset/password_reset_form.html"), name ='password_reset_confirm'),
  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "adminapp/password_reset/password_reset_done.html"), name ='password_reset_complete')
]

urlpatterns += password_reset_paths
