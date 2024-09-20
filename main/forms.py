from .models import Section, Album, Song
from django.forms import Select,ModelForm,TextInput,ImageField,FileField,CharField,URLInput,Textarea,ClearableFileInput



class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['name']
        
        widgets = {
            "name": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Имя категории"
            }),
        }

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['section','album','image','title', 'artist', 'lyrics', 'translate_lyrics', 'audio_file','audio_file_1', 'video_file','video_file_1','comment','year']

        widgets = {
            'section':Select(attrs={'class':'form-select'}),
            'album':Select(attrs={'class':'form-select'}),
            'image':ClearableFileInput(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            'artist': TextInput(attrs={'class': 'form-control'}),
            'year':TextInput(attrs={'class': 'form-control'}),
            'comment':Textarea(attrs={'class': 'form-control'}),
            'lyrics': Textarea(attrs={'class': 'form-control'}),
            'translate_lyrics': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "перевод"
            }),
            'audio_file':ClearableFileInput(attrs={'class': 'form-control'}),
            'audio_file_1':ClearableFileInput(attrs={'class': 'form-control'}),
            'video_file':ClearableFileInput(attrs={'class': 'form-control'}),
            'video_file_1':ClearableFileInput(attrs={'class': 'form-control'}),
        }

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['name','image','section','artist']

        widgets = {
            'name': TextInput(attrs={ 'class': "form-control",'placeholder': "Имя категории"}),
            'artist':TextInput(attrs={'class': "form-control"}),
            'image':ClearableFileInput(attrs={'class': 'form-control'}),
            'section':Select(attrs={'class':'form-select'}),
            
        }