from django.conf.urls import patterns, url
from spotifyapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api', views.get_tags)
)
