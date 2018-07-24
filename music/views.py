from django.http import HttpResponse,Http404
from django.template import RequestContext
from django.shortcuts import render,get_object_or_404,render_to_response
import os.path, os
import requests
from .models import Album, Song, Playlist



def redinit(request, user_id, email_id):
    print(user_id)
    print(email_id)
    # print(222+222)
    request.session['user_id'] = user_id
    request.session['email_id']=email_id

    # return render(request, 'music/index.html', {'all_albums':Album.objects.all()})
    return render(request, 'music/home.html')
    # return render(request,'music/',{})

def home(request):
    return render(request, 'music/home.html')

def index(request):
    all_albums=Album.objects.all()
    # template=loader.get_template('music/index.html')
    context = {
        'all_albums':all_albums,
    }
    return render(request,'music/index.html',context)

def albums(request):
    return render(request, 'music/index.html', {'all_albums': Album.objects.all()})

def detail(request, album_id):
    # try:
    #     album=Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("No album")
    album=get_object_or_404(Album,pk=album_id)
    x=request.session.get('email_id')
    # return HttpResponse(str(x))
    print(x)
    return render(request,'music/songlist.html',{"album":album,})

def plist(request, song_id, album_id):
    # print(song_id)
    # print(request.session.get('email_id'))
    # print(request.session.get('user_id'))

    # entry=Playlist.objects.get(Song.id=song_id)
    # print(entry)
    msg="Already exists"
    f=0
    pl=Playlist()
    song=get_object_or_404(Song, pk=song_id)
    print(song)
    allplist = Playlist.objects.all()
    cuser=request.session.get('user_id')
    for i in allplist:
        if((i.song.song_title == song.song_title) and (i.userid==cuser)):
            f=1
    if(f==0):
        pl.song=song
        pl.useremail=request.session.get('email_id')
        pl.userid=request.session.get('user_id')
        pl.save()
        msg="Added to Playlist"
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/songlist.html', {"album": album,"msg":msg })

def delsong(request,pl_id):
    pl=Playlist.objects.get(pk=pl_id)
    print(pl)
    pl.delete()
    userid = request.session.get('user_id')
    pl = Playlist.objects.all()
    return render(request, 'music/plist.html', {"all_pl": pl, "cuser": userid, "msg":'true'})

def vplist(request):
    userid=request.session.get('user_id')
    pl=Playlist.objects.all()
    return render(request, 'music/plist.html',{"all_pl":pl, "cuser":userid,})

def favourite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request,'music/songlist.html',{
            "album":album,
            "error_msg":"Valid song is not selected",
        })
    else:
        selected_song.is_favourite=True
        selected_song.save()
        return render(request, 'music/songlist.html', {"album": album, })

def add_category(request):
    context=RequestContext(request)
    if request.method=='POST':
        form=CategoryForm(request.POST)
        #         CHECKING FORM VALIDITY
        if form.is_valid():
            #save new category to the dbase
            form.save(commit=True)
            return index(request)
        else:
            print (form.errors)
    else:
        form=CategoryForm()
        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).
        return render(request,'music/add_category.html',{'form': form})

def add(request):
    context={}
    if request.method=="POST":
        num1=int(request.POST.get("num1"))
        num2=int(request.POST.get("num2"))
        context["result"]=num1+num2


    return render(request, "music/abc.html", context=context)

def add2(request):
    context=RequestContext(request)

    if request.method=='POST':
        form=User(request.POST)
        if form.is_valid():
            form.save(commit=True)
            saved=True
            return render(request, "music/abc2.html", {"form": form,"saved":saved})
        else:
            print(form.errors)
    else:
        form=User()
    return render(request,"music/abc2.html",{"form":form})











def dbloadalbum(request):
    dir = "C:\\Users\\Samwise\\Desktop\\Music\\Pink Floyd"
    all = Album.objects.all()
    flag = 0
    for filename in os.listdir(dir):
        for albums in all:
            if albums.album_title==filename:
                flag=1;
        if flag==0:

            a=Album()
            a.artist="Pink Floyd"
            a.album_title=filename
            a.genre='Progressive Rock'
            a.album_logo="http://localhost/Pink Floyd/"+filename+"/"+"Front.jpg"
            a.save()
        flag=0
        a=Album()
        a.artist="Pink Floyd"
        a.album_title=filename
        a.genre='Progressive Rock'
        a.album_logo="http://10.11.48.51:8080/Pink Floyd/"+filename+"/"+"Front.jpg"
        a.save()


    return HttpResponse("<h2>Done!!!!!Check Db</h2>")


def dbloadsong(request):
    dir = "C:\\Users\\Samwise\\Desktop\\Music\\Pink Floyd"
    # for filename in os.listdir(dir):
    #     a = Album.objects.get(album_title__contains=filename)
    #     dirin = dir + "\\" + filename
    #     for song in os.listdir(dirin):
    #
    #         if (song.endswith(".mp3")):
    #             s = Song()
    #
    #             s.album=a
    #             s.file_type = "mp3"
    #             s.song_title = song[0:song.find(".mp3")]
    #             s.save()
    # return HttpResponse("<h2>Done!!!!!Check Db</h2>")
    for filename in os.listdir(dir):
        dirin = dir + "\\" + filename
        a = Album.objects.get(album_title__contains=filename)
        all = Song.objects.all()

        for song in os.listdir(dirin):
            for songs in all:
                if songs.song_title == song[0:song.find(".mp3")]:
                    if songs.album == a:
                        flag = 1
            if (flag == 0):
                if (song.endswith(".mp3")):
                    s = Song()

                    s.album = a
                    s.file_type = "mp3"
                    s.song_title = song[0:song.find(".mp3")]
                    s.save()
            flag = 0
    return HttpResponse("<h2>Done!!!!!Check Db</h2>")


