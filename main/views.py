from django.shortcuts import get_object_or_404, render, redirect
from .models import Section, Song, Album
from .forms import SectionForm,SongForm,AlbumForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

def index(request):
    sections = Section.objects.all()
    songs = Song.objects.all()
    albums = Album.objects.all()  

    context = {
        'sections': sections,
        'songs': songs,
        'albums': albums,  
        'is_admin': request.user.is_staff,
    }
    return render(request, 'main/index.html', context)

def category_songs(request, category_name):
    category = get_object_or_404(Section, name=category_name)
    albums = Album.objects.filter(section=category)
    songs_without_album = Song.objects.filter(section=category, album__isnull=True)
    data = {'title': f'Альбомы из категории {category_name}','title1':f'Песни из категории {category_name}', 'albums': albums, 'sections': Section.objects.all(),'songs_without_album':songs_without_album,'is_admin': request.user.is_staff,}
    return render(request, 'main/category_albums.html', data)

def album_songs(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = Song.objects.filter(album=album)
    data = {'title': f'Песни из альбома {album.name}', 'album': album, 'songs': songs, 'sections': Section.objects.all()}
    return render(request, 'main/album_songs.html', data)

def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    data = {'title': song.title, 'song': song, 'sections': Section.objects.all()}
    return render(request, 'main/song_detail.html', data)

def create(request):
    sections = Section.objects.all()
    albums = Album.objects.all()
    
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Сохраняем экземпляр песни без коммита, чтобы добавить метаданные
            song = form.save(commit=False)

            # Получаем загруженный аудиофайл
            audio_file = request.FILES.get('audio_file')
            
            if audio_file:
                try:
                    # Открываем аудиофайл через mutagen для извлечения метаданных
                    audio = MP3(audio_file, ID3=EasyID3)

                    # Получаем метаданные и присваиваем их полям модели
                    song.title = audio.get('title', ['Без названия'])[0]
                    song.artist = audio.get('artist', ['Неизвестный исполнитель'])[0]
                    song.year = audio.get('date', [None])[0]

                    # Выводим сообщение, что метаданные сохранены
                    print(f"Метаданные сохранены: Название: {song.title}, Исполнитель: {song.artist}, Год: {song.year}")

                except Exception as e:
                    print(f"Ошибка при извлечении метаданных: {e}")
            
            # Сохраняем песню с обновленными метаданными
            song.save()

            return redirect('index')

    form = SongForm()
    data = {
        'form': form,
        'sections': sections,
        'albums': albums,
    }
    return render(request, 'main/create_song.html', data)

def create_section(request):
    if request.method == 'POST':
        form1 = SectionForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('index')
    else:
        form1 = SectionForm()

    data = {
        'form1': form1,
        'title': 'Создать новую категорию'
    }
    return render(request, 'main/index.html', data)  

def create_album(request):
    if request.method == 'POST':
        form2 = AlbumForm(request.POST,request.FILES)
        if form2.is_valid():
            form2.save()
            return redirect('index')
    else:
        form2 = AlbumForm()
    data = {
        'form2': form2,
        'title':'Созданий нового альбома'
    }        
    return render(request,'main/index.html',data)

def edit_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST,request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'main/edit_album.html', {'form': form})


def delete_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        album.delete()
        return redirect('index')
    return render(request, 'main/delete_album.html', {'album': album})

def edit_section(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SectionForm(instance=section)
    return render(request, 'main/edit_section.html', {'form': form})


def delete_section(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    if request.method == 'POST':
        section.delete()
        return redirect('index')
    return render(request, 'main/delete_section.html', {'section': section})


def edit_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    albums = Album.objects.all()
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_detail', song_id=song.id)
    else:
        form = SongForm(instance=song)
    return render(request, 'main/edit_song.html', {'form': form, 'albums': albums})



def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        song.delete()
        return redirect('index')
    return render(request, 'main/delete_song.html', {'song': song})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, 'Неверный логин или пароль.')
        return super().form_invalid(form)

    