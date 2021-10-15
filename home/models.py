from django.db import models

class Cliente(models.Model):
    foto = models.ImageField(blank=True, upload_to='photos/perfil /')
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    def __str__(self):
        return self.nome_produto

class Insumos(models.Model):
    id_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    id_cardapio = models.ForeignKey('Cardapio', on_delete=models.DO_NOTHING)
    descricao = models.CharField(max_length=100)
    qtd_produtos = models.IntegerField()
         
class Cardapio(models.Model):
    logo = models.ImageField(blank=True, upload_to='photos/itens/')
    nome_item = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nome_item

class Pedido(models.Model):
    cardapio_id = models.ForeignKey(Cardapio, on_delete=models.DO_NOTHING)
    
# Create your models here.
