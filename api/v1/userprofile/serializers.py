from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate
from rest_auth.serializers import UserDetailsSerializer
from .models import Account

# Get the UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        # fields = ("id", "first_name","last_name", "profile_picture", "username","employee_number", "email","date_joined","last_login","lucky_number")
        fields ='__all__'
