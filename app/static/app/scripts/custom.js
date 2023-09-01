// custom.js

// Handle Pickup Location and Destination geolocation
document.getElementById("pickup-locate-btn").addEventListener("click", function () {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            // Update the input field value with the geolocation coordinates
            document.getElementById("id_pickup_location").value = latitude + ", " + longitude;
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
            // Update the input field value with the geolocation coordinates
            document.getElementById("id_destination").value = latitude + ", " + longitude;
        });
    } else {
        alert("Geolocation is not available.");
    }
});
$("#zip-form").submit(function (e) {
    e.preventDefault();

    var zipCode = $("input[name='zip']").val();

    $.ajax({
        type: "GET",
        url: "{% url 'get_address' %}",
        data: { zip: zipCode },
        success: function (data) {
            $("#address-result").text(data.address);
        },
        error: function () {
            $("#address-result").text("Error fetching address.");
        }
    });
});
