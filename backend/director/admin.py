from django.contrib import admin
from director.models import Director 
from django.utils.html import format_html
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'born', 'dies', 'birthplace', 'height', 'image_tag')
    def image_tag(self,obj):
        try:
            return format_html('<img src="{0}" style="width: 45px; height:68px; object-fit: cover;" />'.format(obj.photo_url.url))
        except:
            return format_html('<strong>Изображения нет</strong>')

admin.site.register(Director, MyModelAdmin)
