from django.db import models


class Categoria(models.Model):
    nome = models.CharField(verbose_name='Categoria', blank= False, null=False, max_length=100)

class meta:
    verbose_name = 'categoria'
    verbose_name_plural = 'categorias'
    db_table = 'categoria' 

def __str__ (self):
    return self.nome

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

class Meta:
    verbose_name = 'Produto'
    verbose_name_plural = 'Produtos'
    db_table = 'Produto'

def __str__(self):
    return  self.nome