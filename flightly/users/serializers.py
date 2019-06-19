from rest_framework import serializers

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
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        read_only_fields = ('last_login',)

    def create(self, validated_data):
        user = FlightlyUser.objects.create_user(
            **validated_data,
            )
        return user
