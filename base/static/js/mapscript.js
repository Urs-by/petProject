ymaps.ready(init);



function init() {
    var geolocation = ymaps.geolocation,
        myMap = new ymaps.Map('map', {
            center: [55, 34],
            zoom: 10
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

    var myPlacemark;
    myMap.events.add('click', function (e) {
        var coords = e.get('coords');

        if (myPlacemark) {

            myPlacemark.geometry.setCoordinates(coords);
        } else {
            myPlacemark = new ymaps.Placemark(coords, {}, {
                iconLayout: 'default#image',
                iconImageHref: "static/img/marker5.png", // Кастомный макет иконки в формате PNG
                iconImageSize: [35, 60], // Размер иконки
                iconImageOffset: [-25, -25], // Смещение иконки
                draggable: true
            });

            myMap.geoObjects.add(myPlacemark);
        }
    });
}



