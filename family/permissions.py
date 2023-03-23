from rest_framework.permissions import BasePermission
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _


class PersonPermission(BasePermission):
    message = _('User has no profile or role.')

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        user = request.user
        if user.is_blocked:
            self.message = _('User is banned!')
            return False
        if user.groups.filter(name='person').exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
                    return True

