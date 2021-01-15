from django.shortcuts import render
from accomodationApp.models import Guest,HotelRoom,Reservation,Review
from accomodationApp.serializers import GuestSerializer,HotelRoomSerializer,ReservationSerializer,ReviewSerializer
from rest_framework import viewsets

# Create your views here.
class GuestViewSet(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

class HotelRoomViewSet(viewsets.ModelViewSet):
    queryset=HotelRoom.objects.all()
    serializer_class=HotelRoomSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer