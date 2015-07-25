from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^spotifyapp/', include('spotifyapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]