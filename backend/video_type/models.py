from django.db import models

# Create your models here.
class VideoType(models.Model):
    video_type = models.CharField(verbose_name='Тип видео', max_length=64)
   
    def __str__(self):
        return self.video_type

    class Meta:
        verbose_name = 'Тип видео'
        verbose_name_plural = 'Типы видеo'
