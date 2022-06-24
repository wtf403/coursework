from django.db import models
from studio.models import Studio
from genre.models import Genre
from director.models import Director
from actor.models import Actor

# Create your models here.
class Video(models.Model):
    image_url = models.CharField(verbose_name="Ссылка на обложку", max_length=255, blank=True)
    video_url = models.CharField(verbose_name="Ссылка на трейлер", max_length=255, blank=True)
    
    title = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание")

    director = models.ManyToManyField(verbose_name="Режисёры", to=Director, related_name="video")
    actor = models.ManyToManyField(verbose_name="Актёры", to=Actor, related_name="video")
    
    duration = models.TimeField(verbose_name="Продолжительнось")
    release = models.DateField(verbose_name="Дата выхода")
    country = models.CharField(verbose_name="Старна", max_length=64)
    age_restriction	= models.IntegerField(verbose_name="Возрастное ограничение")
    budget = models.IntegerField(verbose_name="Бюджет")
    fees = models.IntegerField(verbose_name="Сборы")
    
    studio = models.ManyToManyField(verbose_name="Стyдия", to=Studio, related_name="video")
    genre = models.ManyToManyField(verbose_name="Жанр", to=Genre, related_name="video")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
