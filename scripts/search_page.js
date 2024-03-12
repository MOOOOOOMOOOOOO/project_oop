search();

var receivedString = getParams().data;
//  `<div class="search_result_container">
//                         <div class="image-container">
//                             <img src="../assets/covers_img/${book_name}.png" alt="../assets/covers_img/temp_cover.jpg">
//                         </div>
//                         <div class="book_content_container"><br>
//                             <p class="book_title">${book_name}</p>
//                             <p class="book_description">${pseudonym}</p>
//                             <p class="book_description">${genre}</p>
//                         </div>
//                     </div>`;

const close_tag = '</p><p class="description">นามปากกา</p><p class="description">หมวดหมู่</p><p class="description">อื่นๆ</p></div></div>'

const not_found = '<a class="not_found">ไม่พบรายการค้นหา</a>'
console.log(receivedString);
if (receivedString){
    search_by_string(receivedString);
    
}

function display_result(result){
    var book_name = result.book_name;
    var pseudonym = result.pseudonym;
    var genre = result.genre;
    var element = `<div class="search_result_container">
    <div class="image-container">
        <img src="../assets/covers_img/${book_name}.png" 
            onerror="this.onerror=null;this.src='../assets/covers_img/temp_cover.jpg';" 
            alt="../assets/covers_img/temp_cover.jpg">
    </div>
    <div class="book_content_container"><br>
        <p class="book_title">${book_name}</p>
        <p class="book_description">${pseudonym}</p>
        <p class="book_description">${genre}</p>
    </div>
</div>`;

    $('#search_result_page').append(element);
}


var current_data; 
var search_type = 0;

function select_type(num){
    search_type = num;
    var type = document.getElementsByClassName("search_type");
    for (let i = 0; i < type.length; i++) {
        type[i].style.borderBottom = "none";
    }
    type[search_type].style.borderBottom = "4px solid var(--main_color)";
    show_type(current_data);
}

function show_type(current_data){
    $('#search_result_page').empty();
    if (search_type == 0){
        display_all(current_data);
    }
    else if(search_type == 1){
        display_books();
    }
    else{
        display_pseudonyms();
    }
}

function search(){
    document.addEventListener('DOMContentLoaded', (event) => {
        document.getElementById("searchFormPage").addEventListener("submit", function (e) {
            e.preventDefault(); // Cancel the default action
            var search_str = document.getElementById('searchInputPage').value;
            fetch('/search_all/' + search_str, {
                method: 'GET',
            })
            .then(resp => resp.json())
            .then(data => {
                current_data = data;
                $('#search_result_page').empty();
                show_type(data);
            })
            .catch(error => {
                console.error(error);
            });
        });
    });
}

function search_by_string(search_str){
            fetch('/search_all/' + search_str, {
                method: 'GET',
            })
            .then(resp => resp.json())
            .then(data => {
                console.log(search_str);
                const search_input = document.getElementById("searchInputPage")
                search_input.value = search_str;
                current_data = data;
                $('#search_result_page').empty();
                show_type(data);
            })
            .catch(error => {
                console.error(error);
            });
}

function display_books(){
    if (current_data.book.length == 0) {
        display_not_found();
    }
    else{
        current_data.book.forEach(result => {
            display_result(result);
        });
    }   
}

function display_pseudonyms(){
    if (current_data.pseudonym.length == 0) {
        display_not_found();
    }
    else{
        current_data.pseudonym.forEach(result => {
            display_result(result);
        });
        console.log(not_found);
    }   
}

function display_not_found(){
    var element = not_found;
    $('#search_result_page').append(element);
}
function display_all(results) {
    if (results.book.length === 0 && results.pseudonym.length === 0) {
        display_not_found();
    } else {
        let search_names = [];

        if (results.book.length !== 0) {
            results.book.forEach(result => {
                display_result(result);
                search_names.push(result.book_name); // Use push to add elements to the array
                console.log(result.book_name);
            });
        }

        console.log(search_names);

        if (results.pseudonym.length !== 0) {
            results.pseudonym.forEach(result => {
                if (!search_names.includes(result.book_name)) {
                    display_result(result);
                }
            });
        }
    }
}



function getParams() {
    var params = {};
    var paramArray = window.location.search.substring(1).split('&');

    for (var i = 0; i < paramArray.length; i++) {
        var pair = paramArray[i].split('=');
        params[pair[0]] = decodeURIComponent(pair[1]);
    }

    return params;
}