from flightly.flight_booking import views, models
from flightly.helpers.db.db_populator import populateFlights
from .commons import SetupWithNoUser, SetupWithAdminUser, SetupWithNonAdminUser


class SetupFlights(SetupWithNoUser):

    def setUp(self):
        super().setUp()
        self.list_uri = self.base_url + 'flights/'
        self.detail_uri = self.base_url + 'flight/'

    @classmethod
    def setUpTestData(self):
        self.inserted_num = 5
        self.flights = populateFlights(self.inserted_num)


class TestWithAnonUser(SetupFlights):

    def test_user_can_view_list_of_flights(self):
        response = self.client.get(self.list_uri)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')
        self.assertEqual(response.data['count'], self.inserted_num,
                         f"Expected {self.inserted_num} Flights, received {response.data['count']} instead.")

    def test_user_cannot_create_flights(self):
        data = '''{
            "name": "Gremlin Airlines Inc. 25",
            "departure_airport": "Hotel Transylvania",
            "arrival_airport": "Bermuda Triangle",
            "departure_datetime": "2019-09-08T00:00:00Z",
            "capacity": 666,
            "price": 0
        }'''
        response = self.client.post(
            self.list_uri,
            data=data,
            content_type='application/json')
        self.assertEqual(response.status_code, 401,
                         f'Expected Response Code 401, received {response.status_code} instead.')

    def test_user_can_retrieve_one_flight(self):
        response = self.client.get(
            self.detail_uri + str(self.flights.first().id))
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')
        # Checking for empty responses
        self.assertTrue(bool(response.data))

    def test_user_cannot_update_a_flight(self):
        data = '''{
            "name": "Gremlin Airlines Inc. 25",
            "departure_airport": "Hotel Transylvania",
            "arrival_airport": "Bermuda Triangle",
            "departure_datetime": "2019-09-08T00:00:00Z",
            "capacity": 666,
            "price": 0
        }'''
        response = self.client.put(
            self.detail_uri + str(self.flights.first().id),
            data=data,
            content_type='application/json')
        self.assertEqual(response.status_code, 401,
                         f'Expected Response Code 401, received {response.status_code} instead.')

    def test_user_cannot_delete_a_flight(self):
        response = self.client.delete(
            self.detail_uri + str(self.flights.first().id))
        self.assertEqual(response.status_code, 401,
                         f'Expected Response Code 401, received {response.status_code} instead.')


class TestWithNonAdminUser(SetupFlights, SetupWithNonAdminUser):

    def test_user_can_view_list_of_flights(self):
        response = self.client.get(self.list_uri)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')
        self.assertEqual(response.data['count'], self.inserted_num,
                         f"Expected {self.inserted_num} Flights, received {response.data['count']} instead.")

    def test_user_cannot_create_flights(self):
        data = '''{
            "name": "Gremlin Airlines Inc. 25",
            "departure_airport": "Hotel Transylvania",
            "arrival_airport": "Bermuda Triangle",
            "departure_datetime": "2019-09-08T00:00:00Z",
            "capacity": 666,
            "price": 0
        }'''
        response = self.client.post(
            self.list_uri,
            data=data,
            content_type='application/json')
        self.assertEqual(response.status_code, 403,
                         f'Expected Response Code 403, received {response.status_code} instead.')

    def test_user_can_retrieve_one_flight(self):
        response = self.client.get(
            self.detail_uri + str(self.flights.first().id))
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')
        # Checking for empty responses
        self.assertTrue(bool(response.data))

    def test_user_cannot_update_a_flight(self):
        data = '''{
            "name": "Gremlin Airlines Inc. 25",
            "departure_airport": "Hotel Transylvania",
            "arrival_airport": "Bermuda Triangle",
            "departure_datetime": "2019-09-08T00:00:00Z",
            "capacity": 666,
            "price": 0
        }'''
        response = self.client.put(
            self.detail_uri + str(self.flights.first().id),
            data=data,
            content_type='application/json')
        self.assertEqual(response.status_code, 403,
                         f'Expected Response Code 403, received {response.status_code} instead.')

    def test_user_cannot_delete_a_flight(self):
        response = self.client.delete(
            self.detail_uri + str(self.flights.first().id))
        self.assertEqual(response.status_code, 403,
                         f'Expected Response Code 403, received {response.status_code} instead.')


class TestWithAdminUser(SetupFlights, SetupWithAdminUser):

    def test_user_can_view_list_of_flights(self):
        response = self.client.get(self.list_uri)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')
        self.assertEqual(response.data['count'], self.inserted_num,
                         f"Expected {self.inserted_num} Flights, received {response.data['count']} instead.")

    def test_user_can_create_flights(self):
        data = '''{
         "name": "Gremlin Airlines Inc. 25",
         "departure_airport": "Hotel Transylvania",
         "arrival_airport": "Bermuda Triangle",
         "departure_datetime": "2019-09-08T00:00:00Z",
         "capacity": 666,
         "price": 0
     }'''
        response = self.client.post(
            self.list_uri,
            data=data,
            content_type='application/json')
        self.assertEqual(response.status_code, 201,
                         f'Expected Response Code 201, received {response.status_code} instead.')

    def test_user_can_retrieve_one_flight(self):
        response = self.client.get(
            self.detail_uri + str(self.flights.first().id))
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')
        # Checking for empty responses
        self.assertTrue(bool(response.data))

    def test_user_can_update_a_flight(self):
        data = '''{
         "name": "Gremlin Airlines Inc. 23",
         "departure_airport": "Hotel Transylvania",
         "arrival_airport": "Bermuda Triangle",
         "departure_datetime": "2019-09-08T00:00:00Z",
         "capacity": 666,
         "price": 0
     }'''
        response = self.client.put(
            self.detail_uri + str(self.flights.first().id),
            data=f"{data}",
            content_type='application/json')
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')

    def test_user_can_delete_a_flight(self):
        response = self.client.delete(
            self.detail_uri + str(self.flights.first().id))
        self.assertEqual(response.status_code, 204,
                         f'Expected Response Code 204, received {response.status_code} instead.')
