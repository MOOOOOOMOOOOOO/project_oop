var view_type = 0;
let current_data;
search_my_page();
$('.my_page_show_view_type').empty();


const not_found_html = '<a class="not_found">ไม่พบข้อมูล</a>'
const pseudonym_html = '<a class="not_found">นามปากกา</a>'
const show_book_html = `<div class="search_result_container">
                        <div class="image-container">
                            <img src="../assets/covers_img/${book_name}.png" alt="../assets/covers_img/temp_cover.jpg">
                        </div>
                        <div class="book_content_container"><br>
                            <p class="book_title">${book_name}</p>
                            <p class="book_description">${pseudonym}</p>
                            <p class="book_description">${genre}</p>
                        </div>
                    </div>`;

function my_page_select_view_type(num){
    type = num;
    var view_type = document.getElementsByClassName("my_page_view_type");
    for (let i = 0; i < view_type.length; i++) {
        view_type[i].style.borderBottom = "none";
    }
    view_type[type].style.borderBottom = "4px solid var(--main_color)";
    my_page_show_type();
}

function my_page_show_type(){
    $('#my_page_show_view_type').empty();
    if (search_type == 0){
        display_writings();;
    }
    // else if(search_type == 1){
    //     display_pseudonyms();
    // }
    // else{
    //     display_commentss();
    // }
}

// ชั่วคราววว
function search_my_page(){
    document.addEventListener('DOMContentLoaded', (event) => {
        document.getElementById("my_page_search_username").addEventListener("submit", function (e) {
            e.preventDefault(); // Cancel the default action
            var username_str = document.getElementById('search_input_my_page').value;
            fetch('/my_page/' + username_str, {
                method: 'GET',
            })
            .then(resp => resp.json())
            .then(data => {
                console.log(data);
                current_data = data;
                $('my_page_show_view_type').empty();
                display_my_page();
                display_writings();
            })
            .catch(error => {
                console.error(error);
            });
        });
    });
}

function display_my_page(){
    for (var key in current_data) {
        var element = document.getElementById('my_page_' + key);
        if (element) {
            var placeholder = '{' + key + '}';
            element.innerHTML = element.innerHTML.replace(placeholder, current_data[key]);
        }
    }
}

function display_writings(){
    current_data.writings.forEach(result => {
        display_writing_result(result);
    });
}

function display_writing_result(result){
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
    $('#my_page_show_view_type').append(element);
}