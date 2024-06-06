
from django.urls import path
from . import views #Importo tutte le funzioni in Views.py

urlpatterns = [
    path('', views.index, name='index'),
    path('michele/', views.michele, name='michele'),
    path('articoli/', views.articoli, name='articoli'),
]