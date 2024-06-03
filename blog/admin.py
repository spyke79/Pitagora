from django.contrib import admin
from .models import Articoli

# Register your models here.

@admin.register(Articoli)
class ArticoliAdmin(admin.ModelAdmin):
    list_display = ['titolo','autore','stato'] #Colonne della tabella
    list_filter = ['data_pubblicatione', 'stato'] #Filtri laterali