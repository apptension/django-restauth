from rest_framework import generics

from . import serializers


class SignUpView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
