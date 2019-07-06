from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from flightly.flight_booking import models, serializers, views
from flightly.users.serializers import FlightlyUserSerializer
from flightly.helpers.db.db_populator import populateReservations, populateFlights, populateUsers
from .commons import SetupWithNoUser, SetupWithAdminUser, SetupWithNonAdminUser


class SetupReservations(SetupWithNoUser):

    def setUp(self):
        super().setUp()
        self.list_uri = self.base_url + 'reservations/'
        self.detail_uri = self.base_url + 'reservation/'
        self.user_serializer = FlightlyUserSerializer
        self.flight_serializer = serializers.FlightSerializer
        self.factory = APIRequestFactory()
        self.request = Request(self.factory.get(self.base_url))
        self.context = {
            'request': self.request
        }
        self.flight_url = self.flight_serializer(
            self.flights.first(),
            context=self.context
        )['url'].value
        self.flight_url2 = self.flight_serializer(
            self.flights.last(),
            context=self.context
        )['url'].value

    @classmethod
    def setUpTestData(self):
        self.inserted_flights = 5
        self.inserted_users = 2
        self.users = populateUsers(self.inserted_users)
        self.flights = populateFlights(self.inserted_flights)
        self.reservations = populateReservations()


class TestWithAnonUser(SetupReservations):

    def test_admin_cannot_view_list_of_reservatios(self):
        response = self.client.get(self.list_uri)
        self.assertEqual(response.status_code, 401,
                         f'Expected Response Code 401, received {response.status_code} instead.')

    def test_user_cannot_create_reservations(self):

        data = {
            "flight": f"{self.flight_url}"
        }
        response = self.client.post(
            self.list_uri,
            data,
            format='multipart')
        self.assertEqual(response.status_code, 401,
                         f'Expected Response Code 401, received {response.status_code} instead.')

    def test_user_cannot_retrieve_reservation_details(self):
        response = self.client.get(
            self.detail_uri + str(self.reservations.first().id))
        self.assertEqual(response.status_code, 401,
                         f'Expected Response Code 401, received {response.status_code} instead.')

    def test_user_cannot_update_a_reservation(self):
        data = {
            "flight": f"{self.flight_url}",
        }
        response = self.client.put(
            self.detail_uri + str(self.flights.first().id),
            data=data,
            format='multipart')
        self.assertEqual(response.status_code, 401,
                         f'Expected Response Code 401, received {response.status_code} instead.')

    def test_user_cannot_delete_a_reservation(self):
        response = self.client.delete(
            self.detail_uri + str(self.reservations.first().id))
        self.assertEqual(response.status_code, 401,
                         f'Expected Response Code 401, received {response.status_code} instead.')


class TestWithNonAdminUser(SetupReservations, SetupWithNonAdminUser):

    def setUp(self):
        super(TestWithNonAdminUser, self).setUp()
        self.user_url = self.user_serializer(
            self.user,
            context=self.context
        )['url'].value

    def create_user_specific_reservation(self, user_url, flight_url):
        creation_data = {
            "traveler": f"{user_url}",
            "flight": f"{flight_url}"
        }
        self.client.post(
            self.list_uri,
            creation_data,
            format='multipart'
        )

    def test_user_can_only_view_own_list_of_reservations(self):
        response = self.client.get(self.list_uri)
        expected_reservations = self.user.reservation_set.count()
        self.assertEqual(response.data['count'], expected_reservations,
                         f'Expected {expected_reservations} reservations, received {response.data["count"]}')
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')

    def test_user_can_create_reservation_for_self(self):
        data = {
            "traveler": f"{self.user_url}",
            "flight": f"{self.flight_url}"
        }
        response = self.client.post(
            self.list_uri,
            data,
            format='multipart')
        self.assertEqual(response.status_code, 201,
                         f'Expected Response Code 201, received {response.status_code} instead.')

    def test_user_can_retrieve_reservation_details(self):
        self.create_user_specific_reservation(
            self.user_url,
            self.flight_url
        )
        response = self.client.get(
            self.detail_uri + str(self.user.reservation_set.first().id))
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')

    def test_user_can_update_a_reservation(self):
        self.create_user_specific_reservation(
            self.user_url,
            self.flight_url
        )
        update_data = {
            "flight": f"{self.flight_url2}",
            "traveler": f"{self.user_url}"
        }
        response = self.client.put(
            self.detail_uri + str(self.user.reservation_set.first().id),
            update_data,
            format='multipart'
        )
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')

    def test_user_can_delete_a_reservation(self):
        self.create_user_specific_reservation(
            self.user_url,
            self.flight_url
        )
        response = self.client.delete(
            self.detail_uri + str(self.user.reservation_set.first().id))
        self.assertEqual(response.status_code, 204,
                         f'Expected Response Code 204, received {response.status_code} instead.')


class TestWithAdminUser(SetupReservations, SetupWithAdminUser):

    def setUp(self):
        super(TestWithAdminUser, self).setUp()
        self.user_url = self.user_serializer(
            self.admin,
            context=self.context
        )['url'].value

    def create_admin_specific_reservation(self, user_url, flight_url):
        creation_data = {
            "traveler": f"{user_url}",
            "flight": f"{flight_url}"
        }
        self.client.post(
            self.list_uri,
            creation_data,
            format='multipart'
        )

    def test_admin_can_view_list_of_reservations(self):
        response = self.client.get(self.list_uri)
        expected_reservations = self.reservations.count()
        # import pdb; pdb.set_trace()
        self.assertEqual(response.data['count'], expected_reservations,
                         f'Expected {expected_reservations} reservations, received {response.data["count"]}')
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')

    def test_admin_can_create_reservation_for_self(self):
        data = {
            "traveler": f"{self.user_url}",
            "flight": f"{self.flight_url}"
        }
        response = self.client.post(
            self.list_uri,
            data,
            format='multipart')
        self.assertEqual(response.status_code, 201,
                         f'Expected Response Code 201, received {response.status_code} instead.')

    def test_admin_can_retrieve_reservation_details(self):
        self.create_admin_specific_reservation(
            self.user_url,
            self.flight_url
        )
        response = self.client.get(
            self.detail_uri + str(self.admin.reservation_set.first().id))
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')

    def test_admin_can_update_a_reservation(self):
        self.create_admin_specific_reservation(
            self.user_url,
            self.flight_url
        )
        update_data = {
            "flight": f"{self.flight_url2}",
            "traveler": f"{self.user_url}"
        }
        response = self.client.put(
            self.detail_uri + str(self.admin.reservation_set.first().id),
            update_data,
            format='multipart'
        )
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')

    def test_admin_can_delete_a_reservation(self):
        self.create_admin_specific_reservation(
            self.user_url,
            self.flight_url
        )
        response = self.client.delete(
            self.detail_uri + str(self.admin.reservation_set.first().id))
        self.assertEqual(response.status_code, 204,
                         f'Expected Response Code 204, received {response.status_code} instead.')
