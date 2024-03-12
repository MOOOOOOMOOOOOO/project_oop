var dataToSend = {
    key1: 'value1',
    key2: 'value2'
};

// Convert data to URL-encoded string
var queryString = Object.keys(dataToSend).map(key => key + '=' + encodeURIComponent(dataToSend[key])).join('&');

// Redirect to the receiving page with the data in the URL
window.location.href = 'receiving_page.html?' + queryString;