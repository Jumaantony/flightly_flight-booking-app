from django.urls import path
from flightly.flight_booking.views import (
    FlightsApiView, FlightDetailApiView,
    ReservationListView, ReservationDetailApiView
)

urlpatterns = [
    path('flights/', FlightsApiView.as_view(), name='flights-all'),
    path(
        'flight/<uuid:pk>',
        FlightDetailApiView.as_view(),
        name='flight-detail'),
    path(
        'reservations/',
        ReservationListView.as_view(),
        name='reservations-all'),
    path(
        'reservation/<uuid:pk>',
        ReservationDetailApiView.as_view(),
        name='reservation-detail'),
]
