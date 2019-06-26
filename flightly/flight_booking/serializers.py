from rest_framework import serializers

from flightly.flight_booking.models import Flight, Reservation


class FlightSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Flight
        fields = (
            'url',
            'id',
            'name',
            'departure_airport',
            'arrival_airport',
            'departure_datetime',
            'capacity',
            'price',
            'available_seats',
        )


class ReservationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reservation
        fields = (
            'url',
            'id',
            'traveler',
            'flight',
            'ticket_number',
            'status',
        )
        read_only_fields = ('ticket_number', 'status',)
