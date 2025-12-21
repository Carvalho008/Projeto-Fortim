from django import forms
from django.core.exceptions import ValidationError
from .models import RespostaPesquisa


class RespostaPesquisaForm(forms.ModelForm):

    class Meta:
        model = RespostaPesquisa
        exclude = ("criado_em",)

        widgets = {
            # Texto / número
            "nome_apelido": forms.TextInput(attrs={"placeholder": "Digite seu nome ou apelido"}),
            "idade": forms.NumberInput(attrs={"placeholder": "Ex: 35"}),
            "tempo_pesca": forms.NumberInput(attrs={"placeholder": "Ex: 10","min": 0}),
            "outra_renda": forms.TextInput(attrs={"placeholder": "Outra fonte de renda"}),
            "quantidade_familiares": forms.NumberInput(attrs={"placeholder": "Quantidade"}),
            "qual_pos_captura": forms.TextInput(attrs={"placeholder": "Qual atividade"}),
            "material_outro": forms.TextInput(attrs={"placeholder": "Outro material"}),
            "zona_outro": forms.TextInput(attrs={"placeholder": "Outra área ou zona"}),
            "conservacao_outro": forms.TextInput(attrs={"placeholder": "Outra forma"}),
            "problema_outro": forms.TextInput(attrs={"placeholder": "Outro problema"}),
            "especies_principais": forms.Textarea(attrs={"placeholder": "Principais espécies", "rows": 2}),

            # Radios
            "genero": forms.RadioSelect,
            "escolaridade": forms.RadioSelect,
            "renda_pesca": forms.RadioSelect,
            "pesca_principal_renda": forms.RadioSelect,
            "familiares_pescadores": forms.RadioSelect,
            "atividade_pos_captura": forms.RadioSelect,
            "possui_registro": forms.RadioSelect,
            "materiais_guardados": forms.RadioSelect,
            "existe_ponto_coleta": forms.RadioSelect,
            "participaria_programa": forms.RadioSelect,
            "reaproveitamento_artesanato": forms.RadioSelect,
            "percepcao_captura": forms.RadioSelect,
            "turismo_pesca": forms.RadioSelect,
            "turismo_valoriza": forms.RadioSelect,

            # Checkboxes
            "materiais": forms.CheckboxSelectMultiple,
            "zonas_pesca": forms.CheckboxSelectMultiple,
            "conservacao": forms.CheckboxSelectMultiple,
            "problemas": forms.CheckboxSelectMultiple,
            "destino_descarte": forms.CheckboxSelectMultiple,
            "meses_mais_produtivos": forms.CheckboxSelectMultiple,
            "meses_menos_produtivos": forms.CheckboxSelectMultiple,
        }
        
        # =========================
        # LABELS (PERGUNTAS)
        # =========================
        labels = {
            "nome_apelido": "1. Nome ou apelido",
            
            "idade": "2. Idade (em anos completos)",
            
            "genero": "3. Gênero",
            
            "escolaridade": "4. Qual é o seu nível de escolaridade?",
            
            "tempo_pesca": "5. Há quanto tempo você se dedica à pesca artesanal?(em anos)",

            "pesca_principal_renda": "6. A pesca é sua principal fonte de renda?",
            "outra_renda": "Se não, qual é?",

            "renda_pesca": "7. Quanto em geral é a renda familiar total que provém da pesca por mês?",

            "familiares_pescadores": (
                "8. Existem mais pessoas da família que realizam a pesca artesanal?"
            ),
            "quantidade_familiares": "Se sim, quantas pessoas?",

            "atividade_pos_captura": (
                "9. Você desenvolve alguma atividade de pós-captura "
                "(beneficiamento, venda, etc.)?"
            ),
            "qual_pos_captura": "Se sim, qual?",

            "possui_registro": (
                "10. Você possui registro em colônia ou associação de pescadores?"
            ),

            "materiais": (
                "11. Quais são os principais materiais utilizados na sua pesca? "
                "(Selecione todos que se aplicam)"
            ),
            "material_outro": "Outro:",

            "meses_mais_produtivos": (
                "12. Em quais meses do ano a pesca é mais intensa ou produtiva?"
            ),

            "meses_menos_produtivos": (
                "13. Em quais meses do ano a pesca é menos produtiva?"
            ),

            "zonas_pesca": (
                "14. Quais são as principais áreas ou zonas de pesca que você utiliza?"
            ),
            "zona_outro": "Outro:",

            "especies_principais": (
                "15. Quais são as três principais espécies que você costuma capturar?"
            ),

            "percepcao_captura": (
                "16. Como você avalia a captura de pescados nos últimos cinco anos?"
            ),

            "conservacao": (
                "17. Como o pescado é conservado após o desembarque?"
            ),
            "conservacao_outro": "Outro:",

            "problemas": (
                "18. Quais são os principais problemas ou preocupações que afetam "
                "atualmente a sua atividade de pesca artesanal?"
            ),
            "problema_outro": "Outro:",

            "destino_descarte": (
                "19. Onde você normalmente descarta os materiais de pesca inutilizados?"
            ),

            "materiais_guardados": (
                "20. Você possui materiais de pesca inutilizados guardados(em casa, depósito, etc.) que gostaria de descartar corretamente?"
            ),

            "existe_ponto_coleta": (
                "21. Sua comunidade possui algum programa ou ponto de coleta específico para materiais de pesca desgastados ou inutilizados?"
            ),

            "participaria_programa": (
                "22. Se houvesse um programa fácil e acessível para a coleta e reciclagem de materiais de pesca, "
                "você participaria?"
            ),

            "reaproveitamento_artesanato": (
                "23. Você, alguém da sua família ou amigos reaproveitam os materiais obsoletos e/ou sem condições de uso para pesca, "
                "para criar artesanato? "
            ),

            "turismo_pesca": "24. Na sua comunidade as atividades de turismo vem ocorrendo em conjunto com as atividades de pesca como experiências?",

            "turismo_valoriza": "25. Você considera que o turismo pode contribuir para a valorização das atividades da pesca desenvolvidas pela comunidade ?",
        }


    def clean_nome_apelido(self):
        nome = self.cleaned_data.get("nome_apelido")

        if RespostaPesquisa.objects.filter(nome_apelido__iexact=nome).exists():
            raise ValidationError(
                "Já existe uma pesquisa cadastrada com este nome ou apelido. "
                "Se for você, procure a equipe responsável."
            )

        return nome