from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from api.models import User
from api.serializers import UserSerializer

class AgentView(ViewSet):
    """Agent views"""

    def retrieve(self, request, pk):
        """retrieves a single agent for detail view"""
        try:
            agent = User.objects.get(pk=pk, user_type__name='Realtor')
            serializer = UserSerializer(agent)
            response = serializer.data

        except User.DoesNotExist:
            response = {'message': 'No agent matching that id' }

        return Response(response, status=status.HTTP_200_OK)

    def list(self, request):
        """returns list of agents"""
        agents = User.objects.filter(user_type__name='Realtor', active=True)
        specialty = request.query_params.get('specialty')
        if specialty is not None:
            agents = agents.filter(specializations__specialization__tag_name=specialty)

        serializer = UserSerializer(agents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
