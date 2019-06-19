from django.contrib import admin

from flightly.flight_booking.models import Flight, Reservation


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'price',
        'capacity',
        'available_seats',
        'departure_airport',
        'departure_datetime')
    list_editable = ('capacity', 'price', 'departure_datetime')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'ticket_number',
        'status',
        'ticket_price',
        'departure_time')
    list_editable = ('status',)
    list_per_page = 20
