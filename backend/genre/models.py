from django.db import models

# Create your models here.
class Genre(models.Model):
    title = models.CharField(verbose_name='Название', max_length=64)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    cover = models.ImageField(verbose_name='Обложка', upload_to='genres/cover', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        
    