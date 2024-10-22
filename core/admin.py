from django.contrib import admin
from .models import Video, Tag

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('num_likes', 'num_views', 'published_at')

admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)