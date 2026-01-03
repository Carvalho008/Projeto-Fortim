import math
from django.db.models import Avg, Count
from .models import RespostaPesquisa

# Função reutilizável

def valor_mais_frequente(campo):
    """
    campo: string no formato 'campo' ou 'campo__atributo'
    Ex: 'genero__nome', 'possui_registro__valor'
    """
    resultado = (
        RespostaPesquisa.objects
        .values(campo)
        .annotate(total=Count(campo))
        .order_by('-total')
        .first()
    )

    return resultado[campo] if resultado else None

# Funções

def get_infos_tabela() -> list:
     return [
        get_qtd(),
        get_media_idade(),
        get_genero_maioria(),
        get_nivel_escolaridade_maioria(),
        get_registro_maioria(),
        get_meses_mais_produtivos(),
    ]

def get_qtd() -> dict:
    qtd = RespostaPesquisa.objects.count()
    
    return {'title': "Quantidade de pesquisas", 'value': qtd, 'style': 's-full'}

def get_media_idade() -> dict:
    resultado = RespostaPesquisa.objects.aggregate(media=Avg('idade'))
    media = resultado['media']

    if media is None:
        media = 0

    media = math.ceil(media)

    return {'title': "Média das idades", 'value': f'{media} anos', 'style': 's-1'}

def get_genero_maioria() -> dict:
    res = valor_mais_frequente('genero__nome')
    
    return {'title': "Gênero predominante", 'value': res, 'style': 's-2'}

def get_nivel_escolaridade_maioria() -> dict:
    res = valor_mais_frequente('escolaridade__nome')
    
    return {'title': "Nível de escolaridade mais comum", 'value': res, 'style': 's-3'}

def get_registro_maioria() -> dict:
    res = valor_mais_frequente('possui_registro__valor')
    
    return {'title': "Maioria possui registro", 'value': res, 'style': 's-1'}

def get_meses_mais_produtivos() -> dict:
    
    meses = (
        RespostaPesquisa.objects
        .values('meses_mais_produtivos__nome')
        .annotate(total=Count('meses_mais_produtivos'))
        .order_by('-total')[:4]
    )

    nomes = [
        mes['meses_mais_produtivos__nome']
        for mes in meses
        if mes['meses_mais_produtivos__nome']
    ]
    
    res = ', '.join(nomes) if nomes else "—"
    
    return {'title': "Meses mais produtivos", 'value': res, 'style': 's-4'}