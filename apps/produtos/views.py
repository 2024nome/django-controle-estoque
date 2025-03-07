from django.shortcuts import render
from django.views.generic import ListView
from produtos.models import produtos
class ProdutoListView(ListView):
    model = produtos
    template_name = 'produtos/produtos.html'
    context_object_name = 'produtos'
    paginate_by = 10

