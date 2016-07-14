from django.shortcuts import render
from rest_framework import viewsets
from comparador.models import Servidor
from comparador.serializers import ServidorSerializer
# Create your views here.


class ServidorViewSet(viewsets.ModelViewSet):
    """
    Classe responsavel pela representacao da view da representacao ServidorSerializer
    """
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

    def get_queryset(self):
        f = Servidor.objects.filter
        dados = False
        if self.request.query_params.get('cpu'):
            dados = f(quantidade_cpu=self.request.query_params.get('cpu'))
        return dados or Servidor.objects.all()


def index(request):
    return render(request, 'index.html', {})
