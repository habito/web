function initialize() {
	var mapOptions = {
		center: new google.maps.LatLng(37.8724523, -122.2590298),
		zoom: 16
	};
	var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
}

google.maps.event.addDomListener(window, 'load', initialize);