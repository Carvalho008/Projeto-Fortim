from django.db import models

# ================================
# MODELS AUXILIARES (OPÇÕES)
# ================================

class SimNao(models.Model):
    valor = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Opção Sim / Não"
        verbose_name_plural = "Opções Sim / Não"

    def __str__(self):
        return self.valor


class Genero(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Escolaridade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class RendaPesca(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class MaterialPesca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Mes(models.Model):
    nome = models.CharField(max_length=15)
    ordem = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["ordem"]

    def __str__(self):
        return self.nome


class ZonaPesca(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class ConservacaoPescado(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class ProblemaPesca(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class DestinoDescarte(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class PercepcaoCapturaOpcao(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class TurismoPescaOpcao(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class TurismoValorizaOpcao(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


# ================================
# MODEL PRINCIPAL
# ================================

class RespostaPesquisa(models.Model):

    # 1. Identificação
    nome_apelido = models.CharField(max_length=100, unique=True)
    idade = models.PositiveSmallIntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)

    # 2. Escolaridade
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.PROTECT)

    # 3. Tempo de pesca
    tempo_pesca = models.PositiveSmallIntegerField(
    verbose_name="Tempo de pesca (em anos)"
    )


    # 4. Renda
    pesca_principal_renda = models.ForeignKey(
        SimNao, on_delete=models.PROTECT, related_name="pesca_principal"
    )
    outra_renda = models.CharField(max_length=100, blank=True)
    renda_pesca = models.ForeignKey(RendaPesca, on_delete=models.PROTECT)

    # 6. Família
    familiares_pescadores = models.ForeignKey(
        SimNao, on_delete=models.PROTECT, related_name="familiares"
    )
    quantidade_familiares = models.PositiveSmallIntegerField(null=True, blank=True)

    # 7. Pós-captura
    atividade_pos_captura = models.ForeignKey(
        SimNao, on_delete=models.PROTECT, related_name="pos_captura"
    )
    qual_pos_captura = models.CharField(max_length=100, blank=True)

    # 8. Registro
    possui_registro = models.ForeignKey(
        SimNao, on_delete=models.PROTECT, related_name="registro"
    )

    # 9. Materiais
    materiais = models.ManyToManyField(MaterialPesca, blank=True)
    material_outro = models.CharField(max_length=100, blank=True)

    # 10 / 11. Sazonalidade
    meses_mais_produtivos = models.ManyToManyField(
        Mes, related_name="mais_produtivos", blank=True
    )
    meses_menos_produtivos = models.ManyToManyField(
        Mes, related_name="menos_produtivos", blank=True
    )

    # 12. Áreas
    zonas_pesca = models.ManyToManyField(ZonaPesca, blank=True)
    zona_outro = models.CharField(max_length=100, blank=True)

    # 13. Espécies
    especies_principais = models.TextField()

    # 14. Percepção
    percepcao_captura = models.ForeignKey(
        PercepcaoCapturaOpcao, on_delete=models.PROTECT
    )

    # 15. Conservação
    conservacao = models.ManyToManyField(ConservacaoPescado, blank=True)
    conservacao_outro = models.CharField(max_length=100, blank=True)

    # 16. Problemas
    problemas = models.ManyToManyField(ProblemaPesca, blank=True)
    problema_outro = models.CharField(max_length=150, blank=True)

    # 17. Descarte
    destino_descarte = models.ManyToManyField(DestinoDescarte, blank=True)

    # 18–21. Programas ambientais
    materiais_guardados = models.ForeignKey(
        SimNao, on_delete=models.PROTECT, related_name="materiais_guardados"
    )
    existe_ponto_coleta = models.ForeignKey(
        SimNao, on_delete=models.PROTECT, related_name="ponto_coleta"
    )
    participaria_programa = models.ForeignKey(
        SimNao, on_delete=models.PROTECT, related_name="participaria"
    )
    reaproveitamento_artesanato = models.ForeignKey(
        SimNao, on_delete=models.PROTECT, related_name="artesanato"
    )

    # 22 / 23. Turismo
    turismo_pesca = models.ForeignKey(
        TurismoPescaOpcao, on_delete=models.PROTECT
    )
    turismo_valoriza = models.ForeignKey(
        TurismoValorizaOpcao, on_delete=models.PROTECT
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_apelido
