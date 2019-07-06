from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings


class SetupWithNoUser(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.base_url = '/api/v1/'


class SetupWithNonAdminUser(SetupWithNoUser):
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


class SetupWithAdminUser(SetupWithNoUser):
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
