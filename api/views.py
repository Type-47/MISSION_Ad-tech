from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from user_management.models import User_Info
from .serializers import User_InfoSerializer


class User_InfoAPIView(generics.ListAPIView):
    queryset = User_Info.objects.all()
    serializer_class = User_InfoSerializer
