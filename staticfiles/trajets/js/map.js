// trajets/static/trajets/js/map.js

// Initialisation de la carte Leaflet
var map = L.map("map").setView([5.36, -4.0083], 13);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "© OpenStreetMap contributors",
}).addTo(map);

// Fonction pour afficher l'itinéraire sur la carte
function afficherItineraire(start, end) {
  var url = `https://router.project-osrm.org/route/v1/driving/${start};${end}?overview=full&geometries=geojson`;

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      var coords = data.routes[0].geometry.coordinates;
      var latLngs = coords.map((coord) => [coord[1], coord[0]]);
      var polyline = L.polyline(latLngs, { color: "blue" }).addTo(map);
      map.fitBounds(polyline.getBounds());
    });
}

// Fonction pour charger l'itinéraire en fonction de l'ID
function chargerItineraire(id) {
  fetch(`/trajets/itineraire/${id}/`)
    .then((response) => response.json())
    .then((data) => {
      afficherItineraire(data.start.join(","), data.end.join(","));
    });
}
