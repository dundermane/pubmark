var LeafIcon = L.Icon.extend({
    options: {
        shadowUrl: 'icon-shadow.png',
        iconSize:     [38, 95],
        shadowSize:   [50, 64],
        iconAnchor:   [22, 94],
        shadowAnchor: [4, 62],
        popupAnchor:  [-3, -76]
    }
});

var map = L.map('map').setView([43.16506,-77.5883], 18);
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>',
    maxZoom: 20
	}).addTo(map);
	
var greenIcon = new LeafIcon({iconUrl: 'icon-.png'}),
    redIcon = new LeafIcon({iconUrl: 'icon-.png'}),
    orangeIcon = new LeafIcon({iconUrl: 'icon-.png'});
    
L.marker([51.5, -0.09], {icon: greenIcon}).addTo(map).bindPopup("I am a something.");
L.marker([51.495, -0.083], {icon: redIcon}).addTo(map).bindPopup("I am something else.");
L.marker([51.49, -0.1], {icon: orangeIcon}).addTo(map).bindPopup("I an other thing.");
