from rest_framework import serializers
from api.models import User, Content, Specialization, ContentType
from rest_framework.serializers import ModelSerializer

class ContentTypeSerializer(ModelSerializer):
    """serializer for blog content type"""

    class Meta:
        """fields"""
        model = ContentType
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    """serializer for user information"""

    class Meta:
        model = User
        fields = ('id','name', 'website', 'bio', 'email', 'user_type')
        depth = 1


class ContentSerializer(ModelSerializer):
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
