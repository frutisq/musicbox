from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Album(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='album_images',blank=True)
    artist = models.CharField(max_length=20)
    section = models.ForeignKey(Section, related_name='albums', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

class Song(models.Model):
    section = models.ForeignKey(Section, related_name='songs', on_delete=models.CASCADE,blank=True)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    producers = models.TextField(blank=True)
    title = models.CharField(max_length=200,blank=True)
    artist = models.CharField(max_length=200,blank=True)
    lyrics = models.TextField(blank=True)
    translate_lyrics = models.TextField(blank=True)
    comment = models.CharField(max_length=200,blank=True)
    year = models.IntegerField(blank=True,null=True)
    audio_file = models.FileField(upload_to='audio/',blank=True,null=True)
    audio_file_1 = models.FileField(upload_to='audio/',blank=True,null=True)
    video_file = models.FileField(upload_to='video/',blank=True,null=True)
    video_file_1 = models.FileField(upload_to='video/',blank=True,null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        