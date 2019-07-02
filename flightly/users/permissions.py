from rest_framework.permissions import BasePermission, IsAdminUser


class IsOwnerOrAdminOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj == user or user.is_staff or user.is_superuser
