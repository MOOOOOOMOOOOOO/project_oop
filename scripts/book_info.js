// script.js
document.addEventListener('DOMContentLoaded', function() {

    function displayBookInfoAndNavigate(bookName) {
        console.log("start");

        // Fetch book information asynchronously
        fetch(`/book/${bookName}`)
        .then(response => response.json())
        .then(data => {
            console.log("oooo")
            // Store book information in sessionStorage
            sessionStorage.setItem('bookInfo', JSON.stringify(data));

            console.log(sessionStorage.getItem('bookInfo'))
            // Navigate to book_info.html
            window.location.href = "book_info.html";

            //DOM
            const bookInfo = JSON.parse(sessionStorage.getItem('bookInfo'));

            console.log("Retrieved book information:", data);

            // Check if the parsed object has the expected properties
            if (bookInfo && bookInfo.genre && bookInfo.name && bookInfo.pseudonym && bookInfo.prologue && bookInfo.writer_name && bookInfo.date_time) {
                // Display book information in the HTML page
                // document.getElementById('book').textContent = bookInfo;
                document.getElementById('genre').textContent = bookInfo.genre;
                document.getElementById('bookName').textContent = bookInfo.name;
                document.getElementById('prologueInfo').textContent = bookInfo.prologue;
                document.getElementById('prologueDisplay').textContent = bookInfo.prologue;
                document.getElementById('pseudonymInfo').textContent = bookInfo.pseudonym;
                document.getElementById('pseudonymDisplay').textContent = bookInfo.pseudonym;
                document.getElementById('writer_username').textContent = bookInfo.writer_name;
                document.getElementById('date_time').textContent = bookInfo.date_time;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
        
    }
});