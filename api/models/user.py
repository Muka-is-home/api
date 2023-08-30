from django.db import models
from django.contrib.auth.models import User as AuthUser
from .user_type import UserType


class User(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    website = models.URLField()
    bio = models.TextField()
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    company = models.CharField(max_length=55)
    company_address = models.CharField(max_length=86)
    company_phone = models.CharField(max_length=17)
    contact_no = models.CharField(max_length=17)
    facebook = models.URLField()
    instagram = models.URLField()
    tiktok = models.URLField()
    image = models.URLField()
