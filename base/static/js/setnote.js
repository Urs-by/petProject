ymaps.ready(init);

function init() {
    //  определяем местоположение по ip
    var geolocation = ymaps.geolocation,
        myMap = new ymaps.Map('map', {
            center: [55, 34],
            zoom: 5
        }, {
            searchControlProvider: 'yandex#search'
        });

    geolocation.get({
        autoReverseGeocode: false,
        mapStateAutoApply: true
    }).then(function (result) {
        // Если браузер не поддерживает эту функциональность, метка не будет добавлена на карту.
        result.geoObjects.options.set('preset', 'islands#blueCircleIcon');
        myMap.geoObjects.add(result.geoObjects);
    });


    var customMarker = new ymaps.Placemark(myMap.getCenter(), {}, {
        iconLayout: 'default#image',
        iconImageHref: '/static/img/marker5.png',
        iconImageSize: [30, 42],
        iconImageOffset: [-15, -42]
    });

    myMap.geoObjects.add(customMarker);

    myMap.events.add('click', function (e) {
        var coords = e.get('coords');
        document.getElementById('id_latitude').value = coords[0].toPrecision(6);
        document.getElementById('id_longitude').value = coords[1].toPrecision(6);
        customMarker.geometry.setCoordinates(coords);

        ymaps.geocode(coords).then(function (res) {
            var firstGeoObject = res.geoObjects.get(0);

            var address = firstGeoObject.getAddressLine();
            var addressComponents = firstGeoObject.properties.get('metaDataProperty.GeocoderMetaData.Address');

            var city = addressComponents.Components.find(component => component.kind === 'locality').name;
            var street = addressComponents.Components.find(component => component.kind === 'street').name;

            document.getElementById('id_city').value = city;
            document.getElementById('id_street').value = street;
        });




    });
}
