from django.conf.urls import url
from django.contrib import admin
from about.views import About


app_name='about'

urlpatterns = [
    url(r'^$', About , name='about1'),


]