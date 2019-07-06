from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings


class BaseSetup(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.base_url = '/api/v1/'
        self.create_uri = self.base_url + 'users/'
        self.list_uri = self.base_url + 'users/all'
        self.detail_uri = self.base_url + 'user/'


class TestAnonUser(BaseSetup):

    def test_can_register(self):
        data = {
            "email": "anon@test.com",
            "first_name": "anon",
            "last_name": "nymous",
            "password": "Idonoth@ve1",
        }
        response = self.client.post(
            self.create_uri,
            data,
            format='json'
        )
        self.assertEqual(response.status_code, 201,
                         f'Expected Response Code 201, received {response.status_code} instead.')

    def test_cannot_access_users_list(self):
        response = self.client.get(
            self.list_uri
        )
        self.assertEqual(response.status_code, 401,
                         f'Expected Response Code 401, received {response.status_code} instead.')


class TestNonAdminUser(BaseSetup):
    def setUp(self):
        super().setUp()
        self.user = self.setup_user()
        self.jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        self.jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        self.payload = self.jwt_payload_handler(self.user)
        self.token = self.jwt_encode_handler(self.payload)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create(
            first_name='nonadmin',
            email='nonadmin@test.com',
            password='random_test_password'
        )

    def tearDown(self):
        super().tearDown()
        self.client.logout()

    def test_can_register(self):
        data = {
            "email": "anon@test.com",
            "first_name": "anon",
            "last_name": "nymous",
            "password": "Idonoth@ve1",
        }
        response = self.client.post(
            self.create_uri,
            data,
            format='json'
        )
        self.assertEqual(response.status_code, 201,
                         f'Expected Response Code 201, received {response.status_code} instead.')

    def test_cannot_access_users_list(self):
        response = self.client.get(
            self.list_uri
        )
        self.assertEqual(response.status_code, 403,
                         f'Expected Response Code 403, received {response.status_code} instead.')


class TestAdminUser(BaseSetup):
    def setUp(self):
        super().setUp()
        self.jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        self.jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        self.admin = self.setup_user()
        self.payload = self.jwt_payload_handler(self.admin)
        self.token = self.jwt_encode_handler(self.payload)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_superuser(
            first_name='admin',
            email='admin@test.com',
            password='random_test_password'
        )

    def tearDown(self):
        super().tearDown()
        self.client.logout()

    def test_can_register(self):
        data = {
            "email": "anon@test.com",
            "first_name": "anon",
            "last_name": "nymous",
            "password": "Idonoth@ve1",
        }
        response = self.client.post(
            self.create_uri,
            data,
            format='json'
        )
        self.assertEqual(response.status_code, 201,
                         f'Expected Response Code 201, received {response.status_code} instead.')

    def test_can_access_users_list(self):
        response = self.client.get(
            self.list_uri
        )
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')
