import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings

class SpotifyService:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=settings.SPOTIPY_CLIENT_ID,
            client_secret=settings.SPOTIPY_CLIENT_SECRET,
            redirect_uri=settings.SPOTIPY_REDIRECT_URI,
            scope="user-library-read"
        ))

    def get_latest_song_uri(self, artist_name):
        results = self.sp.search(q=f'artist:{artist_name}', type='track', limit=1)
        if results and 'tracks' in results and 'items' in results['tracks'] and results['tracks']['items']:
            latest_track = results['tracks']['items'][0]
            return latest_track['uri']
        return None


# from main.views import get_top_track
import requests

def get_token():
    client_id = '915534a01bd142e18fa91f41672775d1'
    client_secret = '8e715ebcda0e499e8728feae4d34967b'
    token_url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['access_token']
        print("Bearer Token:", access_token)
    else:
        print("Не вдалося отримати токен. Помилка:", response.status_code)

def get_top_track(artist_id: str):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=PL'
    data = {
        'grant_type': 'client_credentials',
        'client_id': '915534a01bd142e18fa91f41672775d1',
        'client_secret': '8e715ebcda0e499e8728feae4d34967b',
    }
    headers = {
        'Authorization': 'Bearer BQC5UTs4xFX7Ba9-HKqy5qPLxJrloJ9t_CLw9gxgjOC5vtlbhZI5I6-txSH1kN79fIkZyUHd1DV6Gc02flvK4zuRnSRZ7YFYSFGsI0SFryyuWXf9GjA'
    }
    response = requests.get(url, headers=headers)
    print(response.content)

def get_artist_id(name: str):
    headers = {
        'Authorization': 'Bearer BQClO3maayUkke9f-9TEx1WHlbuoTX1niPBw2wpJDrF5RFRG6Lab1nhQXR75m8EHYdrWlAEy_0BLFAnRhi6xKu4gmXlSZ1GO0ADq_LtTzAhhseRLchQ'
    }
    url = f'https://api.spotify.com/v1/search?q={name}&type=artist'
    response = requests.get(url, headers=headers)
    print(response.content)


#get_artist_id('Jann')
get_top_track('61mjebytLODtxAOS9ULCmb')
# get_token()