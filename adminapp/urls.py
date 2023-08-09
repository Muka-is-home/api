# https://www.django-rest-framework.org/api-guide/routers/
from django.urls import path

from adminapp.views import my_view

urlpatterns = [
    path("", my_view, name="index"),
]
