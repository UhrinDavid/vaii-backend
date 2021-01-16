from django.shortcuts import render
from accomodationApp.models import ,HotelRoom,Reservation,Review
from accomodationApp.serializers import HotelRoomSerializer,ReservationSerializer,ReviewSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
def get_user_reservations(request):
    reservations=Reservation.objects.filer(userID=request.data['userID'])
    serializer=ReservationSerializer(reservations,many=True)
    return Response(serializer.data)