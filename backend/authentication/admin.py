from django.contrib import admin
from authentication.models import User
from django.utils.html import format_html
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'image_tag']
    def image_tag(self,obj):
        try:
            return format_html('<img src="{0}" style="width: 45px; height:68px; object-fit: cover;" />'.format(obj.photo.url))
        except:
            return format_html('<strong>Изображения нет</strong>')

admin.site.register(User, MyModelAdmin)
