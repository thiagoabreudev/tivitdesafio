from django.test import TestCase
from comparador.models import Servidor


# Create your tests here.


class ServidorTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_servidor_00(self):
        Servidor.objects.create(nome="Servidor TESTE", quantidade_cpu=4, quantidade_memoria=1024,
                                quantidade_hd=200, sistema_operacional='Linux', preco=100.0)
        servidor = Servidor.objects.get(nome='Servidor TESTE')
        self.assertEqual(servidor.quantidade_cpu, 4)
        self.assertEqual(servidor.quantidade_hd, 200)
        self.assertEqual(servidor.quantidade_memoria, 1024)
        self.assertEqual(servidor.sistema_operacional, 'Linux')
        self.assertEqual(servidor.preco, 100.00)
