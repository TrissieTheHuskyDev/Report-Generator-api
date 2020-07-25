from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
from .models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "username", "email", "lucky_number")
