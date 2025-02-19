from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True)
    video = models.FileField(upload_to='videos/', verbose_name='Vídeo', null=True)
    slug = models.SlugField(max_length=100, unique=True)
    published_at = models.DateTimeField(verbose_name='Publicado em', editable=False, null=True)
    is_published = models.BooleanField(default=False, verbose_name='Publicado')
    num_likes = models.IntegerField(default=0, verbose_name='Likes', editable=False)
    num_views = models.IntegerField(default=0, verbose_name='Visualizações', editable=False)
    tags = models.ManyToManyField('Tag', verbose_name='Tags')
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='Autor', editable=False)

    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'

    def __str__(self):
        return self.title
    
    def clean(self):
        if self.is_published and not self.thumbnail and not self.video:
            raise ValidationError('O campo "miniatura" e "vídeo" são obrigatórios para vídeos publicados.')
    
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        return super().save(*args, **kwargs)
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nome')

    def __str__(self):
        return self.name