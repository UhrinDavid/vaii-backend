from django.shortcuts import render
from accomodationApp.models import HotelRoom,Reservation,Review
from accomodationApp.serializers import HotelRoomSerializer,ReservationSerializer,ReservationSerializerBooked,ReviewSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

# Create your views here.
class HotelRoomViewSet(viewsets.ModelViewSet):
    queryset=HotelRoom.objects.all()
    serializer_class=HotelRoomSerializer
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy','create']:
            # which is permissions.IsAdminUser 
            return request.user and request.user.is_staff       
        else :
            # which is permissions.AllowAny
            return True


class ReviewViewSet(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    def get_permissions(self):
        if self.action in [ 'destroy']:
            # which is permissions.IsAdminUser 
            return request.user and request.user.is_staff
        elif self.action in ['create','update', 'partial_update']:
            # which is permissions.IsAuthenticated
            return request.user and is_authenticated(request.user)             
        else :
            # which is permissions.AllowAny
            return True

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    if self.action in [ 'destroy','update', 'partial_update', 'list']:
            # which is permissions.IsAdminUser 
            return request.user and request.user.is_staff
        elif self.action in ['create']:
            # which is permissions.IsAuthenticated
            return request.user and is_authenticated(request.user)             
        else :
            # which is permissions.AllowAny
            return True

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_user_reservations(request, user):
    reservations=Reservation.objects.filter(userID=user)
    serializer=ReservationSerializer(reservations,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_reservation_dates(request,room):
    reservations=Reservation.objects.filter(roomID=room)
    serializer=ReservationSerializerBooked(reservations,many=True)
    return Response(serializer.data)