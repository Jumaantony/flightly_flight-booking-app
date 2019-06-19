import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from flightly.users.models import FlightlyUser


class Flight(models.Model):
    '''
    Flight:
        fields:
            name
            departure airport
            arrival airport
            departure datetime
            capacity
            price

        additional modification:
            - Make a available_seats property that returns available seats i.e capacity - reservations
            - Change id field to be of type uuid
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        _("Flight Name"),
        max_length=50,
        unique=True,
        null=False)
    departure_airport = models.CharField(
        _("Departure Airport"), max_length=50, null=False)
    arrival_airport = models.CharField(
        _("Arrival Airport"), max_length=50, null=False)
    departure_datetime = models.DateTimeField(_("Departure Time"))
    capacity = models.IntegerField(_("Carrying Capacity"), null=False)
    price = models.DecimalField(
        _("Ticket Price"),
        decimal_places=2,
        max_digits=10,
        default=0)

    @property
    def available_seats(self):
        return self.capacity - self.reservation_set.count()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    '''
    Reservation:
        fields:
            traveler (FK)
            flight (FK)
            ticket number
            status

        additional modification:
            - Make a status a Choice Field with paid, unpaid and canceled
            - Change id field to be of type uuid
    '''
    RESERVATION_STATUS = (
        ("unpaid", "Unpaid"),
        ("paid", "Paid"),
        ("cancelled", "Cancelled")
    )

    def generate_ticket_number():
        return uuid.uuid4().hex[:13]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    traveler = models.ForeignKey(FlightlyUser, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.SET_NULL, null=True)
    ticket_number = models.CharField(
        max_length=23,
        default=generate_ticket_number,
        unique=True)
    status = models.CharField(
        choices=RESERVATION_STATUS,
        max_length=10,
        default="unpaid")

    @property
    def ticket_price(self):
        return self.flight.price

    @property
    def departure_time(self):
        return self.flight.departure_datetime

    def __str__(self):
        return f"Reservation for Flight {self.flight} made by {self.traveler.username}."
