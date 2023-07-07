from django.db import models
from .content import Content
from .tag import Tag


class ContentTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
