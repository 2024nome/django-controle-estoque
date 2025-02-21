from django.db import models

class Categoria(models.Model):
    nome = models.CharField(verbose_name='categoria', blank='false', null='false', max_length=100)

class meta:
    verbose_name = 'categoria'
    verbose_name_plural = 'categorias'
    db_table = 'categoria' 

def __str__ (self):
    return self.nome