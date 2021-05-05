from django.test import TestCase
from post_app.models import Noticia
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

# Test em Model
class NewsTestCase(TestCase):

    def setUp(self):

        usuario = User.objects.create(
            username='Teste',
            password='123456'
        )

        Noticia.objects.create(
            codigo=1,
            titulo="Titulo da Noticia",
            header_image="",
            assunto="Assunto da noticia",
            texto="Texto da Noticia",
            timestamp="",
            author=usuario,
        )

    # Testando se a noticia foi realmente cadastrada
    def test_cadastrar_noticia(self):
        noticia = Noticia.objects.get(codigo=1)
        self.assertEquals(noticia.titulo, 'Titulo da Noticia')


# Teste em View
class NewsViewTestCase(TestCase):

    def test_status_200(self):
        response = self.client.get(reverse('Home'))
        self.assertEquals(response.status_code, 200)