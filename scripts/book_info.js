// script.js

function displayBookInfoAndNavigate(bookName) {
    console.log("start");

    // Fetch book information asynchronously
    fetch(`/book/${bookName}`)
    .then(response => response.json())
    .then(data => {
        // Store book information in sessionStorage
        sessionStorage.setItem('bookInfo', JSON.stringify(data));

        // Navigate to book_info.html
        window.location.href = "book_info.html";
    })
    .catch(error => {
        console.error('Error:', error);
    });
}