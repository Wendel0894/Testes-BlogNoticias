from django.db import models
from django.urls import reverse

# Create your models here.

class Noticia (models.Model):
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    header_image = models.ImageField(null=True, blank=True, upload_to='imagens/')
    assunto = models.CharField(max_length=100)
    texto = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail_notice', args=[str(self.codigo)])

    def __str__(self):
        return str(self.codigo)

class Comentario (models.Model):
    codigo = models.AutoField(primary_key=True)
    opiniao = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    cod_noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comments')
    cod_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('visualizar_noticia', args=[str(self.cod_noticia)])

    def __str__(self):
        return f'{self.codigo}: {self.opiniao}'


