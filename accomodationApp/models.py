from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# Create your models here.
class HotelRoom(models.Model):
    roomNumber=models.PositiveIntegerField(unique=True,validators=[MinValueValidator(1), MaxValueValidator(9999)])
    capacity=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField(max_length=1023)

class Reservation(models.Model):
    userID=models.ForeignKey(User, on_delete=models.CASCADE)
    roomID=models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    dateFrom=models.DateField()
    dateTo=models.DateField()
    note=models.CharField(max_length=255,blank=True)

class Review(models.Model):
    userID=models.OneToOneField(User, on_delete=models.CASCADE)
    reviewText=models.CharField(max_length=1023,blank=True)
    stars=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
