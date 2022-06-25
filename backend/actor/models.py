from django.db import models
# Create your models here.

class Actor(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=64)
    born = models.DateField(verbose_name='Родился', blank=True,  null=True) 
    dies = models.DateField(verbose_name='Умер', blank=True, null=True) 
    birthplace = models.CharField(verbose_name='Место рождения', max_length=64, blank=True, null=True)
    height = models.IntegerField(verbose_name='Рост', null=True, blank=True)
    photo_url = models.ImageField(verbose_name='Обложка', upload_to='actors/cover', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'
