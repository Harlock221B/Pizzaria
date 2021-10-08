from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    def __str__(self):
        return self.nome_produto

class Insumos(models.Model):
    id_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    id_cardapio = models.ForeignKey('Cardapio', on_delete=models.DO_NOTHING)
    descricao = models.CharField(max_length=100)
    quantidade = models.IntegerField()
         
class Cardapio(models.Model):
    nome_item = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nome_item

class Pedido(models.Model):
    cardapio_id = models.ForeignKey(Cardapio, on_delete=models.DO_NOTHING)
# Create your models here.
