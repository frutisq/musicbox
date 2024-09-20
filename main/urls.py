from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from . import views
from .views import CustomLoginView


urlpatterns = [
    path('', views.index, name='index'),
    path('категория/<str:category_name>/', views.category_songs, name='category_songs'),
    path('альбом/<int:album_id>/', views.album_songs, name='album_songs'),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),
    path('song/<int:song_id>/edit/', views.edit_song, name='edit_song'),
    path('delete_song/<int:song_id>/', views.delete_song, name='delete_song'),
    path('create', views.create, name='create'),
    path('create_section',views.create_section,name='create_section'),
    path('create_album',views.create_album,name='create_album'),
    path('edit_section/<int:section_id>/', views.edit_section, name='edit_section'),
    path('delete_section/<int:section_id>/', views.delete_section, name='delete_section'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('login/', CustomLoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
