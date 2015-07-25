import requests
import json

query_url = "https://api.spotify.com/v1/search?q="

def get_tracks(query_params):
    query_url += '%20'.join(query_params)
    query_url += '&type=track'

    r = requests.get(query_url)
    tracks = json.loads(r.text)['tracks']['items']
    return [(track['name'], track['preview_url']) for track in tracks]
