from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birth =  models.DateField(blank=True, null=True)
    is_seller = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    referral_code = models.CharField(max_length=10, unique=True, blank=True, null=True)
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.username
    
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True,null=True)
    genres = models.ManyToManyField(Genre)
    followers = models.IntegerField(default=0)

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='events')
    artists = models.ManyToManyField(Artist, related_name='events')

    def __str__(self):
        return f"{self.event_name} - {self.date}"