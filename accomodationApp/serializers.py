from rest_framework import serializers
from accomodationApp.models import HotelRoom,Reservation,Review
from django.contrib.auth.models import  User

class HotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields='__all__'

class HotelRoomSerializerNumber(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields=['roomNumber']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields='__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id', 'first_name', 'last_name']

class ReviewSerializerList(serializers.ModelSerializer):
    userID= CustomUserSerializer()
    class Meta:
        model = Review
        fields='__all__'

class ReservationSerializerBooked(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields=['dateFrom', 'dateTo']

class ReservationSerializerList(serializers.ModelSerializer):
    userID= CustomUserSerializer()
    roomID=HotelRoomSerializerNumber()
    class Meta:
        model = Reservation
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields='__all__'
