from django.db import models

class Logo(models.Model):
  name = models.CharField(max_length=55)
  image = models.ImageField()
