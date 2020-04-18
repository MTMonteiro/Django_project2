from django.shortcuts import render
from .forms import ContatoForm, ApModelForm
from django.contrib import messages
from .models import Aps

def index(request):
    context = {
        'aps': Aps.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    #quando acessa o html gera um GET
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def aps(request):
    if str(request.method) == 'POST':
        form = ApModelForm(request.POST, request.FILES)
        if form.is_valid:
            # Salvar no banco de dados
            form.save()
            messages.success(request, 'Ap inserido com sucesso!')
            form = ApModelForm()
        else:
            messages.error(request, 'Falha ao adicionar o ap, verifique os dados!')
    else:
        form = ApModelForm()
    context = {
        'form': form
    }
    return render(request, 'aps.html', context)

