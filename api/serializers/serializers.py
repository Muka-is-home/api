from rest_framework.serializers import ModelSerializer
from api.models import User

class UserSerializer(ModelSerializer):
    """serializer for blog content"""

    class Meta:
        """fields"""
        model = User
        fields = ('name', 'website', 'bio', 'user', 'user_county')
        depth = 2
