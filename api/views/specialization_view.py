from rest_framework import filters, generics
from api.models import Specialization
from api.serializers import SpecializationSerializer

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('field', [])

class SpecializationView(generics.ListAPIView):
    queryset = Specialization.objects.all()
    filter_backends = [CustomSearchFilter]
    serializer_class = SpecializationSerializer

    def get_queryset(self):
        home_page = self.request.query_params.get('homePage')
        if home_page:
            return Specialization.objects.filter(on_homepage=True, userspecialization__user__user_type__name='Vendor').distinct()
        return super().get_queryset()
