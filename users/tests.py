from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.


class UnitTestsUser(TestCase):

    def setUp(self):

        User.objects.create(
            username='Teste',
            password='123456'
        )

    def test_cadastro_user(self):
        user = User.objects.get(username='Teste')
        self.assertEquals(user.username, 'Teste')



