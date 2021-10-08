from django.db.models import Q
from django.shortcuts import render, Http404, get_object_or_404
from django.contrib import messages
from .models import Cardapio

def index(request):
    
    return render(request,'home/index.html')

# Create your views here.
