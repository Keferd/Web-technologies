var myMap;
ymaps.ready(init); // Ожидание загрузки API с сервера Яндекса
function init () {
  myMap = new ymaps.Map("contact-us__map", {
    center: [54.724497, 55.940589], // Координаты центра карты
    zoom: 10 // Zoom
  });
}
