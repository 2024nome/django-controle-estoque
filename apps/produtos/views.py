from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView
from produtos.models import Produtos

class ProdutoListView(ListView):
    model = Produtos
    template_name = 'produtos/produtos.html'
    context_object_name = 'produtos'
    paginate_by = 10

class ProdutosCreateView(CreateView):
    model = Produtos
    fields = ['nome','marca','descricao', 'preco', 'quantidadeEstoque', 'categoria', 'fornecedor', 'imagem']
    template_name = 'produtos/produto_create_update.html'
    sucess_url = reverse_lazy('produtos')