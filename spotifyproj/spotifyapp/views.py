from django.shortcuts import render

def index(request):
    return render(request, 'spotifyapp/index.html')