from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'spotifyapp/index.html')


def get_tags(request):
    jake = ['hats', 'cats', 'bats', 'rats']
    return JsonResponse(jake, safe=False)
