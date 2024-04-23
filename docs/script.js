document.getElementById('calculateButton').addEventListener('click', function() {
    var selectedDate = document.getElementById('dateInput').value;
    var date = new Date(selectedDate);
    var panchang = new Panchang(date);
    panchang.calculate();
    displayPanchangDetails(panchang);
});

function displayPanchangDetails(panchang) {
    var detailsDiv = document.getElementById('panchangDetails');
    detailsDiv.innerHTML = JSON.stringify(panchang, null, 2);
}
