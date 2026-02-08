from django.db import models



# Create your models here.
from django.db import models

class Certificat(models.Model):
    nom_habitant = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    date_emission = models.DateField(auto_now_add=True)
    numero_certificat = models.CharField(max_length=20, unique=True)
    statut_paiement = models.CharField(max_length=20, default='non payé')

    def __str__(self):
        return f"{self.nom_habitant} - {self.numero_certificat}"

