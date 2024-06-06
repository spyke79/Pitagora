from django.shortcuts import render

from .models import Articoli #Prendo le tabelle che mi interessano del DB
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='index')
def michele(request):
    return render(request,'michele.html')

def articoli(request):
    articoli_lista = Articoli.objects.all() #Vado a prendere tutti gli articoli nel DB e li salvo nella variabile articoli_lista
    return render(request, 'blog/articoli.html', {'articoli_lista':articoli_lista, 'nome':'Pasquale'})