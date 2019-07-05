from flightly.flight_booking import views, models
from flightly.helpers.db.db_populator import populateFlights
from .commons import SetupWithNoUser, SetupWithAdminUser, SetupWithNonAdminUser

class SetupFlights(SetupWithNoUser):
    def setUp(self):
        populateFlights(5)
        super(SetupFlights).setUp()
