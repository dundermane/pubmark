//Connect to Database
<?php
	//Globals for whole site
	$URL = 'localhost';

	// Connecting, selecting database
	$link = mysql_connect($URL , 'webuser', 'iamauser')
	or die('Could not connect: ' . mysql_error());
	mysql_select_db('pubmark') or die('//Could not select database');
?>

function loadResources(sources, callback) {
  var assetDir = 'images/';
  var images = {};
  var loadedImages = 0;
  var numImages = 0;
  for(var src in sources) {
    numImages++;
  }
  for(var src in sources) {
    images[src] = new Image();
    images[src].onload = function() {
      if(++loadedImages >= numImages) {
        callback(images);
      }
    };
    images[src].src = assetDir + sources[src];
  }
}
function buildStage(images) {

	var zin_button = new Kinetic.Image({
		x: 5, y: 5,
		height: 40, width: 40,
		image: images.zin
	});
	
	var zout_button = new Kinetic.Image({
		x: 5, y: 50,
		height: 40, width: 40,
		image: images.zout
	});

	var blip_min = new Kinetic.Image({
		x: 5, y: 5,
		height: 40, width: 40,
		image: images.bmin
	});

	<?php
		// Performing SQL query
		$lastSat = strtotime('last Saturday + 5 hours');
		$query = 'SELECT Category FROM vendors WHERE LastCheckIn >' . $lastSat . ' GROUP BY Category';
		$result = mysql_query($query) or die('alert(Query failed: ' . mysql_error() . ');');

		// Defining all Category Icons
		while ($map_icon = mysql_fetch_array($result, MYSQL_ASSOC)) {
			echo "\tvar icon_" . $map_icon["Category"] . " = new Kinetic.Image({\n";
			echo "\t\tx: 5, y: 5,\n";
			echo "\t\theight: 40, width: 40,\n";
			echo "\t\timage: images." . $map_icon["Category"] . "\n";
			echo "\t});\n";
		}
		mysql_free_result($result);
	?>	

	//Define the Map
  var map = new Kinetic.Image({
    x: 0,
    y: 0,
    image: images.mapObj,
    width: 400,
    height: 400
  });
  maplay.setWidth(map.getWidth());
  maplay.setHeight(map.getHeight());
  
	// add the objects to the layers
	maplay.add(map);
	fore.add(zin_button);
	fore.add(zout_button);

	<?php /////////JSON NEEDED	
		// Performing SQL query
		$lastSat = strtotime('last Saturday + 5 hours');
		$query = 'SELECT ID, Category, LastLocX, LastLocY FROM vendors WHERE LastCheckIn >' . $lastSat;
		$result = mysql_query($query) or die('Query failed: ' . mysql_error());

		// Placing all the Vendor Icons
		$i = 1;
		while ($vendor_blip = mysql_fetch_array($result, MYSQL_ASSOC)) {
			echo "\nvar vendor" . $i . " = new Kinetic.Group({\n";
			echo "\tx: " . $vendor_blip["LastLocX"] . ",\n";
			echo "\ty: " . $vendor_blip["LastLocY"] . "\n";
			echo "});\n";
			echo "\nvendor" . $i . ".add(blip_min);";
			echo "\nvendor" . $i . ".add(icon_" . $vendor_blip["Category"] . ");\n";
			echo "\nmaplay.add(vendor" . $i . ");\n\n";
			$i += 1;
		}
		mysql_free_result($result);	
	?>
	
	// add the layers to the stage
	stage.add(maplay);
	stage.add(fore);
	
	zin_button.on('mousedown touchstart', function() {
		zoomIn();
	});

	zout_button.on('mousedown touchstart', function()  {
		zoomOut();
	});	

	zout_button.on('dbltap dblclick', function() {
		zoom1();
		maplay.setX(0);
		maplay.setY(0);
		maplay.draw();
	});

	document.addEventListener("mousewheel", wheelzoom, false)

  
}

//Define the Stage (canvas)
var stage = new Kinetic.Stage({
  container: 'content2',
  width: document.getElementById('content2').offsetWidth,
  height: document.getElementById('content2').offsetWidth
});

var maxzoom = 5;

//Define the Layers	
var fore = new Kinetic.Layer();
var maplay = new Kinetic.Layer({
	scaleY: 1,
	scaleX: 1,
	x: 0,
	y: 0,
	width: 1,
	height: 1,
  draggable: true,
  dragBoundFunc: function(pos) {
    var X=pos.x;
    var Y=pos.y;
    if(X<minX){X=minX;}
    if(X>maxX){X=maxX;}
    if(Y<minY){Y=minY;}
    if(Y>maxY){Y=maxY;}
    return({x:X, y:Y});
  }
});


var sources = {
	mapObj: 'pubmark_map.png',
	zin: 'zin.svg',
	zout: 'zout.svg',
	//JSON: GET ALL ICON FILE NAMES
};

//define the dragging bounds of maplay
var minX=-maplay.scaleX()*maplay.getWidth()+stage.width();
var maxX=0;
var minY=-maplay.scaleY()*maplay.getHeight()+stage.height();
var maxY=0;

//ZOOM FUNCTIONS
function zoomIn() {
	if( maplay.scaleX() < maxzoom && maplay.scaleY() < maxzoom){
	maplay.setScale({y: maplay.scaleY()+1,x: maplay.scaleX()+1});
	maplay.draw();
	minX=-maplay.scaleX()*maplay.getWidth()+stage.width();
	minY=-maplay.scaleY()*maplay.getHeight()+stage.height();
}
}

function zoom1()  {
	maplay.setScale({y: 1,x: 1});
	maplay.draw();
	minX=-maplay.scaleX()*maplay.getWidth()+stage.width();
	minY=-maplay.scaleY()*maplay.getHeight()+stage.height();
}

function zoomOut() {
	if( maplay.scaleX() > 1 && maplay.scaleY() > 1){
	maplay.setScale({y: maplay.scaleY()-1,x: maplay.scaleX()-1});
	minX=-maplay.scaleX()*maplay.getWidth()+stage.width();
	minY=-maplay.scaleY()*maplay.getHeight()+stage.height();
	maplay.setPosition({y: (minY+maxY)/2+maxY , x: (minX+maxX)/2+maxX});
	maplay.draw();
}
}

var wheelzoom = function(e) {
  var zoomAmount = e.wheelDeltaY;
  if (zoomAmount > 0)
  	zoomIn();
  if (zoomAmount < 0)
  	zoomOut();
  else
  	zoom1();
}

//LOAD EVERYTHING
loadResources(sources, buildStage);
