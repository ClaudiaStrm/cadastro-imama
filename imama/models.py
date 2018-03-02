from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

class Paciente(models.Model):
    imama = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    nome = models.CharField('Nome da paciente', max_length=200, help_text='*')
    local_palestra = models.CharField('Onde assistiu a palestra do IMAMA', blank=True, max_length=200)
    data_nascimento = models.DateField('Data de nascimento', help_text='* Formato: dd/mm/aaaa')
    sexo = models.CharField(max_length=10, help_text='*')
    etnia = models.CharField(max_length=20, help_text='*')
    telefone = models.CharField(max_length=20, help_text='* Exemplo: 99 9999999999')
    celular = models.CharField(max_length=20, blank=True, help_text=' Exemplo: 99 9999999999')
    email = models.CharField(max_length=200, help_text='*')
    endereco = models.CharField('Endereço', max_length=400, help_text='*')
    cidade = models.CharField(max_length=50, help_text='*')
    contato_nome = models.CharField('Pessoa para contato', blank=True, max_length=200)
    contato_telefone = models.CharField('Telefone do contato', blank=True, max_length=20)
    cpf = models.CharField('CPF', max_length=20, help_text=' Apenas números')
    rg = models.CharField('RG', max_length=20, help_text='*')
    amigo_rosa = models.CharField('Navegador', max_length=200, help_text='*')
    data_cadastro = models.DateField(default=timezone.now)
    observacoes = models.TextField('Observações', blank=True)
        #entrevista
    data_entrevista = models.DateField('Data da entrevista e mamografia PoA Rural',default=timezone.now, blank=True, null=True)
    UAB_referencia = models.CharField('Unidade de Atenção Básica de Referência', max_length=200, blank=True)
    cartao_sus = models.CharField('Nº Cartão SUS', max_length=20, blank=True)
    sistema_saude = models.CharField('Utiliza outro tipo de sistema de saúde', max_length=200, blank=True)
    beneficio_governo = models.CharField('Recebe algum benefício do governo', max_length=20, blank=True)
    qtdade_filhos = models.CharField('Estado civil', max_length=20, blank=True)
    estado_civil = models.CharField('Nº de filhos', max_length=20, blank=True)
    idade_filhos = models.CharField('Idade dos filhos', max_length=20, blank=True)
    profissao = models.CharField('Profissão', max_length=50, blank=True)
    exerce_profissao = models.CharField('Atualmente exerce a profissão', max_length=20, blank=True)
    data_menarca = models.DateField('Data da menarca (1ª menstruação)', blank=True, null=True)
    menopausa = models.CharField('Menopausa', max_length=20, blank=True)
    data_menopausa = models.DateField('Desde quando', blank=True, null=True)
    reposicao_hormonal = models.CharField('Reposição hormonal', max_length=20, blank=True)
    data_reposicao_hormonal = models.DateField('Há quanto tempo', blank=True, null=True)
    local_trabalho = models.CharField('Onde trabalha', max_length=200, blank=True)
    sustenta_familia = models.CharField('É responsável pelo sustento da família', max_length=20, blank=True)
    pessoas_familia = models.CharField('Quantas pessoas moram com você', max_length=2, blank=True)
    escolaridade = models.CharField('Escolaridade ', max_length=40, blank=True)
    motivos_servico_saude = models.TextField('Costuma procurar o serviço de saúde para', blank=True)
    ultima_consulta_ginecologista = models.DateField('Data da última consulta com ginecologista', default=timezone.now, blank=True, null=True)
    auto_exame = models.CharField('Costuma examinar suas próprias mamas', max_length=20, blank=True)
    exame_profissional = models.CharField('Suas mamas são apalpadas por profissionais de saúde', max_length=20, blank=True)
    data_mamografia = models.DateField('Data da mamografia mais recente', default=timezone.now, blank=True, null=True)
    conclusao_laudo_mamografia = models.TextField('Conclusão do laudos da mamografia mais recente', blank=True)
    data_outros_exames = models.DateField('Outros exames das mamas (data)', default=timezone.now, blank=True, null=True)
    conclusao_laudo_outros_exames = models.TextField('Conclusão do laudo dos outros exames',blank=True)
    orientacoes_exames = models.TextField('Quais orientações recebeu sobre os resultados dos exames, por quem e quando', blank=True)
    alteracao_mama = models.CharField('Percebeu alguma alteração na mama?', max_length=20, blank=True)
    familiares_cancer_mama = models.CharField('Tem familiares com câncer de mama', max_length=20, blank=True)
    cirurgia_mamas = models.CharField('Já fez alguma cirurgia nas mamas', max_length=20, blank=True)
    tipo_cirurgia_mamas = models.TextField('Tipo de cirugia', blank=True)
    observacoes_entrevista = models.TextField('Observações', blank=True)

    def criar_usuario(username, email, password):
        usuario = User.objects.create_user(username=nome, email=email, password=rg )
        user.save()
        grupo = Group.objects.get(name='Paciente')
        grupo.user_set.add(usuario)

    def publish(self):
        criar_usuario(nome, email, rg)
        self.data_cadastro = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

class AmigoRosa(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField('Endereço', max_length=400)
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20, blank=True)
    contato = models.CharField(max_length=20)
    data_nascimento = models.CharField('Data de nascimento', max_length=20)
    email = models.CharField(max_length=200)
    curso = models.CharField(max_length=200)
    cpf = models.CharField('CPF', max_length=15, help_text="Apenas números")
    rg = models.CharField('RG', max_length=15)

    class Meta:
        permissions = (
            ('pode_adicionar_paciente', 'Pode adicionar paciente'),
            ('pode_editar_paciente', 'Pode editar a paciente'),
    )

    #espaço para foto

    def publish(self):
        self.save()

    def __str__(self):
        return self.nome
