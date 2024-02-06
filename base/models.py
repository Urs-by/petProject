from django.db import models


# Create your models here.

class User(models.Model):
    # username = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    pets = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'{self.login}'


class Pet(models.Model):
    nickname = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    owners = models.ManyToManyField(User, related_name='pet')

    def __str__(self):
        return f' {self.nickname}, {self.breed}, {self.owners}'


class Shop(models.Model):
    shop_name = models.CharField(max_length=50)
    legal_name = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    coordinates_lat = models.FloatField(blank=True, null=True)
    coordinates_lng = models.FloatField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.shop_name} , {self.rating}, {self.coordinates_lat}, {self.coordinates_lng}'
