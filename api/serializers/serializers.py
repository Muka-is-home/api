from rest_framework import serializers
from api.models import User, Content, Specialization, ContentType, UserType, State, County, Tag
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
        fields = ('id', 'title', 'body', 'author', 'content_type', 'date', 'tags')
        depth = 1

class SpecializationSerializer(serializers.ModelSerializer):
    """serializer for vendor specializations"""

    class Meta:
        model = Specialization
        fields = ('id', 'tag_name', 'description', 'on_homepage')

class UserTypeSerializer(serializers.ModelSerializer):
    """serializer for user types"""

    class Meta:
        model = UserType
        fields = ('id', 'name')

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('id', 'name', 'abbreviation')

class CountySerializer(serializers.ModelSerializer):

    class Meta:
        model = County
        fields = ('id', 'name', 'state')
        depth = 1

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ('id', 'name')
