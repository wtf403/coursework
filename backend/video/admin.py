from django.contrib import admin
from video.models import Video
from embed_video.admin import AdminVideoMixin
from django.utils.html import format_html
# Register your models here.

class MyModelAdmin(AdminVideoMixin,admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['v_type']
    list_display = ('title', 'image')
    filter_horizontal = ('actor', 'director', 'genre', 'studio')

    def image(self,obj):
        try:
            return format_html('<img src="{0}" style="width: 45px; height: 68px; object-fit: cover;" />'.format(obj.image_url))
        except:
            return format_html('<strong>Изображения нет</strong>')

admin.site.register(Video, MyModelAdmin)
