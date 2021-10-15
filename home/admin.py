from django.contrib import admin
from .models import Cardapio, Pedido, Produto, Insumos

class DetCardapio(admin.ModelAdmin):
    list_display = ('id', 'nome_item','valor')
    list_display_links = ('nome_item')
    search_fields = ('nome_item')

admin.site.register(Cardapio)
admin.site.register(Insumos)
admin.site.register(Pedido)
admin.site.register(Produto)

# Register your models here.
