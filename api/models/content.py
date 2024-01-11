from django.db import models
from .user import User
from .content_type import ContentType


class Content(models.Model):
    title = models.CharField(max_length=55)
    body = models.TextField()
    author = models.CharField(max_length=55)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
