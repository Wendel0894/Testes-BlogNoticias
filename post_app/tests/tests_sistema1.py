from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TesteSistema1(LiveServerTestCase):
    def teste_sistema(self):
        selenium = webdriver.Chrome()
        # Url que será visitada
        selenium.get('http://127.0.0.1:8000/accounts/Cadastrar/')

        # Procura os elementos necessarios para inserir as informações
        username = selenium.find_element_by_id('id_username')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')

        # Localiza o botão de "Cadastrar"
        submit = selenium.find_element_by_id('cadastrar')

        # Insere as informações em cada campo.
        username.send_keys('Jaco')
        password1.send_keys('war99857133')
        password2.send_keys('war99857133')

        # Clica no botão "Cadastrar"
        submit.send_keys(Keys.RETURN)
