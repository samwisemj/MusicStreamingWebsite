from django.test import TestCase
#
# # Create your tests here.

import os.path,os
from .models import Album,Song
a=Album()
s=Song()
dir="C:\\Users\\Samwise\\Desktop\\Music\\Pink Floyd"
for filename in os.listdir(dir):
    dirin=dir+"\\"+filename
    a.album_title=filename;
    a.artist='Pink Floyd'
    a.genre='Progressive Rock'
    for song in os.listdir(dirin):
        if(song.endswith(".mp3")):
            s.album=filename
            s.file_type="mp3"
            s.song_title=song[0:song.find(".mp3")]
        if(song.endswith(".jpg") or song.endswith(".jpeg") or song.endswith(".png")):
            a.album_logo=song
    s.save()
a.save()