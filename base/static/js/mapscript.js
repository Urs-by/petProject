// отрисовываем карту по умолчанию
ymaps.ready(function () {
    var geolocation = ymaps.geolocation,
        myMap = new ymaps.Map('map', {
            center: [55, 34],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        });
    // отрисовка карты местности по текущему местораположению (по ip )
    geolocation.get({
        autoReverseGeocode: false,
        mapStateAutoApply: true
    }).then(function (result) {
        // Если браузер не поддерживает эту функциональность, метка не будет добавлена на карту.
        result.geoObjects.options.set('preset', 'islands#blueCircleIcon');
        myMap.geoObjects.add(result.geoObjects);
    });


    // Получаем данные из view  data
    data.forEach(function (shop) {
        var placemark = new ymaps.Placemark([shop.latitude, shop.longitude], {

            hintContent: shop.name,
            balloonContent: 'Rating: ' + shop.rating.toFixed(2)
        }, {
            //    cтилизуем иконку
            iconLayout: 'default#image',
            iconImageHref: "static/img/marker5.png", // Кастомный макет иконки в формате PNG
            iconImageSize: [35, 60], // Размер иконки
            iconImageOffset: [-25, -25], // Смещение иконки
            draggable: true
        });
        myMap.geoObjects.add(placemark);
    });
});


