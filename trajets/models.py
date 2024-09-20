# models.py
from django.db import models
import json

class Itineraire(models.Model):
    nom = models.CharField(max_length=100, blank=True)  # Ancien nom
    name = models.CharField(max_length=100, blank=True)  # Nouveau nom
    coordinates = models.TextField(default="[]", blank=True)  # Stocker les coordonnées en tant que texte

    def set_coordinates(self, coords):
        self.coordinates = json.dumps(coords)  # Convertir en JSON

    def get_coordinates(self):
        return json.loads(self.coordinates)  # Convertir en liste
