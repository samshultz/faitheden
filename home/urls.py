from django.conf.urls import url
from django.contrib import admin
from .views import Post_List, Post_Detail


app_name='myblog'
urlpatterns = [
    url(r'^$', Post_List, name='list'),
    url(r'^(?P<id>\d+)/$', Post_Detail, name='detail'),

]
