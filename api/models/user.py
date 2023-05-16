from django.db import models
from .user_type import UserType

class User(models.Model):
  name = models.CharField(max_length=55)
  website = models.URLField()
  bio = models.TextField()
  user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
  active = models.BooleanField()
  image = models.ImageField()
 
  
