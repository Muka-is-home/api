from rest_framework.serializers import ModelSerializer
from api.models import User, Content

class UserSerializer(ModelSerializer):
    """serializer for blog content"""

    class Meta:
        """fields"""
        model = User
        fields = ('name', 'website', 'bio', 'user', 'user_county')
        depth = 2

class ContentSerializer(ModelSerializer):
    """serializer for blog content"""

    class Meta:
        """fields"""
        model = Content
        fields = ('id', 'title', 'body', 'author', 'content_type', 'date')
        depth = 1