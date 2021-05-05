from django.test import TestCase
from post_app.models import Noticia
from django.contrib.auth.models import User

# Create your tests here.

class NewsTestCase(TestCase): #Teste Unitário Cadastrar Noticia

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
