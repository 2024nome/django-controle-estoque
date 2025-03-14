from django.db import models
from django.contrib.auth.models import User



class Categoria(models.Model):
    nome = models.CharField(verbose_name='Categoria', blank= False, null=False, max_length=100)

class meta:
    verbose_name = 'categoria'
    verbose_name_plural = 'categorias'
    db_table = 'categoria' 

def __str__ (self):
    return self.no
class Fornecedor(models.Model):
    nome =  models.CharField ( verbose_name='Nome Fantasia', max_length=150,  blank=False, null=False )
    contato = models.CharField ( verbose_name='Contato', max_length=20,  blank=False, null=False)
    cnpj =  models.CharField ( verbose_name='CNPJ', max_length=150,  blank=False, null=False )
    email = models.CharField (verbose_name='E-mail', max_length=200,  blank=False, null= False)

class meta:
    verbose_name = 'Fornecedor'
    verbose_name_plural = 'Fornecedores'
    db_table = 'Fornecedor'
    

def __str__(self):
    return (f'{self.nome} - {self.cnpj}')

class Produtos(models.Model):
    nome = models.CharField (verbose_name='nome do produto', max_length = 50, blank=False, null=False)
    descricao = models.CharField (verbose_name='Descrição do Produtos', max_length = 200)
    preco = models.DecimalField (verbose_name='valor', decimal_places=2, max_digits= 10 ,blank=False, null=False )
    quantidadeEstoque = models.PositiveBigIntegerField (verbose_name='Quantidade', default=0)
    categoria = models.ForeignKey (Categoria, on_delete=models.PROTECT)
    fornecedor = models.ForeignKey (Fornecedor, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    imagem = models.ImageField(null=True, blank=True, default='/images/placeholder.png')
    marca = models.CharField(max_length=200, null=True, blank=True)
    avaliacao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    criadoEm = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        db_table = 'Produto'

    def __str__(self):
        return  (f'{self.nome} | {self.marca} | R${str(self.preco)}')

