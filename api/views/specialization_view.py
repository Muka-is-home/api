from rest_framework import filters, generics
from api.models import Specialization, User
from api.serializers import SpecializationSerializer, UserSerializer

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('field', [])

class SpecializationView(generics.ListAPIView):
    queryset = Specialization.objects.all()
    filter_backends = [CustomSearchFilter]
    serializer_class = SpecializationSerializer

    def get_serializer_class(self):
        if self.request.query_params.get('service'):
            return UserSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        home_page = self.request.query_params.get('homePage')
        specialization = self.request.query_params.get('service')
        if home_page:
            return Specialization.objects.filter(on_homepage=True)
        if specialization:
            return User.objects.filter(user_specialization__specialization__tag_name=specialization)
        return super().get_queryset()
