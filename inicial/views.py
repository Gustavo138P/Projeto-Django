from django.shortcuts import render

def inicial(request):
    return render(request,'inicial/pages/inicial.html')


def contatos(request):
    return render(request, 'contatos/contatos.html')


def projetos(request):
    return render(request,'projetos/projetos.html')

def formacao(request):
    return render(request, 'formacao/formacao.html')
