from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from main import views, spotify
from .views import NameAutocomplete

urlpatterns = [
    path("", views.home, name="home"),

    path('name_autocomplete/', NameAutocomplete.as_view(), name='name_autocomplete'),
    path('api/events/autocomplete/', views.event_autocomplete, name='event_autocomplete'),


    path('artists/', views.artist_list, name='artist_list'),
    path('artist/<int:artist_id>/', views.artist_details, name='artist_details'),

    path('events/', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_details, name='event_details'),
    path('event/create/', views.create_event, name='create_event'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('event/<int:event_id>/edit/', views.edit_event, name='edit_event'),

    path('places/', views.place_list, name='place_list'),
    path('place/<int:place_id>/', views.place_details, name='place_details'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('auth/', include('social_django.urls', namespace='social')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('song/<int:song_id>/', views.song_detail, name='song_detail'),
    path('get_top_track', spotify.get_top_track, name='get_top_track'),

    #path('artist/<int:artist_id>/script.js', spotify.get_top_track, name='get_top_track')

]