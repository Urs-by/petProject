from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import os
from uuid import uuid4

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class UserCustom(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    pets = models.BooleanField(default=False)
    image = models.ImageField(upload_to='user/', blank=True, null=True)

    def __str__(self):
        return f'{self.user}'


class Pet(models.Model):
    nickname = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    owners = models.ManyToManyField(User, related_name='pet')

    def __str__(self):
        return f' {self.nickname}, {self.breed}, {self.owners}'


class PetPhoto(models.Model):
    pet = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pet_photos')
    image = models.ImageField(upload_to='pets/', null=True, blank=True)
    comment = models.TextField()

    def __str__(self):
        return f'Photo of {self.pet.nickname}'


class Shop(models.Model):
    shop_name = models.CharField(max_length=50)
    legal_name = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    coordinates_lat = models.FloatField(blank=True, null=True)
    coordinates_lng = models.FloatField(blank=True, null=True)
    total_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.shop_name} , {self.total_rating}, {self.coordinates_lat}, {self.coordinates_lng}'


class UserShopRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    users_rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])
    comment = models.TextField(blank=True)
