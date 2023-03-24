from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),

]
