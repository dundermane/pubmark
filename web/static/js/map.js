

var LeafIcon = L.Icon.extend({
    options: {
        iconSize:     [32, 32],
        iconAnchor:   [22, 16],
        popupAnchor:  [-3, -16],
        shadowSize:   [32, 32],
        shadowAnchor: [22, 16]
    }
});



var map = L.map('map').setView([43.16506,-77.5883], 18);
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>',
    maxZoom: 20
	}).addTo(map);

var icons = {};
icons['meat'] = new LeafIcon({iconUrl: '/images/icn/produce.png'}),
icons['coffee'] = new LeafIcon({iconUrl: '/images/icn/bread.png'}),
icons['produce'] = new LeafIcon({iconUrl: '/images/icn/local.png'}),

    
//dummy markers
L.marker([43.16506,-77.5883], {icon: icons['meat']}).addTo(map).bindPopup("This is the center.");
L.marker([43.16544, -77.58887], {icon: icons['meat']}).addTo(map);
L.marker([43.16537, -77.58924], {icon: icons['coffee']}).addTo(map);
L.marker([43.16528, -77.58822], {icon: icons['produce']}).addTo(map);
L.marker([43.16493, -77.58952], {icon: icons['produce']}).addTo(map);
L.marker([43.16469, -77.58864], {icon: icons['produce']}).addTo(map);
L.marker([43.16544, -77.58868], {icon: icons['coffee']}).addTo(map);
L.marker([43.16522, -77.58866], {icon: icons['produce']}).addTo(map);
L.marker([43.16502, -77.58904], {icon: icons['meat']}).addTo(map);
L.marker([43.16546, -77.58943], {icon: icons['meat']}).addTo(map);
L.marker([43.16515, -77.58985], {icon: icons['meat']}).addTo(map);
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

