from django.contrib import admin
from .models import Artist, Event, Song, Place, Country, Order
# Register your models here.

admin.site.register(Artist)
admin.site.register(Event)
admin.site.register(Song)
admin.site.register(Place)
admin.site.register(Country)
admin.site.register(Order)