from rest_framework import serializers
from api.models import User

class UserFormSerializer(serializers.ModelSerializer):
    """serializer for form in adminapp"""

    class Meta:
        model = User
        fields = ('id', 'name', 'website', 'bio', 'company', 'company_address', 'company_phone', 'contact_no', 'facebook', 'instagram', 'tiktok', 'image', 'licenses', 'user_type', 'specializations', 'counties', 'email')
        depth = 2
