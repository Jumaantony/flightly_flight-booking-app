from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from django.db.models.query import QuerySet

from flightly.users.serializers import FlightlyUserSerializer
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
                traveler=user
            )
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset

    def perform_create(self, serializer):
        # import pdb; pdb.set_trace()
        user = serializer.context['request'].user
        if user.is_staff or user.is_superuser or serializer.validated_data['traveler'] == user:
            serializer.save()
        else:
            raise PermissionDenied(
                detail='You are not authorized to make reservations for other users'
            )


class ReservationDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsReservationOwnerOrAdminOnly, IsAuthenticated)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
