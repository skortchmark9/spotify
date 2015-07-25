from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'spotifyapp/index.html')


def get_tags(request):
    jake = ['taylor', 'swift']
    return JsonResponse(jake, safe=False)
