from django.contrib import admin
from comparador.models import Servidor, Provedor
# Register your models here.


class ProvedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'logo']


class ServidorAdmin(admin.ModelAdmin):
    list_display = ['nome']

admin.site.register(Servidor, ServidorAdmin)
admin.site.register(Provedor, ProvedorAdmin)


