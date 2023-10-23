from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Artist, Event, Place, Song
from .forms import EventForm
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .spotify import get_top_track

from django.shortcuts import render, redirect
import requests
from .forms import OrderForm


def index(response, id):
    ls = Artist.objects.get(id=id)
    item = ls.events.get(id=1)
    return render(response, "myapp/artist_detail.html", {"artist":ls})
  #  return HttpResponse("<h1>%s</h1>" %(ls.name, str(item.name)))

def home(response):
    return render(response, "myapp/home.html", {})

def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'song_details.html', {'song': song})

def artist_list(request):
    artists = Artist.objects.all()
    data_for_chart1 = []
    data_for_chart2 = []
    for artist in artists:
        songs_count = Song.objects.filter(artist=artist).count()
        data_for_chart1.append({'artist_name': artist.name, 'songs_count': songs_count})
        events_count = artist.events.count()
        data_for_chart2.append({'artist_name': artist.name, 'events_count': events_count})

    context = {'artists': artists, 'data_for_chart1': data_for_chart1, 'data_for_chart2': data_for_chart2}
    return render(request, 'artists.html', context)

def artist_details(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    # Отримайте список подій для поточного артиста
    events = artist.events.all()
    top_track_data = get_top_track(artist.name)
    context = {
        'artist': artist,
        'events': events,
        'top_track_data': top_track_data,
    }
    return render(request, 'artist_details.html', context)

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})


def event_details(request, event_id):
    # Отримуємо об'єкт події або видаємо 404 помилку, якщо подія не існує
    event = get_object_or_404(Event, pk=event_id)

    return render(request, 'event_details.html', {'event': event})


def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        event.delete()
        return redirect('event_list')  # Перенаправте на список подій або на іншу сторінку

    return render(request, 'delete_event.html', {'event': event})
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Перенаправте на список подій або на іншу сторінку
    else:
        form = EventForm()

    return render(request, 'create_event.html', {'form': form})


def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Перенаправте на список подій або на іншу сторінку
    else:
        form = EventForm(instance=event)

    return render(request, 'edit_event.html', {'form': form, 'event': event})
def place_list(request):
    places = Place.objects.all()
    return render(request, 'places.html', {'places': places})
def place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    return render(request, 'place_details.html', {'place': place})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Перенаправте на домашню сторінку або іншу сторінку
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})