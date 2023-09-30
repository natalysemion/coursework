// Отримати ідентифікатор артиста з запиту до вашого сервера
const artistId = '61mjebytLODtxAOS9ULCmb';

// Функція для отримання та відображення найкращого треку
function displayTopTrack() {
    fetch(`/get_top_track?artist_id=${artistId}`, {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer {get_token()}'
        }
    })
    .then(response => response.json())
    .then(data => {
        const topTrackContainer = document.getElementById('top-track');
        const topTrack = data.tracks[0]; // Перший трек в списку найкращих
        const trackName = topTrack.name;
        const artistName = topTrack.artists[0].name;
        const imageUrl = topTrack.album.images[0].url;

        // Відобразити інформацію про найкращий трек
        const trackElement = document.createElement('div');
        trackElement.innerHTML = `
            <h2>Найкращий трек:</h2>
            <p>Назва: ${trackName}</p>
            <p>Виконавець: ${artistName}</p>
            <img src="${imageUrl}" alt="${trackName} cover">
        `;
        topTrackContainer.appendChild(trackElement);
    })
    .catch(error => console.error('Помилка:', error));

}

// Викликаємо функцію для відображення найкращого треку при завантаженні сторінки
displayTopTrack();
