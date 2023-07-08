# https://www.django-rest-framework.org/api-guide/routers/
from rest_framework import routers
from .views import ShopItemView, LogoView, EmailView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'emails', EmailView, 'email')
router.register(r'shop', ShopItemView, 'shop_item')
router.register(r'logos', LogoView, 'logo')
