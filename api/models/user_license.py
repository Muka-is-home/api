from django.db import models
from api.models import User, State
    
class UserLicense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='licenses')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_licenses')
    license_no = models.CharField(max_length=55)    
