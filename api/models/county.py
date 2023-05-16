from django.db import models
from .state import State

class County(models.Model):
  name = models.CharField(max_length=55)
  state = models.ForeignKey(State, on_delete=models.CASCADE)
