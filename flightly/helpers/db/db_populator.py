# coding: utf-8

# In[75]:


from flightly.helpers.db import airlines
from flightly.users.models import FlightlyUser
from flightly.flight_booking.models import Flight, Reservation
from django.db import IntegrityError
import pytz
import random
from faker import Faker
import itertools
import django
import os
import sys
from tqdm import tqdm
sys.path.insert(0, '.')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flightly.settings")
django.setup()


# In[76]:


# In[77]:


fake = Faker()


# In[78]:

def populateUsers(number=500):
    goal = 0
    while goal < number:
        try:
            fname = fake.first_name()
            lname = fake.last_name()
            email = fake.email()
            password = fake.password()
            user = FlightlyUser(email=email, first_name=fname, last_name=lname)
            user.set_password(password)
            user.save()
        except IntegrityError:
            continue

    print(f"FlightlyUsers populated Successfully.")
    return FlightlyUser.objects.all()

# In[82]:


def populateFlights(number=40):
    air_lines = airlines.get_reports(test=False)
    dep_airline_in_cycle = itertools.cycle(air_lines[:len(air_lines) // 2])
    random.shuffle(air_lines)
    arv_airline_in_cycle = itertools.cycle(air_lines[len(air_lines) // 2:])
    timezone = pytz.utc
    goal = 0
    while goal < number:
        try:
            dep_air_line = next(dep_airline_in_cycle)
            arv_air_line = next(arv_airline_in_cycle)
            name = f"{arv_air_line['Statistics']['Carriers']['Names'][1]} {random.randint(11,99)}"
            departure_airport = f"{dep_air_line['Airport']['Name'].split(':')[0]} ({dep_air_line['Airport']['Code']})"
            arrival_airport = f"{arv_air_line['Airport']['Name'].split(':')[0]} ({arv_air_line['Airport']['Code']})"
            departure_datetime = fake.future_datetime(
                end_date="+45d", tzinfo=timezone)
            capacity = fake.pyint(min=300, max=500, step=1)
            price = fake.pydecimal(
                right_digits=2, min_value=500, max_value=1500)

            _flight = Flight(
                name=name,
                departure_airport=departure_airport,
                arrival_airport=arrival_airport,
                departure_datetime=departure_datetime,
                capacity=capacity,
                price=price
            )
            if _flight.departure_airport != _flight.arrival_airport:
                _flight.save()
                goal += 1
        except IntegrityError:
            # A cheap way to escape IntegrityErrors due to similar names of
            # Flights
            continue
    print(f"Flights populated Successfully.")
    return Flight.objects.all()


# In[80]:

def populateReservations():
    travelers = itertools.cycle(FlightlyUser.objects.all())
    flights = itertools.cycle(Flight.objects.all())
    status_options = ['paid', 'unpaid', 'cancelled']
    for _ in tqdm(range(int(FlightlyUser.objects.all().count()
                            * Flight.objects.all().count() / 3.14))):
        traveler = next(travelers)
        flight = next(flights)
        status = random.choice(status_options)
        _reservation = Reservation(
            traveler=traveler, flight=flight, status=status)
        _reservation.save()

    print(f"Reservations populated Successfully.")
    return Reservation.objects.all()
# In[ ]:


if __name__ == '__main__':
    populateUsers()
    populateFlights()
    populateReservations()
