from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Paciente
from django.shortcuts import render, get_object_or_404
from .forms import PacienteForm
from .forms import AmigoRosaForm
from datetime import date
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required


def pacientes(request):
    pacientes = Paciente.objects.filter(data_cadastro__lte=timezone.now()).order_by('data_cadastro')
    return render(request, 'imama/pacientes.html', { 'pacientes' : pacientes })

def paciente_detalhe(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'imama/paciente_detalhe.html', { 'paciente': paciente })

def nova_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.imama = request.user
            #paciente.data_cadastro = timezone.now()
            paciente.save()
            user = User.objects.create_user(username=paciente.nome, email=paciente.email, password=paciente.rg )
            user.save()
            grupo = Group.objects.get(name='Pacientes')
            grupo.user_set.add(user)
            return redirect('paciente_detalhe', pk=paciente.pk)
    else:
        form = PacienteForm()
        return render(request, 'imama/form_paciente.html', {'form': form})

def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.imama = request.user
            #paciente.data_cadastro = timezone.now()
            paciente.save()
            return redirect('paciente_detalhe', pk=paciente.pk)
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'imama/form_paciente.html', {'form': form})


def novo_navegador(request):
    if request.method == "POST":
        form = AmigoRosaForm(request.POST)
        if form.is_valid():
            amigo_rosa = form.save(commit=False)
            amigo_rosa.imama = request.user
            #paciente.data_cadastro = timezone.now()
            amigo_rosa.save()
            user = User.objects.create_user(username=amigo_rosa.rg, email=amigo_rosa.email, password=amigo_rosa.rg)
            user.save()
            grupo = Group.objects.get(name='Amigos Rosa')
            grupo.user_set.add(user)
            return redirect('/')
    else:
        form = AmigoRosaForm()
        return render(request, 'imama/form_navegador.html', {'form': form})
