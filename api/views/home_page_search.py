from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.models import User, UserCounty
from api.serializers import UserSerializer

class SearchView(ViewSet):
    """Search View"""

    def list(self, request):
        """Search lists"""

        user_type = request.query_params.get('userType')
        state = request.query_params.get('state')
        county = request.query_params.get('county')
        users = User.objects.filter(user_type__name=user_type)
        if user_type and not state:
            user_counties = UserCounty.objects.filter(user__user_type__name=user_type)
            response = set([user_county.county.state.name for user_county in user_counties])
        elif user_type and state and not county:
            counties = UserCounty.objects.filter(user__user_type__name=user_type, county__state__name=state)
            response = set([county.county.name for county in counties])
        else:
            user_list = users.filter(user_county__county__name=county, user_county__county__state__name=state, active=True)
            serializer = UserSerializer(user_list, many=True)
            response = serializer.data

        return Response(response)
