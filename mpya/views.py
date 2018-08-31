from .models import Album,Song
from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request,'home.html')

def today(request):
	return render(request,'today.html')

def song(request):
	#album = Album.objects.all()
	songs = Song.objects.all()
	return render(request,'song.html',{'Songs':songs})


def album(request):
	album = Album.objects.all()
	#songs = Song.objects.all()
	return render(request,'album.html',{'Album':album})
