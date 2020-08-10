from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from .models import Account
from .serializers import UserSerializer
from rest_auth import views
from rest_framework.permissions import IsAuthenticated, AllowAny


class ProfileView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = UserSerializer


class ProfileDetailView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user