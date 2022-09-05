from django.urls import path, include, re_path
from family.views import PersonView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('person', PersonView, basename='person'),

urlpatterns = [
    path('', include(router.urls)),

]
