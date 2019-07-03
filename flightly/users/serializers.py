from rest_framework import serializers
from django.contrib.auth import password_validation


from django.contrib.auth import get_user_model
FlightlyUser = get_user_model()


class FlightlyUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FlightlyUser
        fields = (
            'url',
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'last_login',
            'photograph'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        read_only_fields = ('last_login',)

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value
