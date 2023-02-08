from django.urls import path, include
from .views import *


urlpatterns = [
    path('person/token', PersonTokenObtainPairView.as_view(), name='person/token')
]