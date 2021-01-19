from django.contrib import admin
from accomodationApp.models import HotelRoom, Reservation, Review

class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'roomNumber', 'price', 'capacity', 'image')
admin.site.register(HotelRoom, HotelRoomAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'roomID', 'userID','dateFrom', 'dateTo','note')
admin.site.register(Reservation, ReservationAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'userID', 'reviewText','stars')
admin.site.register(Review, ReviewAdmin)