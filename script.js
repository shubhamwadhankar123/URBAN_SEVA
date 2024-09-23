function bookService(serviceName, serviceImage, serviceDescription, servicePrice) {
    // Store the selected service details in localStorage
    localStorage.setItem('selectedService', serviceName);
    localStorage.setItem('selectedServiceImage', serviceImage);
    localStorage.setItem('selectedServiceDescription', serviceDescription);
    localStorage.setItem('selectedServicePrice', servicePrice);

    // Redirect to location page
    window.location.href = 'location.html';
}

// Location form submission logic
document.getElementById('location-form')?.addEventListener('submit', function(e) {
    e.preventDefault();

    // Get the selected location details
    const country = document.getElementById('country').value;
    const state = document.getElementById('state').value;
    const district = document.getElementById('district').value;
    const area = document.getElementById('area').value;

    // Concatenate location details into a string
    const userLocation = `${area}, ${district}, ${state}, ${country}`;

    // Store the location in localStorage
    localStorage.setItem('userLocation', userLocation);

    // Redirect to service details page
    window.location.href = 'service-details.html';
});
