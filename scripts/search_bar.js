search_from_home();
function search_from_home(){
    document.addEventListener('DOMContentLoaded', (event) => {
        document.getElementById("searchForm").addEventListener("submit", function (e) {
            e.preventDefault(); // Cancel the default action
            var search_str = document.getElementById('search_str').value;
            var queryString = 'data=' + encodeURIComponent(search_str);
            window.location.href = 'search_page.html?' + queryString;
        });
    });
}