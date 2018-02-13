from django.contrib import auth as dj_auth
from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework import validators


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[validators.UniqueValidator(queryset=dj_auth.get_user_model().objects.all())],
    )

    class Meta:
        model = dj_auth.get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    def validate_password(self, password):
        password_validation.validate_password(password)
        return password

    def create(self, validated_data):
        user = dj_auth.get_user_model().objects.create_user(
            validated_data['email'],
            validated_data['password'],
        )
        # Schedule an email for account activation here
        # from . import tokens
        # activation_token = tokens.account_activation_token.make_token(user)
        # print(activation_token)
        return user
