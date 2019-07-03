from rest_framework import generics
from django.db.models.query import QuerySet


from flightly.flight_booking.models import Flight, Reservation
from flightly.flight_booking.serializers import FlightSerializer, ReservationSerializer
from flightly.flight_booking.permissions import (
    IsReservationOwnerOrAdminOnly, IsAuthenticated,
    IsAdminUserOrReadOnly
    )


class FlightsApiView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUserOrReadOnly,)
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUserOrReadOnly,)
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class ReservationListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReservationSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            queryset = Reservation.objects.all()
        else:
            queryset = Reservation.objects.filter(
            traveler = user
            )
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset



class ReservationDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsReservationOwnerOrAdminOnly,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
