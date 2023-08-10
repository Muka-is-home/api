# https://www.django-rest-framework.org/api-guide/routers/
from django.urls import path

from adminapp.views import my_view, content_view

app_name = "adminapp"

urlpatterns = [
    path("", my_view, name="index"),
    path("content/", content_view, name="content"),
    path("content/<int:content_id>", content_view, name="single_content"),
    path("content/<int:content_id>/<str:is_edit>", content_view, name="editcontent"),
]
