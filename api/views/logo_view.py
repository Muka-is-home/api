from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from api.models import Logo


class LogoView(ViewSet):
    def list(self, _):
        logos = Logo.objects.all()
        serialized = LogoSerializer(logos, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ('id', 'name')
