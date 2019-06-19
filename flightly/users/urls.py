from django.urls import path
from flightly.users.views import (
    FlightlyUserApiView, FlightlyUserDetailApiView
)

urlpatterns = [
    path(
        'api/v1/users/',
        FlightlyUserApiView.as_view(),
        name='flightlyusers-all'),
    path(
        'api/v1/user/<uuid:pk>',
        FlightlyUserDetailApiView.as_view(),
        name='flightlyuser-detail'),
]
