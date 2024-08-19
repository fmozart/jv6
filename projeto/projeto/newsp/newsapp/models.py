from django.db import models
from shortuuid.django_fields import ShortUUIDField 
from django.utils.html import mark_safe

# Create your models here.
class Noticia_p(models.Model):
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='noticias/')
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Titulo(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    data_publicacao = models.DateTimeField(auto_now_add=True)

class Paragrafo(models.Model):
    text = models.TextField()
    text2 = models.TextField()

class Imagem(models.Model):
    img = models.ImageField(upload_to='noticias/')
    
    
    def categoria_imagem(self):
        return mark_safe(
            '<img src="%s" width="50" height="50" />'

            % (self.image.url)
        )