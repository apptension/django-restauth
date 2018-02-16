from rest_framework import generics, permissions

from . import serializers


class SignUpView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserSignupSerializer


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = serializers.UserProfileSerializer

    def get_object(self):
        return self.request.user.profile
