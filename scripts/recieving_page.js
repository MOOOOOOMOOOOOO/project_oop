function getParams() {
    var params = {};
    var paramArray = window.location.search.substring(1).split('&');

    for (var i = 0; i < paramArray.length; i++) {
        var pair = paramArray[i].split('=');
        params[pair[0]] = decodeURIComponent(pair[1]);
    }

    return params;
}

// Get the data from the URL
var receivedData = getParams();

// Example: Log received data
console.log('Received Data:', receivedData);
