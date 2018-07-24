from django.conf.urls import url
from . import views
app_name='music'
urlpatterns = [
    # /music/
    # url(r'^$', views.index,name='index'),

    #load db
    #userid=5ae41f0c8071e11420dd0327,email=samwise.mj@gmail.com
    url(r'^userid=(?P<user_id>[0-9A-Za-z]+),email=(?P<email_id>[0-9A-Za-z.@_]+)/$',views.redinit,name="redinit"),
    url(r'^dbloadsong5535/',views.dbloadsong,name="dbloadsong"),
    url(r'^dbloadalbum5535/',views.dbloadalbum,name="dbloadalbum"),
    # url(r'^dbloadalbumart5535/',views.dbloadalbumart,name="dbloadalbum")
    #/music/xxxx
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name="detail"),
#     url for favourite
    url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favourite,name="favourite"),
    # add_category form
    url(r'^add_category/',views.add_category,name='add_category'),
    url(r'^(?P<song_id>[0-9]+)/(?P<album_id>[0-9]+)$', views.plist, name="plist"),
    url(r'^add',views.add,name='add'),
    url(r'^abc2',views.add2,name='add2'),
    url(r'^playlist/(?P<pl_id>[0-9]+)/$', views.delsong, name="delsong"),
    url(r'^playlist/', views.vplist, name="vplist"),
    url(r'^albums/', views.albums, name="albums"),
    url(r'^home/', views.home, name="home"),

]
