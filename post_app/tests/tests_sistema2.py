from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TesteSistema2(LiveServerTestCase):
    def teste(self):
        selenium = webdriver.Chrome()

        # Url que será visitada
        selenium.get('http://127.0.0.1:8000/accounts/login/')

        # Procura os elementos necessarios para inserir as informações
        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')

        # Localiza o botão de "Entrar"
        submit = selenium.find_element_by_id('entrar')

        # Insere as informações em cada campo.
        username.send_keys('Zeca')
        password.send_keys('war99857133')

        # Clica no botão "Entrar"
        submit.send_keys(Keys.RETURN)

        # Localiza o botão de "Gerenciar"
        submit = selenium.find_element_by_id('btnGerenciar')

        # Clica no botão "Gerenciar"
        submit.send_keys(Keys.RETURN)

        # Localiza o botão de "Adicionar"
        submit = selenium.find_element_by_id('teste_add')

        # Clica no botão "Adicionar"
        submit.send_keys(Keys.RETURN)

        # Procura os elementos necessarios para inserir as informações
        titulo = selenium.find_element_by_id('id_titulo')
        assunto = selenium.find_element_by_id('id_assunto')
        texto = selenium.find_element_by_id('id_texto')

        # Localiza o botão de "Adicionar"
        submit = selenium.find_element_by_id('btn_form')

        # Insere as informações em cada campo.
        titulo.send_keys('Noticia Teste')
        assunto.send_keys('Testando adição de noticias.')
        texto.send_keys('Isso é um teste para ver se funciona a adição de noticia')

        # Clica no botão "Adicionar"
        submit.send_keys(Keys.RETURN)
