# Generated by Django 4.0.5 on 2022-06-25 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_type', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videotype',
            options={'verbose_name': 'Тип видео', 'verbose_name_plural': 'Типы видеo'},
        ),
    ]