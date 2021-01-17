from django.shortcuts import render
from accomodationApp.models import HotelRoom,Reservation,Review
from accomodationApp.serializers import HotelRoomSerializer,ReservationSerializer,ReservationSerializerBooked,ReviewSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
import jwt
from backend.settings import SECRET_KEY

# Create your views here.
class HotelRoomViewSet(viewsets.ModelViewSet):
    queryset=HotelRoom.objects.all()
    serializer_class=HotelRoomSerializer
    """def get_permissions(self):
        if self.request.method in ['update', 'partial_update', 'destroy','create']:
            self.permission_classes = [IsAdminUser, ]
        else:
            self.permission_classes = [AllowAny, ]"""

class ReviewViewSet(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    """def get_permissions(self):
        if self.action in ['destroy',]:
            self.permission_classes = [IsAdminUser, ]
        elif self.action in ['create','update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [AllowAny, ]"""

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    """def get_permissions(self):
        if self.request.method in ['destroy','update', 'partial_update', 'list']:
            self.permission_classes = [IsAdminUser, ]
        elif self.request.method in ['create',]:
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [AllowAny, ]"""
            

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_user_reservations(request):
    reservations=Reservation.objects.filter(userID=jwt.decode(request.headers['Authorization'][7:],SECRET_KEY, algorithms=['HS256'])['user_id'])
    serializer=ReservationSerializer(reservations,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_reservation_dates(request,room):
    reservations=Reservation.objects.filter(roomID=room)
    serializer=ReservationSerializerBooked(reservations,many=True)
    return Response(serializer.data)
