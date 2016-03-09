// https://developers.google.com/maps/documentation/javascript/examples/
function initMap() {
  var customMapType = new google.maps.StyledMapType([
      {
      stylers: [
        { hue: "#FA82CC" },
        { saturation: 0 }
      ]
    },
    {
      featureType: "road",
      elementType: "geometry",
      stylers: [
        { lightness: 100 },
        { visibility: "simplified" }
      ]
    }
    //{
    //  featureType: "road",
    //  elementType: "labels",
    //  stylers: [
    //    { visibility: "off" }
    //  ]
    //
    //}
    ], {
      name: 'Unify Style'
  });

  var image = new google.maps.MarkerImage(
  	'{% static "Images/marker.png" %}',
  	new google.maps.Size(48,54),
  	new google.maps.Point(0,0),
  	new google.maps.Point(24,54)
  	);

  var customMapTypeId = 'custom_style';

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 16,
    scrollwheel: false,
    center: {lat: 25.106111, lng: 121.532099},  // Brooklyn.
    mapTypeControlOptions: {
      mapTypeIds: [google.maps.MapTypeId.ROADMAP, customMapTypeId]
    }
  });

  var infowindow = new google.maps.InfoWindow;
  infowindow.setContent('<b>蘇惠珍皮膚科診所</b>');

  var marker = new google.maps.Marker({
  	map: map,
  	clickable: false,

  	position: {lat: 25.106111, lng: 121.532099}
  });

  map.mapTypes.set(customMapTypeId, customMapType);
  map.setMapTypeId(customMapTypeId);

}
