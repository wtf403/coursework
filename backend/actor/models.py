from django.db import models
# Create your models here.

class Actor(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=64)
    surname = models.CharField(verbose_name="Фамилия", max_length=64)
    born = models.DateField(verbose_name="Родился", blank=True) 
    dies = models.DateField(verbose_name="Умер", blank=True) 
    birthplace = models.CharField(verbose_name="Место рождения", max_length=64, blank=True)
    nationality = models.CharField(verbose_name="Нацональность", max_length=64, blank=True)
    photo_url = models.ImageField(verbose_name="Обложка", upload_to="actors/cover", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'
