from django.db import models
from django.utils import timezone #Serve per avere la data e ora 
from django.contrib.auth.models import User #Vado a prelevare la tabella utentei di Django
# Create your models here.

class Articoli(models.Model):

    class Stato(models.TextChoices): #Creo le scelte del menù a tendina
        BOZZA = 'BZ', 'Bozza'
        PUBBLICATO = 'PB', 'Pubblicato'
        REVISIONE = 'RV', 'Revisione'

    titolo = models.CharField('Titolo Articolo: ', max_length=150)
    corpo = models.TextField()
    data_pubblicatione = models.DateTimeField(default=timezone.now)
    stato = models.CharField(max_length=2, choices=Stato.choices, default=Stato.BOZZA) #Menù a tendina
    autore = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name_plural = "Articoli"