from rest_framework import serializers
from api.models import User, Content, Specialization

class UserSerializer(serializers.ModelSerializer):
    """serializer for user information"""

    class Meta:
        model = User
        fields = ('id','name', 'website', 'bio', 'email')
        depth = 2

    email = serializers.EmailField(source='user.email')

class ContentSerializer(serializers.ModelSerializer):
    """serializer for blog content"""

    class Meta:
        model = Content
        fields = ('id', 'title', 'body', 'author', 'content_type', 'date')
        depth = 1

class SpecializationSerializer(serializers.ModelSerializer):
    """serializer for vendor specializations"""

    class Meta:
        model = Specialization
        fields = ('id', 'tag_name', 'description', 'on_homepage')
