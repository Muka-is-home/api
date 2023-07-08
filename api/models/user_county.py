from django.db import models
from .user import User
from .county import County


class UserCounty(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_county')
  county = models.ForeignKey(County, on_delete=models.CASCADE)
