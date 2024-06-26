from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsOwnerOrEmployee(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):

        if request.user.is_employee or request.user.is_superuser:
            return True

        return obj.id == request.user.id
