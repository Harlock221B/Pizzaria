from django.db.models import Q
from django.shortcuts import render, Http404, get_object_or_404
from django.contrib import messages
from .models import Cardapio

def index(request):
    return render(request,'home/index.html')

def cardapio(request):
    cardapios = Cardapio.objects.all()
    return render(request,'home/cardapio.html',{'cardapios':cardapios})

def buscar(request):
    query = request.GET.get('q')
    if query:
        cardapios = Cardapio.objects.filter(
            Q(nome__icontains=query) |
            Q(descricao__icontains=query) |
            Q(preco__icontains=query)
        )
    else:
        cardapios = Cardapio.objects.all()
    return render(request,'home/cardapio.html',{'cardapios':cardapios})

def 
# Create your views here.
