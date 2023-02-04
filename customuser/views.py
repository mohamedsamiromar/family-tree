from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *


class PersonTokenObtainPairView(TokenObtainPairView):

    def post(self, request):
        serializer = PersonTokenObtainPairSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)