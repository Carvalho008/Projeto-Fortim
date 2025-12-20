from django.contrib import admin
from .models import *

# Opções
admin.site.register(SimNao)
admin.site.register(Genero)
admin.site.register(Escolaridade)
admin.site.register(RendaPesca)
admin.site.register(MaterialPesca)
admin.site.register(Mes)
admin.site.register(ZonaPesca)
admin.site.register(ConservacaoPescado)
admin.site.register(ProblemaPesca)
admin.site.register(DestinoDescarte)
admin.site.register(PercepcaoCapturaOpcao)
admin.site.register(TurismoPescaOpcao)
admin.site.register(TurismoValorizaOpcao)


@admin.register(RespostaPesquisa)
class RespostaPesquisaAdmin(admin.ModelAdmin):
    list_display = ("nome_apelido", "idade", "genero", "criado_em")
    search_fields = ("nome_apelido",)
    ordering = ("-criado_em",)
