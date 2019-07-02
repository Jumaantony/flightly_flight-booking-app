from rest_framework import generics, filters

from flightly.users.models import FlightlyUser
from flightly.users.serializers import FlightlyUserSerializer
from flightly.users.permissions import (IsOwnerOrAdminOnly, IsAdminUser)


class FlightlyUserApiView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = FlightlyUser.objects.all()
    serializer_class = FlightlyUserSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    search_fields = ('first_name','last_name', 'email')
    ordering_fields = ('first_name','last_name')


class FlightlyUserCreateApiView(generics.CreateAPIView):
    serializer_class = FlightlyUserSerializer


class FlightlyUserDetailApiView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrAdminOnly,)
    queryset = FlightlyUser.objects.all()
    serializer_class = FlightlyUserSerializer
