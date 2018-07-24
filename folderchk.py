# # from django.test import TestCase
# #
# # # Create your tests here.
import os.path,os
import eyed3


dir="C:\\Users\\Samwise\\Desktop\\Music\\Pink Floyd"
for filename in os.listdir(dir):
    dirin=dir+"\\"+filename
    print(filename)
    for song in os.listdir(dirin):
        if(song.endswith(".mp3")):
            audio=eyed3.load(song)
            print ('\t artist-->{} {}-->title'.format(audio.tag.artist,audio.tag.title))
    print("\n")

# str="21--as.mp3"
# # if (int(str[0]) in range(0,9)):
# #     print(str[0])
# print(str[0:str.find(".mp3")])
