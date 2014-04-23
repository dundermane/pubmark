
var LeafIcon2 = L.Icon.extend({
    options: {
        shadowUrl: '/images/icn/bmin.svg',
        iconSize:     [38, 95],
        shadowSize:   [50, 64],
        iconAnchor:   [22, 94],
        shadowAnchor: [4, 62],
        popupAnchor:  [-3, -76]
    }
});

var LeafIcon = L.Icon.extend({
    options: {
        iconSize:     [32, 32],
        iconAnchor:   [22, 16],
        popupAnchor:  [-3, -16]
    }
});



var map = L.map('map').setView([43.16506,-77.5883], 18);
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>',
    maxZoom: 20
	}).addTo(map);

var icons = {};
icons['meat'] = new LeafIcon({iconUrl: '/images/icn/bmin.svg'}),
icons['redIcon'] = new LeafIcon({iconUrl: '/images/icn/meat.svg'}),
icons['orangeIcon'] = new LeafIcon({iconUrl: '/images/icn/flowers.svg'});
    
//test markers
L.marker([43.16506,-77.5883], {icon: icons['meat']}).addTo(map).bindPopup("This is the center.");
L.marker([43.1659,-77.5883], {icon: icons['redIcon']}).addTo(map).bindPopup("I am something else.");
L.marker([43.1642,-77.5883], {icon: icons['orangeIcon']}).addTo(map).bindPopup("I an other thing.");
recentIcons();

//Show all the last locations for all vendors
function recentIcons() {
	var getting = true;
	var n = 0;
	while(n<10&&getting==true) {
	  getting = $.getJSON('/_recent_merchants', {
	    n: n,
	  }, function(data) {
	    if (data.geo) {
	    	populate(data);
	    	return true;
	    }
	    else
	    {
	    	return true;
	    }
	  }).fail( function(d) {
            return false;
      });
	  n++;
	};
};

//show all the locations for one vendor.
function populateVendorIcons(vendor) {

};

function populate(merchant) {
	console.log(merchant.geo.coordinates);
	L.marker(merchant.geo.coordinates, 
			{icon: icons[merchant.category]})
	.addTo(map)
	.bindPopup("This is a Merchant");
};

//in bounds
var lonbounds = [43.1659,43.1642];
var latbounds = [-77.5910,-77.5874];
function inBounds(geo) {
	if (geo[0] >= lonbounds[0] && geo[0] <= lonbounds[1] && geo[1] >= latbounds[0] && geo[1] <= latbounds[1]) {return true}
	else {return false}
};

