from rest_framework import serializers
from api.models import User

class UserListSerializer(serializers.ModelSerializer):
    """serializer for user list information"""
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'user', 'active', 'ready_for_approval')
        depth = 1
