from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework.response import Response
from . service import *


class PersonTokenObtainPairView(TokenObtainPairView):

    def post(self, request):
        serializer = PersonTokenObtainPairSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('email'))
        return Response(serializer.validated_data)