from django.contrib import admin

from flightly.flight_booking.models import Flight, Reservation


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'capacity',
        'available_seats',
        'price',
        'departure_airport',
        'departure_datetime')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'ticket_number',
        'status',
        'ticket_price',
        'departure_time')
