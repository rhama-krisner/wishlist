from rest_framework.test import APITestCase
from lista.models import ListaModel
from django.urls import reverse
from rest_framework import status

class ListaTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Produtos-list')
        self.produto1 = ListaModel.objects.create(
            produto = 'Produto Teste 1',
            descricao = 'Produto sendo testado',
            link = 'https://qitech.com.br/',
            adquirido = 'Sim'
        )
    
    def test_get(self):
        """Teste de verificação do GET"""

        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_post(self):
        """Teste de verificação do POST"""

        data = {
            'produto':'Produto2',
            'descricao':'Produto Criado',
            'link':'https://qitech.com.br/',
            'adquirido':'Não'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        """Teste de verificação do DELETE"""

        response = self.client.delete('/produto/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put(self):
        """Teste de verificação do PUT"""

        data = {
            'produto':'Produto2',
            'descricao':'Produto2 Criado',
            'link':'https://qitech.com.br/',
            'adquirido':'Sim'
        }
        response = self.client.put('/produto/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
