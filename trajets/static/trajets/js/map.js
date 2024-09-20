// Gérer l'événement de création d'une polyligne
map.on(L.Draw.Event.CREATED, function (event) {
  var layer = event.layer;
  drawnItems.addLayer(layer);

  // Obtenir les coordonnées de la polyligne
  var coords = layer.getLatLngs();
  console.log("Itinéraire tracé : ", coords);

  // Envoyer les coordonnées au serveur Django
  fetch("/trajets/save_route/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": "{{ csrf_token }}", // Ajouter le token CSRF si nécessaire
    },
    body: JSON.stringify({ coordinates: coords }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Itinéraire sauvegardé :", data);
    });
});
