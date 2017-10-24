from django.conf.urls import url
from django.contrib import admin
from .views import contact


app_name='contact'
urlpatterns = [
    url(r'^$', contact, name='contact1'),


]
