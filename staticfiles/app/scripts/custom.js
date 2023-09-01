// custom.js

// Handle Pickup Location and Destination geolocation
document.getElementById("pickup-locate-btn").addEventListener("click", function () {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            // Update the input field value or perform other actions
        });
    } else {
        alert("Geolocation is not available.");
    }
});

document.getElementById("destination-locate-btn").addEventListener("click", function () {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            // Update the input field value or perform other actions
        });
    } else {
        alert("Geolocation is not available.");
    }
});
