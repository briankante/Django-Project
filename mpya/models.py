from django.db import models

class Album(models.Model):
	artist = models.CharField(max_length=120)
	album_title = models.CharField(max_length=120)
	genre = models.CharField(max_length=120)
	album_logo=models.CharField(max_length=120)

	def __str__(self):
		return self.artist

class Song(models.Model):
	artist=models.CharField(max_length=120)
	song_title=models.CharField(max_length=120)
	file_type=models.CharField(max_length=120)
	def __str__(self):
		return self.song_title		


# Create your models here.
