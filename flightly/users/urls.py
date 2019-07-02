from django.urls import path

from flightly.users.views import (
    FlightlyUserApiView, FlightlyUserDetailApiView, FlightlyUserCreateApiView
)

urlpatterns = [
    path(
        'users/all',
        FlightlyUserApiView.as_view(),
        name='flightlyusers-all'),
    path(
        'users/',
        FlightlyUserCreateApiView.as_view(),
        name='flightlyusers-create'),
    path(
        'user/<uuid:pk>',
        FlightlyUserDetailApiView.as_view(),
        name='flightlyuser-detail'),
]
