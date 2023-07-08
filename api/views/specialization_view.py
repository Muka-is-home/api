from rest_framework import filters, generics
from api.models import Specialization
from api.serializers import SpecializationSerializer

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('field', [])

class SpecializationView(generics.ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    filter_backends = [CustomSearchFilter]

    def finalize_response(self, request, response, *args, **kwargs):
        if request.query_params.get('limit') == 'True':
            response.data = response.data[:6]

        return super().finalize_response(request, response, *args, **kwargs)
