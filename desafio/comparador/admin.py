from django.contrib import admin
from comparador.models import Servidor
# Register your models here.


class ServidorAdmin(admin.ModelAdmin):
    list_display = ['nome']

admin.site.register(Servidor, ServidorAdmin)


