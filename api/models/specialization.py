from django.db import models

class Specialization(models.Model):
  tag_name = models.CharField(max_length=55)
