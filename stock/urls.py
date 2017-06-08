from django.conf.urls import url
from django.contrib import admin
from .views import table, search_name

app_name = 'watch'

urlpatterns = [
    # /watch/
    url(r'^$', table, name='index'),
    url(r'^search/$', search_name, name = 'search'),
]
