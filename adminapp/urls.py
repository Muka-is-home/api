from django.urls import path

from adminapp.admin import admin_site

urlpatterns = [
    path("admin/", admin_site.urls),
]
