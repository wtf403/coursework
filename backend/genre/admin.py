from django.contrib import admin
from genre.models import Genre
from django.utils.html import format_html
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('title', 'image_tag')
    def image_tag(self,obj):
        try:
            return format_html('<img src="{0}" style="width: 45px; height:115px; object-fit: cover;" />'.format(obj.cover.url))
        except:
            return format_html('<strong>Изображения нет</strong>')

admin.site.register(Genre)
