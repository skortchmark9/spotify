from django.shortcuts import render
from django.http import JsonResponse
import memcache
import requests
import json

def index(request):
    return render(request, 'spotifyapp/index.html')


def get_tags(request):
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    key = 'tags'
    tags = mc.get(key) or ['hats']
    songs = get_songs_by_lyrics(tags)
    if songs:
        songs = [{'title': song['title'], 'artist': song['artist'], 'context':song['context']} for song in songs]

    jake = {'songs': songs, 'tags': tags}
    return JsonResponse(jake, safe=False)


def get_songs_by_lyrics(tags):
    url = 'http://api.lyricsnmusic.com/songs?api_key=efee5f39bd2b6902960d1a8d44542f'
    url += '&lyrics='
    url += '%20'.join(tags)
    response = requests.get(url)
    if not response:
        response = []
    return json.loads(response.text)
