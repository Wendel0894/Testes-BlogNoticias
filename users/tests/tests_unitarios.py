from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.


class UnitTestsUser(TestCase):

    def setUp(self):

        User.objects.create(
            username='Teste',
            password='123456'
        )

    # Testanto se Usuario foi realmente cadastrado
    def test_cadastro_user(self):
        user = User.objects.get(username='Teste')
        self.assertEquals(user.username, 'Teste')

    # Testando tamanho minimo para a senha
    def test_password(self):
        t_password = User.objects.get(password='123456')
        self.assertTrue(len(t_password.password) > 5)

