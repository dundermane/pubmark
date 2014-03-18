//Define the Stage (canvas)
var stage = new Kinetic.Stage({
  container: 'content2',
  width: document.getElementById('content2').offsetWidth,
  height: document.getElementById('content2').offsetWidth
});

var maxzoom = 5;

//define the "zoom in" button
var rect1 = new Kinetic.Rect({
  x: 0,
  y: 0,
	height: 30,
	width: 30,
  fill: 'white',
  stroke: '#CCC',
  strokeWidth: 2
});

//define the "zoom out" button
var rect2 = new Kinetic.Rect({
  x: 0,
  y: 40,
	height: 30,
	width: 30,
  fill: 'white',
  stroke: '#CCC',
  strokeWidth: 2
});

var line1 = new Kinetic.Line({
  points: [15, 8, 15, 22],
  stroke: '#CCC',
  strokeWidth: 2,
  lineCap: 'round',
  lineJoin: 'round'
});

var line2 = new Kinetic.Line({
  points: [8, 15, 22, 15],
  stroke: '#CCC',
  strokeWidth: 2,
  lineCap: 'round',
  lineJoin: 'round'
});

var line3 = new Kinetic.Line({
  points: [8, 55, 22, 55],
  stroke: '#CCC',
  strokeWidth: 2,
  lineCap: 'round',
  lineJoin: 'round'
});

var zin_button = new Kinetic.Group({
  x: 10,
  y: 10
});

var zout_button = new Kinetic.Group({
  x: 10,
  y: 10
});

zin_button.add(rect1);
zin_button.add(line1);
zin_button.add(line2);
zout_button.add(rect2);
zout_button.add(line3);


var mapObj = new Image();
mapObj.onload = function() {
	//Define the Map
  var map = new Kinetic.Image({
    x: 0,
    y: 0,
    image: mapObj,
    width: 400,
    height: 400
  });
  maplay.setWidth(map.getWidth());
  maplay.setHeight(map.getHeight());
  
	// add the objects to the layers
	maplay.add(map);
	fore.add(zin_button);
	fore.add(zout_button);

	
	// add the layers to the stage
	stage.add(maplay);
	stage.add(fore);
  
};
mapObj.src = "images/pubmark_map.png";


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


//define the dragging bounds of maplay
var minX=-maplay.scaleX()*maplay.getWidth()+stage.width();
var maxX=0;
var minY=-maplay.scaleY()*maplay.getHeight()+stage.height();
var maxY=0;


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

var wheelzoom = function(e) {
  var zoomAmount = e.wheelDeltaY;
  if (zoomAmount > 0)
  	zoomIn();
  if (zoomAmount < 0)
  	zoomOut();
  else
  	zoom1();
}


document.addEventListener("mousewheel", wheelzoom, false)
