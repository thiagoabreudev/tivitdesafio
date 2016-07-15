from django.shortcuts import render
from rest_framework import viewsets
from comparador.models import Servidor, Provedor
from comparador.serializers import ServidorSerializer, ProvedorSerializer
# Create your views here.


class ProvedorViewSet(viewsets.ModelViewSet):
    """
    Classe responsavel pela representacao da view da representacao ProvedorSerializer
    """
    queryset = Provedor.objects.all()
    serializer_class = ProvedorSerializer


class ServidorViewSet(viewsets.ModelViewSet):
    """
    Classe responsavel pela representacao da view da representacao ServidorSerializer
    """
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

    def get_queryset(self):
        dados = Servidor.objects.all()
        filtro = self.request.query_params
        if filtro.get('quantidade_cpu'):
            dados = filter(lambda i: str(i.quantidade_cpu) == filtro.get('quantidade_cpu'), dados)
        if filtro.get('quantidade_memoria'):
            dados = filter(lambda i: str(i.quantidade_memoria) == filtro.get('quantidade_memoria'),
                           dados)
        if filtro.get('preco'):
            try:
                preco = float(filtro.get('preco'))
                dados = filter(lambda i: i.preco <= preco, dados)
            except ValueError:
                pass
        if filtro.get('sistema_operacional'):
            dados = filter(lambda i: filtro.get('sistema_operacional').upper() in
                           i.sistema_operacional.upper(), dados)
        return dados


def index(request):
    return render(request, 'index.html', {})
