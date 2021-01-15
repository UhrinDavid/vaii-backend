from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class HotelRoom(models.Model):
    roomNumber=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)])
    capacity=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField(max_length=10000)

class Guest(models.Model):
    userID=models.ForeignKey(User, on_delete=models.CASCADE)
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    email=models.EmailField()
    mobileNumber=PhoneNumberField()

class Reservation(models.Model):
    userID=models.ForeignKey(User, on_delete=models.CASCADE)
    roomID=models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    dateFrom=models.DateField()
    dateTo=models.DateField()
    note=models.CharField(max_length=255)

class Review(models.Model):
    userID=models.OneToOneField(User, on_delete=models.CASCADE)
    reviewText=models.CharField(max_length=1000)
    stars=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])