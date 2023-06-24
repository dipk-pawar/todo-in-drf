from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializers import AccountSerializer
from .models import User


# Create your views here.
class UserCreateAPI(generics.CreateAPIView):
    serializer_class = AccountSerializer
