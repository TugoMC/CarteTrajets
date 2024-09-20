# trajets/views.py
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Itineraire


def map_view(request):
    return render(request, 'map.html')  # Assurez-vous que 'map.html' est bien dans le dossier 'templates'






def save_route(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        coordinates = data.get('coordinates')
        line_name = data.get('name')

        # Créer et sauvegarder l'objet Itineraire
        itineraire = Itineraire(name=line_name)
        itineraire.set_coordinates(coordinates)
        itineraire.save()

        return JsonResponse({'status': 'success', 'data': {'name': line_name, 'coordinates': coordinates}})
    return JsonResponse({'status': 'error'}, status=400)