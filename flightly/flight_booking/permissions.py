from rest_framework.permissions import (
    BasePermission, IsAuthenticated,
    IsAdminUser, SAFE_METHODS)


class IsTravelerOrAdminOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.traveler == user or user.is_admin or user.is_superuser


class IsReservationOwnerOrAdminOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.traveler == user or user.is_staff or user.is_superuser


class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly,
            self).has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin
