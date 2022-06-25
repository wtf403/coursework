# Generated by Django 4.0.5 on 2022-06-24 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0003_remove_director_nationality_director_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='birthplace',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Место рождения'),
        ),
        migrations.AlterField(
            model_name='director',
            name='born',
            field=models.DateField(blank=True, null=True, verbose_name='Родился'),
        ),
        migrations.AlterField(
            model_name='director',
            name='dies',
            field=models.DateField(blank=True, null=True, verbose_name='Умер'),
        ),
        migrations.AlterField(
            model_name='director',
            name='height',
            field=models.IntegerField(blank=True, null=True, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='director',
            name='photo_url',
            field=models.ImageField(blank=True, null=True, upload_to='dierctors/cover', verbose_name='Обложка'),
        ),
    ]