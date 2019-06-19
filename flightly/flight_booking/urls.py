from django.urls import path
from flightly.flight_booking.views import (
    FlightsApiView, FlightDetailApiView,
    ReservationListView, ReservationDetailApiView
)

urlpatterns = [
    path('api/v1/flights/', FlightsApiView.as_view(), name='flights-all'),
    path(
        'api/v1/flight/<uuid:pk>',
        FlightDetailApiView.as_view(),
        name='flight-detail'),
    path(
        'api/v1/reservations/',
        ReservationListView.as_view(),
        name='reservations-all'),
    path(
        'api/v1/reservation/<uuid:pk>',
        ReservationDetailApiView.as_view(),
        name='reservation-detail'),
]
