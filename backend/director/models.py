from django.db import models
# Create your models here.

class Director(models.Model): 
    name = models.CharField(verbose_name='Имя', max_length=64)
    born = models.DateField(verbose_name='Родился', blank=True, null=True,) 
    dies = models.DateField(verbose_name='Умер', blank=True, null=True,) 
    birthplace = models.CharField(verbose_name='Место рождения', max_length=64, null=True, blank=True)
    height = models.IntegerField(verbose_name='Рост', null=True, blank=True)
    photo_url = models.ImageField(verbose_name='Обложка', upload_to='dierctors/cover', blank=True, null=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиcёр'
        verbose_name_plural = 'Режиcёры'
