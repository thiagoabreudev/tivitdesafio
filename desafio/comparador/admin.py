from django.contrib import admin
from comparador.models import Servidor, Provedor
# Register your models here.


class ProvedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'logo']


class ServidorAdmin(admin.ModelAdmin):
    search_fields = ['nome',  'sistema_operacional']
    list_display = ['id', 'nome', 'provedor_nome', 'quantidade_cpu', 'quantidade_hd',
                    'quantidade_memoria', 'sistema_operacional']
    list_editable = ['nome', 'quantidade_cpu', 'quantidade_hd',
                     'quantidade_memoria', 'sistema_operacional']
    list_filter = ['nome', 'quantidade_cpu', 'quantidade_hd',
                   'quantidade_memoria', 'sistema_operacional', 'provedor']

    def provedor_nome(self, obj):
        return obj.provedor.nome

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'provedor':
            kwargs["queryset"] = Provedor.objects.all()
        return super(ServidorAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Servidor, ServidorAdmin)
admin.site.register(Provedor, ProvedorAdmin)


