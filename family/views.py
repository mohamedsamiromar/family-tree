from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from family import queries
from family.serializer import CreatePersonSerializer, PersonSerializer
from family.services import PersonService
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from . permissions import PersonPermission


class PersonView(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated, PersonPermission]

    def create(self, request):
        user = queries.get_user(user=request.user)
        serializer = CreatePersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = PersonService.create_person(
            user=user, **serializer.validated_data
        )
        return Response(PersonSerializer(instance).data, status=status.HTTP_200_OK)
