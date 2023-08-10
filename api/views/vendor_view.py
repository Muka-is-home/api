from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from api.models import User
from api.serializers import UserSerializer

class VendorView(ViewSet):
    """Vendor views"""

    def retrieve(self, request, pk):
        """retrieves a single vendor for detail view"""
        try:
            vendor = User.objects.get(pk=pk, user_type__name='Vendor')
            serializer = UserSerializer(vendor)
            response = serializer.data

        except User.DoesNotExist:
            response = {'message': 'No vendor matching that id' }

        return Response(response, status=status.HTTP_200_OK)

    def list(self, request):
        """returns list of Vendors"""
        vendors = User.objects.filter(user_type__name='Vendor')
        specialty = request.query_params.get('specialty')
        if specialty is not None:
            vendors = vendors.filter(user_specialization__specialization__tag_name=specialty)

        serializer = UserSerializer(vendors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        