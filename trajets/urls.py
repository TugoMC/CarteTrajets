# trajets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map_view'),  # Ajoutez une vue pour la carte
    path('save_route/', views.save_route, name='save_route'),
]
