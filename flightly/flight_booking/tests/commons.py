from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings

class SetupWithNoUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

class SetupWithNonAdminUser(SetupWithNoUser):
    def setUp(self):
        self.user = self.setup_user()
        self.jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        self.jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        self.payload = self.jwt_payload_handler(self.user)
        self.token = self.jwt_encode_handler(self.payload)
        super(SetupWithNonAdminUser).setUp()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create(
            first_name='nonadmin',
            email='nonadmin@test.com',
            password='random_test_password'
        )

class SetupWithAdminUser(SetupWithNoUser):
    def setUp(self):
        self.jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        self.jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        self.user = self.setup_user()
        self.payload = self.jwt_payload_handler(self.user)
        self.token = self.jwt_encode_handler(self.payload)
        super(SetupWithAdminUser).setUp()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_superuser(
            first_name='nonadmin',
            email='nonadmin@test.com',
            password='random_test_password'
        )
