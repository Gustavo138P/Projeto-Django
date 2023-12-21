from django.shortcuts import render

def inicial(request):
    return render(request,'inicial/inicial.html')

def contatos(request):
    return render(request, 'contatos/contatos.html')
