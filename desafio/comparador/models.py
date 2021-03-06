from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Provedor(models.Model):
    nome = models.CharField(verbose_name=u'Provedor', max_length=200)
    logo = models.ImageField(verbose_name="Logo")

    class Meta:
        db_table = u'provedor'
        verbose_name_plural = 'Provedores'

    def __unicode__(self):
        return self.nome


class Servidor(models.Model):
    """
    Classe responsavel por manter os dados cadastrais dos servidores
    """

    nome = models.CharField(verbose_name=u'Nome', max_length=100)
    quantidade_cpu = models.IntegerField(verbose_name=u'Quantidade de CPU',)
    quantidade_memoria = models.IntegerField(verbose_name=u'Quantidade memoria')
    quantidade_hd = models.IntegerField(verbose_name=u'Quantidade de HD')
    sistema_operacional = models.CharField(verbose_name=u'Sistema Operacional', max_length=200)
    preco = models.FloatField(verbose_name=u'Preco')
    provedor = models.ForeignKey(Provedor, verbose_name='Provedor')

    class Meta:
        db_table = u'servidor'
        verbose_name_plural = u'Servidores'

    def __unicode__(self):
        return self.nome
