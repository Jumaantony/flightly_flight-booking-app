from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

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
]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
    )
