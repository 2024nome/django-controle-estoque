from django.db import models

class Categoria(models.Model):
    nome = models.CharField(verbose_name='categoria', blank= False, null=False, max_length=100)

class meta:
    verbose_name = 'categoria'
    verbose_name_plural = 'categorias'
    db_table = 'categoria' 

def __str__ (self):
    return self.nome

class fornecedor(models.Model):
    nome =  models.CharField ( verbose_name='Nome Fantasia', max_length=150,  blank=False, null=False )
    contato = models.CharField ( verbose_name='Contato', max_length=20,  blank=False, null=False)
    cnpj =  models.CharField ( verbose_name='CNPJ', max_length=150,  blank=False, null=False )
    Email = models.CharField (verbose_name='E-mail', max_length=200,  blank=False, null= False)

class meta:
    verbose_name = 'Fornecedor'
    verbose_name_plural = 'Fornecedores'
    db_table = 'Fornecedor' 

def __str__(self):
    return self.nome