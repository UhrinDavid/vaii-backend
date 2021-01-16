from django.shortcuts import render
from accomodationApp.models import HotelRoom,Reservation,Review
from accomodationApp.serializers import HotelRoomSerializer,ReservationSerializer,ReservationSerializerBooked,ReviewSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class HotelRoomViewSet(viewsets.ModelViewSet):
    queryset=HotelRoom.objects.all()
    serializer_class=HotelRoomSerializer
    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer

@api_view(['GET'])
def get_user_reservations(request, user):
    reservations=Reservation.objects.filter(userID=user)
    serializer=ReservationSerializer(reservations,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_reservation_dates(request,room):
    reservations=Reservation.objects.filter(roomID=room)
    serializer=ReservationSerializerBooked(reservations,many=True)
    return Response(serializer.data)