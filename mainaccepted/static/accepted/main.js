var mymap = L.map("mapid").setView([42.6593, 20.2887], 14);

    L.tileLayer(
      "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
      {
        attribution:
          'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: "mapbox/streets-v11",
        accessToken: "your.mapbox.access.token"
      }
    ).addTo(mymap);

    const attribution =
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
    const tileUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
    const tiles = L.tileLayer(tileUrl, { attribution });
    tiles.addTo(mymap);

    var marker = L.marker([42.6612, 20.2883]).addTo(mymap);
    var marker1 = L.marker([42.6591, 20.2895]).addTo(mymap);
    var marker2 = L.marker([42.6624, 20.2838]).addTo(mymap);

    marker
      .bindPopup(
        "<b>Seraphine Plaza</b><br><a id='klikopointer' data-toggle='modal' data-target='#myModal'> Kliko ketu per me shume </a>"
      )
      .openPopup();
    marker1
      .bindPopup(
        "<b>Hotel Dukagjini</b><br><a id='klikopointer' data-toggle='modal' data-target='#myModal2'> Kliko ketu per me shume </a>"
      )
      .openPopup();
    marker2
      .bindPopup(
        "<b>Shkolla Asdreni - Peje</b><br><a id='klikopointer' data-toggle='modal' data-target='#myModal1'> Kliko ketu per me shume </a>"
      )
      .openPopup();
