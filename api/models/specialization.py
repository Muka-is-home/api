from django.db import models


class Specialization(models.Model):
    tag_name = models.CharField(max_length=55)
    description = models.CharField(max_length=200)
    on_homepage = models.BooleanField()
