from rest_framework import serializers
from api.models import User, ShopItem

class UserListSerializer(serializers.ModelSerializer):
    """serializer for user list information"""

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'user', 'active', 'ready_for_approval')
        depth = 1

class ShopItemSerializer(serializers.ModelSerializer):
    """serializer for shop items in admin portal"""
    
    class Meta:
        model = ShopItem
        fields = ('id', 'name', 'price', 'description', 'link', 'image')
