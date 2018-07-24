from django.db import models


class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title +" - "+self.artist

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)

    def __str__(self):
        return self.song_title

class Playlist(models.Model):
    userid=models.CharField(max_length=100)
    useremail=models.CharField(max_length=100)
    song=models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.song.song_title

