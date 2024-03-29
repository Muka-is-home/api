from django.db import models
from .user import User
from .specialization import Specialization


class UserSpecialization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='specializations')
    specialization = models.ForeignKey(
        Specialization, on_delete=models.CASCADE)
