from django.shortcuts import render
from django.views.generic import ListView

#class home(ListView):
#    template_name='home.html'


def index(request):
    return render(request, 'produtos/produtos.html')

