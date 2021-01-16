from rest_framework import serializers
from accomodationApp.models import Guest,HotelRoom,Reservation,Review

class HotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields='__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields='__all__'

class ReservationSerializerBooked(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields=['roomID','dateFrom', 'dateTo']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields='__all__'