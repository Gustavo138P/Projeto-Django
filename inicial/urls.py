from django.urls import path
from inicial.views import inicial, contatos

urlpatterns = [
    path('', inicial),
    path('contatos/', contatos)
]