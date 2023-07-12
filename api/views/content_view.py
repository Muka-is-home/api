from rest_framework import filters, generics
from api.models import Content
from api.serializers import ContentSerializer

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('field', [])

class ContentView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = [CustomSearchFilter]
