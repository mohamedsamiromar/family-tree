from rest_framework import viewsets
from rest_framework import permissions
from family import queries
from family.serializer import CreatePersonSerializer, PersonSerializer
from family.services import PersonService
from rest_framework.response import Response
from rest_framework import status


class PersonView(viewsets.ViewSet):
    permissions = [permissions.IsAuthenticated]

    def create(self, request):
        user = queries.get_user(user=1)
        serializer = CreatePersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = PersonService.create_person(
            user=user, **serializer.validated_data
        )
        return Response(PersonSerializer(instance).data, status=status.HTTP_200_OK)
