#!/usr/bin/python
# -*- encoding: utf-8 -*-

from rest_framework import serializers
from comparador.models import Servidor, Provedor


class ProvedorSerializer(serializers.HyperlinkedModelSerializer):
    """
    Classe responsavel pela representacao dos dados da entidade Servidor
    """
    class Meta:
        model = Provedor
        fields = ('nome', 'logo')


class ServidorSerializer(serializers.HyperlinkedModelSerializer):
    """
    Classe responsavel pela representacao dos dados da entidade Servidor
    """
    provedor = ProvedorSerializer(many=False)

    class Meta:
        model = Servidor
        fields = ('nome', 'quantidade_cpu', 'quantidade_memoria', 'quantidade_hd',
                  'sistema_operacional', 'preco', 'provedor')
