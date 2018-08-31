


from django.urls import path
from . import views

urlpatterns = [
    path('',        views.home,    name='home'),
    path('today/',  views.today,   name='today'),
    path('song/',  views.song,   name='song'),
    path('album/',  views.album,   name='album')
]