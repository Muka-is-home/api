from django.db import models
from django.contrib.auth.models import User as AuthUser
from .user_type import UserType


class User(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    email = models.EmailField()
    website = models.URLField()
    bio = models.TextField()
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    company = models.CharField(max_length=55)
    company_address = models.CharField(max_length=86)
    company_phone = models.CharField(max_length=17)
    contact_no = models.CharField(max_length=17)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    tiktok = models.URLField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)
    ready_for_approval = models.BooleanField(default=False)
