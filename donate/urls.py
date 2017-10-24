from django.conf.urls import url
from django.contrib import admin
from .views import donate


app_name='donate'
urlpatterns = [
    url(r'^$', donate, name='donate1'),

]

