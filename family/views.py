from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from . serializer import FamilyTreeSerializer,PersonModelSerializer
from . services import FamilyService


class Personview(viewsets.ViewSet):
    def create(self, request):
        serializer = FamilyTreeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = FamilyService.family_service(**serializer.validated_data)
        serializer = PersonModelSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

