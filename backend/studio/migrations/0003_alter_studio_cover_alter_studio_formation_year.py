# Generated by Django 4.0.5 on 2022-06-24 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='studios/cover', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='formation_year',
            field=models.DateField(blank=True, null=True, verbose_name='Год основания'),
        ),
    ]
