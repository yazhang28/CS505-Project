$(document).ready(function() {

  // if (!$("#mapid").size()) {
  //     console.log("here"); 
  //   } else { 
  	initMap(42.312780, -71.099737, 12); 
    // }

});

function initMap() {

  window.map = L.map('mapid', { 
    center:[arguments[0], arguments[1]], 
    zoom:arguments[2],
  });
  mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';

  var friday_morning_layer = L.geoJson(frid_morn, {style: style}).addTo(map);
  var friday_afternoon_layer = L.geoJson(frid_afternoon, {style: style})
  var friday_evening_layer = L.geoJson(frid_evening, {style: style})
  var friday_night_layer = L.geoJson(frid_night, {style: style})

  var baseLayers = {
    "Friday Morning": friday_morning_layer,
    "Friday Afternoon": friday_afternoon_layer,
    "Friday Evening": friday_evening_layer,
    "Friday Night": friday_night_layer
  };

  L.control.layers(baseLayers).addTo(map);

  L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  	// window.mapMarkers = [];
  	// var marker = L.marker([arguments[0], arguments[1]])
  	// mapMarkers.push(marker);
  	// mapMarkers[0].addTo(map).bindPopup("This is center of the map.");

  function getColor(d) {
    return d == "Larceny"  ? '#4E5474' : 
           d == "Manslaughter"  ? '#42E45C' : 
           d == "Rape/Sexual Assault"  ? '#878F42' : 
           d == "Assault/Battery"  ? '#2C4597' : 
           d == "Kidnapping"  ? '#B36F58' : 
           d == "Burglary"  ? '#590E13' : 
           d == "Bombs/Explosives"  ? '#3F4B47' : 
           d == "Harrassment"  ? '#92C2D8' : 
           d == "Weapons"  ? '#D4CA2A' : 
           d == "Arson" ? '#FEF6E9' : 
           d == "Breaking/Entering" ? '#523724' : 
           d == "Child Abuse/Endangerment" ? '#C6BAA4' :
           d == "Disorderly Conduct" ? '#FBDFB0' : 
           d == "Public Drinking" ? '#C46537' : 
           d == "Possession" ? '#587367' :
           d == "Robbery" ? '#AE42E4' :
                       '#FFEDA0';
  }

  function style(feature) {
      return {
          fillColor: getColor(feature.properties.crime),
          weight: 2,
          opacity: 1,
          color: 'white',
          dashArray: '3',
          fillOpacity: 0.7
      };
  }

  var legend = L.control({position: 'bottomright'});

  legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
      grades = ["Larceny","Manslaughter","Rape/Sexual Assault","Assault/Battery","Kidnapping","Burglary","Bombs/Explosives","Harrassment","Weapons","Arson","Breaking/Entering","Child Abuse/Endangerment","Disorderly Conduct","Public Drinking","Possession","Robbery"],
      labels = [],
      from, to;

    for (var i = 0; i < grades.length; i++) {
      from = grades[i];
      labels.push(
        '<i style="background:' + getColor(from) + '"></i> ' +
        from);
    }

    div.innerHTML = labels.join('<br>');
    return div;
  };
  /* Initialize the SVG layer */
	map._initPathRoot()
  legend.addTo(map);
}