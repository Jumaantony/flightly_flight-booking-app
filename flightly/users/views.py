from rest_framework import generics, filters

from flightly.users.models import FlightlyUser
from flightly.users.serializers import FlightlyUserSerializer


class FlightlyUserApiView(generics.ListCreateAPIView):
    queryset = FlightlyUser.objects.all()
    serializer_class = FlightlyUserSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    search_fields = ('first_name','last_name', 'email')
    ordering_fields = ('first_name','last_name')


class FlightlyUserDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlightlyUser.objects.all()
    serializer_class = FlightlyUserSerializer
    