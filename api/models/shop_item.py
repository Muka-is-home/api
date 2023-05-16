from django.db import models

class ShopItem(models.Model):
  name = models.CharField(max_length=55)
  description = models.TextField
  purchase_url = models.URLField
  image = models.ImageField
