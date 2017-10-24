from django.conf.urls import url
from django.contrib import admin
from .views import mar


app_name='quote'
urlpatterns = [
   url(r'^$', mar, name='quotes'), 

]