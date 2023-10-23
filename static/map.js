function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 0, lng: 0 },
        zoom: 2
    });

    // Отримання місць з Django моделі і додавання їх на мапу
    var places = [{% for place in places %}
        {
            name: "{{ place.name }}",
            lat: {{ place.lat }},
            lng: {{ place.lng }},
        },
        {% endfor %}];

    for (var i = 0; i < places.length; i++) {
        var place = places[i];
        var marker = new google.maps.Marker({
            position: { lat: place.lat, lng: place.lng },
            map: map,
            title: place.name
        });
    }
}
