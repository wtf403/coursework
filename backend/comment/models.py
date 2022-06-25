from dataclasses import dataclass
from django.db import models
from authentication.models import User
from video.models import Video

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comment')
    description = models.TextField(verbose_name='Текст')
    data = models.DateTimeField(verbose_name='Дата')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комменатрии'
