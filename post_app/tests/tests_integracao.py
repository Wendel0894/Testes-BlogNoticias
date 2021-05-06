from django.test import TestCase
from post_app.models import Noticia, Comentario
from django.contrib.auth.models import User

class IntegrationTests(TestCase):

    def setUp(self):

        User.objects.create(
            username='Wendel',
            password='123456'
        )
        Noticia.objects.create(
            codigo=1,
            titulo="Titulo da Noticia",
            header_image="",
            assunto="Assunto da Noticia",
            texto="Texto da Noticia",
            timestamp="",
            author=User.objects.get(username='Wendel'),
        )
        Comentario.objects.create(
            codigo=1,
            opiniao="Teste Comentário",
            timestamp="",
            cod_noticia=Noticia.objects.get(codigo=1),
            cod_usuario=User.objects.get(username='Wendel')
        )

    #testando se os models Comentario e Noticia estão se relacionando corretamente.

    def test_comentarios_noticia(self):
        noticia = Noticia.objects.get(codigo=1)
        comentario = Comentario.objects.get(codigo=1)

        #verificando se os models estão se relacionando corretamente
        self.assertEquals(comentario.cod_noticia.codigo, noticia.codigo)
        self.assertEquals(comentario.cod_noticia.titulo, noticia.titulo)
        self.assertEquals(comentario.cod_noticia.assunto, noticia.assunto)
        self.assertEquals(comentario.cod_noticia.texto, noticia.texto)
        self.assertEquals(comentario.cod_noticia.timestamp, noticia.timestamp)
        self.assertEquals(comentario.cod_noticia.author, noticia.author)

    #testando se a quantidade de comentários de uma noticia está correta.

    def test_quantidade_comentarios_noticia(self):
        #Criando a noticia
        noticia = Noticia.objects.get(codigo=1)

        #Adicionando comentário a noticia
        comentario = Comentario.objects.get(codigo=1)

        #verificando se a quantidade de comentarios da noticia é igual a 1
        self.assertEquals(noticia.comments.all().count(), 1)

    #testando se o nome do author de uma noticia está correto.

    def test_nome_author_noticia(self):
        noticia = Noticia.objects.get(codigo=1)
        usuario = User.objects.get(username='Wendel')
        self.assertEquals(noticia.author.username, usuario.username)















