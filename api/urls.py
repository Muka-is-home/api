# https://www.django-rest-framework.org/api-guide/routers/
from rest_framework import routers
from django.urls import path, include
from .views import ShopItemView, LogoView, EmailView, ContentView, SpecializationView, SearchView, VendorView, AgentView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'emails', EmailView, 'email')
router.register(r'shop', ShopItemView, 'shop_item')
router.register(r'logos', LogoView, 'logo')
router.register(r'search', SearchView, 'search')
router.register(r'vendors', VendorView, 'vendor')
router.register(r'agents', AgentView, 'agent')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/content', ContentView.as_view()),
    path('api/specializations', SpecializationView.as_view())
]
