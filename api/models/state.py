from django.db import models


class State(models.Model):
    name = models.CharField(max_length=55)
    abbreviation = models.CharField(max_length=2)
