from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nome', 'local_palestra', 'data_nascimento',
        'sexo', 'etnia', 'telefone', 'celular', 'email', 'endereco',
        'cidade', 'contato_nome', 'contato_telefone', 'amigo_rosa',
        'data_entrevista','UAB_referencia', 'cartao_sus',
        'sistema_saude', 'beneficio_governo', 'qtdade_filhos',
        'estado_civil', 'idade_filhos', 'profissao',
        'exerce_profissao', 'data_menarca', 'menopausa',
        'data_menopausa', 'reposicao_hormonal', 'data_reposicao_hormonal',
        'local_trabalho', 'sustenta_familia', 'pessoas_familia',
        'escolaridade', 'motivos_servico_saude', 'ultima_consulta_ginecologista',
        'auto_exame', 'exame_profissional', 'data_mamografia',
        'conclusao_laudo_mamografia', 'data_outros_exames', 'conclusao_laudo_outros_exames',
        'orientacoes_exames', 'alteracao_mama', 'familiares_cancer_mama',
        'cirurgia_mamas', 'tipo_cirurgia_mamas', 'observacoes_entrevista',
        )
