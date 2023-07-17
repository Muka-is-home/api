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
        if self.request.query_params.get('vendor'):
            return UserSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        home_page = self.request.query_params.get('homePage')
        specialization = self.request.query_params.get('vendor')
        if home_page:
            return Specialization.objects.filter(on_homepage=True)
        elif specialization:
            return User.objects.filter(user_specialization__specialization__tag_name=specialization)
        else:
            return super().get_queryset()
