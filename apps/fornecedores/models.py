from django.db import models
from django import models

class Fornecedores(models.Model):
    nome = models.CharField(verbose_name='nome', blank='false', null='false', max_length=50)
    contato = models.CharField(verbose_name='contato', blank='false', null='false', max_length=15)
    cpnj = models.CharField(verbose_name='cnpj', blank='false', null='false', max_length=14)
    Email = models.CharField (verbose_name='E-mail', max_length=100,  blank=False, null= False)


    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        db_table = 'fornecedor' 


class Categoria(models.Model):
    nome = models.CharField(verbose_name='categoria', blank= False, null=False, max_length=100)

class meta:
    verbose_name = 'categoria'
    verbose_name_plural = 'categorias'
    db_table = 'categoria' 

def __str__ (self):
    return self.nome
