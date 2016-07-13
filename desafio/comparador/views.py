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
