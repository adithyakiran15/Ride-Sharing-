from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Ride
from .serializers import rideserializers, Userserializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

# Create your views here.

class rideviewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Ride.objects.all()
    serializer_class = rideserializers

class CreateuserView(CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = Userserializer

class duerideviewset(viewsets.ModelViewSet):
    queryset = Ride.objects.all().order_by('-created_at').filter(completed=False)
    serializer_class = rideserializers

class completedviewset(viewsets.ModelViewSet):
    queryset = Ride.objects.all().order_by('-created_at').filter(completed=True)
    serializer_class = rideserializers



# I tried to implement but had a little confusion and doughs,
# but I have done some research regarding it and I would like
# to tell you what I have gone thought.
#
#
# **Implement a simulation of real-time ride tracking. This
# could involve periodically updating the ride's current location.**
#
# Real time tracking can be implemented by the creating the
# fields in model and using serializers to convert the data.
# I got doughs when creating a real time communication with
# the customer and the driver it can be channeled through
# WebSocket integration which enables real time communication.
#
#
#
# **Implement an algorithm for matching ride requests with
# available drivers. This could be based on proximity, or other factors.**
#
# This can be done by haversine formula where it calculate the
# distance between two point in the earths surface.
# When the request is made by the customer, it uses the Haversine formula
# to calculate distances between coordinates and selects the nearest driver
# for each ride request.



