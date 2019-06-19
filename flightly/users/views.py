from rest_framework import generics

from flightly.users.models import FlightlyUser
from flightly.users.serializers import FlightlyUserSerializer


class FlightlyUserApiView(generics.ListCreateAPIView):
    queryset = FlightlyUser.objects.all()
    serializer_class = FlightlyUserSerializer


class FlightlyUserDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlightlyUser.objects.all()
    serializer_class = FlightlyUserSerializer