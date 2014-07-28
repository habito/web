function loadCoverPic(container, static_url) {
	var photos = ['snow', 'balloon', 'craft', 'gg', 'narrow', 'office_bw', 'water'];
	var randomImage = photos[Math.floor(Math.random() * photos.length)];
	var imageURL = 'website/img/banner/' + randomImage + '_low_opa_compressed.jpg';
	$(container).css("background", "url(" + static_url + imageURL + ") no-repeat center center fixed");
	$(container).css("background-size", "cover");
	$(container).css("-webkit-background-size", "cover");
	$(container).css("-moz-background-size", "cover");
	$(container).css("-o-background-size", "cover");
}