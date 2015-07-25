from django.shortcuts import render
from django.http import JsonResponse
import memcache


def index(request):
    return render(request, 'spotifyapp/index.html')


def get_tags(request):
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    key = 'tags'
    jake = mc.get(key) or ['taylor', 'swift']
    return JsonResponse(jake, safe=False)
