from django.db import models

# Create your models here.
class Studio(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64)
    formation_year = models.DateField(verbose_name='Год основания', blank=True, null=True)
    cover = models.ImageField(verbose_name='Обложка', upload_to='studios/cover', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студия'
        verbose_name_plural = 'Студии'
