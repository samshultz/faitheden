from django.conf.urls import url
from django.contrib import admin
from donate.views import Donate


app_name='donate'

urlpatterns = [
    url(r'^$', Donate , name='donate1'),


]