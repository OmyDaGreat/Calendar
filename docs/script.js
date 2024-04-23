// script.js
function fetchFestivals() {
    const month = document.getElementById('monthSelect').value;
    fetch('/.netlify/functions/getFestivals?month=' + month)
        .then(response => response.json())
        .then(data => {
            const festivalsList = document.getElementById('festivalsList');
            festivalsList.innerHTML = '';
            data.forEach(festival => {
                festivalsList.innerHTML += `<p>${festival.name}</p>`;
            });
        });
}
