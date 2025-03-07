
from django.contrib import admin
from django.urls import path
from apps.produtos.views import ProdutoListView, ProdutosCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProdutoListView.as_view(), name='produtos'),
    path('produto/add/', ProdutosCreateView.as_view(), name='produto-create')
    
]
