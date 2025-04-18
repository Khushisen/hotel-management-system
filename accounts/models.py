from typing import Iterable
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class Amenities(models.Model):
    name = models.CharField(max_length=1000)
    icon = models.ImageField(upload_to='amenities')
    
    
    def __str__(self):
        return self.name

class HotelUser(User):
    profile_picture = models.ImageField(upload_to='profile')
    phone_number = models.CharField(unique=True, max_length=100)
    email_token = models.CharField(max_length=100,null=True,blank=True)
    otp = models.CharField(max_length=10,null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    
    class Meta:
        db_table = "hotel_user"
    
class HotelVendor(User):
    phone_number = models.CharField(unique=True,max_length=100)
    profile_picture = models.ImageField(upload_to="profile")
    email_token = models.CharField(max_length = 100 ,null = True , blank=True)
    otp = models.CharField(max_length = 10 , null = True , blank = True)
    business_name = models.CharField(max_length=100)
    
    is_verified = models.BooleanField(default = False)
    
    class Meta:
        db_table = "hotel_vendors"
    
class Ameneties(models.Model):
    name=models.CharField(max_length=1000)
    icon=models.ImageField(upload_to="hotels")
    
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_description = models.TextField()
    hotel_slug = models.SlugField(max_length = 1000 , unique  = True)
    hotel_owner = models.ForeignKey(HotelVendor, on_delete = models.CASCADE , related_name = "hotels")
    ameneties = models.ManyToManyField(Ameneties)
    hotel_price = models.FloatField()
    hotel_offer_price = models.FloatField()
    hotel_location = models.TextField()
    is_active = models.BooleanField(default = True)
    
    def save(self,) ->None:
        from .utils import generateSlug
        if not self.pk:
            self.hotel_slug = generateSlug(self.hotel_name)
        return super().save()
    
    
class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="hotel_managers")
    manager_name = models.CharField(max_length=100)
    manager_contact=models.CharField(max_length=100)
    