from django.contrib import admin
from .models import Video, Tag

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('num_likes', 'num_views', 'published_at')
    list_display = ('title', 'is_published', 'published_at', 'num_likes', 'num_views')

admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)