from django.db import models
from .user import User
from .county import County


class UserCounty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
