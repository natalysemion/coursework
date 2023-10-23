from django.db import models
from .spotify import SpotifyService
class Event(models.Model):
    name = models.CharField(max_length=100)
    is_complete = models.BooleanField()
    date_time = models.DateTimeField(null=True, blank=True)
    place = models.ForeignKey('Place', null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField()
    #artists = models.ManyToManyField('Artist', related_name='events')  # Змінено related_name на 'events'

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    male = models.CharField(max_length=10)
    birth_date = models.DateField(null=True)
    country = models.ForeignKey('Country', null=True, on_delete=models.SET_NULL)
    photo = models.URLField(null=True, blank=True)
    events = models.ManyToManyField('Event', related_name='artists')  # Змінено related_name на 'artists'
    latest_song_uri = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        spotify_service = SpotifyService()
        self.latest_song_uri = spotify_service.get_latest_song_uri(self.name)
        super().save(*args, **kwargs)

class Song(models.Model):
    name = models.CharField(max_length=100)
    lyrics = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')  # Зв'язок один-до-багатьох між Song і Artist
    spotify_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    photo = models.URLField(null=True, blank=True)  # Посилання на фото місця
    location = models.URLField(null=True, blank=True)  # Посилання на розташування місця
    capacity = models.PositiveIntegerField()
    lat = models.FloatField(null=True, blank=True)  # Широта
    lng = models.FloatField(null=True, blank=True)  # Довгота

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey('Event',  null=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)

    def str(self):
        return f"Order {self.id}"