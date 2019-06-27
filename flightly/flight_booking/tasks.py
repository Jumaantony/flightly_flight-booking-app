from flightly.flight_booking.models import Flight
from datetime import datetime, timedelta
from django.conf import settings
from pytz import timezone
from numpy import array_split
from threading import Thread


class SendEmailReminder:

    def __init__(self, *args, chunk_num=5, **kwargs):
        self.chunk_num = chunk_num

    def __call__(self, *args, **kwargs):
        # Fetch flights that will departure time in the next 24hours
        # Chunk them into clusters
        # Send emails to travelers with paid reservations (flight info and
        # time)

        for index, chunk in enumerate(self.chunked_flight_list()):
            mailing_thread = Thread(
                name=f"Mailing Thread #{index + 1}",
                target=self.run_mailing_thread,
                args=(chunk, )
            )
            mailing_thread.start()

    def chunked_flight_list(self):
        return array_split(
            self.fetch_list_flight_to_notify_about(), self.chunk_num)

    def run_mailing_thread(self, chunk):
        if not any(chunk):
            return
        for flight in chunk:
            for reservation in flight.reservation_set.all():
                if reservation.status == 'paid':
                    self.send_email(reservation.traveler, flight, reservation)

    @staticmethod
    def fetch_list_flight_to_notify_about():
        now = datetime.now(tz=timezone(settings.TIME_ZONE))
        now_plus_24 = now + timedelta(days=1)
        return Flight.objects.filter(
            departure_datetime__gte=now,
            departure_datetime__lte=now_plus_24
        )

    @staticmethod
    def send_email(user, flight, reservation):

        subject = f"Flight Reminder {flight.name} | {flight.departure_airport}/{flight.arrival_airport}"
        message = f"""
        Dear {user.first_name or 'customer' },

        This is a reminder for your scheduled flight detailed below.

        Flight Name: {flight.name}
        Flight Time: {flight.departure_datetime}
        Ticket Number: {reservation.ticket_number}
        Departure Airport: {flight.departure_airport}
        Destination Airport: {flight.arrival_airport}

        Thank you for choosing Flightly

        """
        user.email_user(
            subject=subject,
            message=message,
        )
