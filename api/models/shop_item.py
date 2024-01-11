from django.db import models
from cloudinary.models import CloudinaryField


class ShopItem(models.Model):
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    link = models.URLField()
    image = models.URLField()
