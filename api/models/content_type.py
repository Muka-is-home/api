from django.db import models


class ContentType(models.Model):
    name = models.CharField(max_length=55)
