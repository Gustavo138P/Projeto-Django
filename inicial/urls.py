from django.urls import path
from inicial.views import inicial, contatos, projetos, formacao

urlpatterns = [
    path('', inicial),
    path('contatos/', contatos),
    path('projetos/', projetos),
    path('formacao/', formacao),
]