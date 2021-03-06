from operator import ne
from user import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'
urlpatterns = [
  path('', view=views.mainSearch, name="main"),
  path('mypage/', view=views.myPage, name="myPage"),

  path('myInfo/', view=views.myInfo, name="myInfo"),
  path('updateInfo/', view=views.updateInfo, name="updateInfo"),
  path('myInfo/register/', view=views.myInfoRegister, name="myInfoRegister"),
  path('register/', views.certificationRegister, name='certificationRegister'),
  path('mypage/<int:pk>/', views.certDetail, name='certDetail'),
  path('mypage/<int:pk>/update/', views.certUpdate, name='certUpdate'),
  path('mypage/<int:pk>/delete/', views.certDelete, name='certDelete'),
  path('register/addMusicAjax/', views.addMusicAjax, name='addMusicAjax'),

  path('search/',views.searchResult, name='search'),
  path('search/addMusicAjax/', views.addMusicAjax, name='addMusicAjax'),
  path('search/myFeed',views.searchMyFeed, name='searchMyFeed'),
  path('search/likedFeed',views.searchLikedFeed, name='searchLikedFeed'),
  path('deleteFeed/<int:pk>',views.deleteFeed, name="deleteFeed"),
  path('updateFeed/<int:pk>', views.updateFeed, name="updateFeed"),
  path('updateFeed/addMusicAjax/', views.addMusicAjax, name='addMusicAjax'),
  path('feed/<int:pk>/', views.feedDetail, name="feedDetail"),
  path('search/<int:pk>/like/', views.feedLike, name='feedLike'),
  path('list/',views.feedList, name='feedList'),
  path('list/addMusicAjax/', views.addMusicAjax, name='addMusicAjax'),
  
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)