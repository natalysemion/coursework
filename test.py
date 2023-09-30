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
        return access_token
    else:
        print("Не вдалося отримати токен. Помилка:", response.status_code)
        raise  Exception('Can\'t get acces_token')
def get_top_track(artist_id: str):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=PL'
    data = {
        'grant_type': 'client_credentials',
        'client_id': '915534a01bd142e18fa91f41672775d1',
        'client_secret': '8e715ebcda0e499e8728feae4d34967b',
    }
    headers = {
        #'Authorization': 'Bearer BQClO3maayUkke9f-9TEx1WHlbuoTX1niPBw2wpJDrF5RFRG6Lab1nhQXR75m8EHYdrWlAEy_0BLFAnRhi6xKu4gmXlSZ1GO0ADq_LtTzAhhseRLchQ'
         'Authorization': f'Bearer {get_token()}'

    }
    response = requests.get(url, headers=headers)
   # print(response.content)
    top_track_data = response.json()
    print(top_track_data)
    return top_track_data


def get_artist_id(name: str):
    headers = {
        'Authorization': 'Bearer BQClO3maayUkke9f-9TEx1WHlbuoTX1niPBw2wpJDrF5RFRG6Lab1nhQXR75m8EHYdrWlAEy_0BLFAnRhi6xKu4gmXlSZ1GO0ADq_LtTzAhhseRLchQ'
    }
    url = f'https://api.spotify.com/v1/search?q={name}&type=artist'
    response = requests.get(url, headers=headers)
    print(response.content)


#get_artist_id('Jann')
get_token()
get_top_track('61mjebytLODtxAOS9ULCmb')
# get_token()