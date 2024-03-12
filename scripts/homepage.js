let toggle_dd_status = false;

function toggle_user_icon_drop_down(){
    toggle_search_off();
    toggle_dd_status = !toggle_dd_status;
    const dropdown = document.getElementById('home_dd_container');

    if (toggle_dd_status){
        dropdown.style.display = "block";
    }
    else{
        dropdown.style.display = "none";
    }
    
}

function go_to_my_page(){
    window.location.href = 'myPage.html';
}

function go_to_my_profile(){
    window.location.href = 'myPage.html';
}

function go_to_buy_coin(){
    window.location.href = 'payment.html';
}

function go_to_my_reading(){
    window.location.href = 'myPage.html';
}

function go_to_my_writing(){
    window.location.href = 'myPage.html';
}

function go_to_my_coin_transac(){
    window.location.href = 'myPage.html';
}

function go_to_my_chapter_transac(){
    window.location.href = 'myPage.html';
}

function go_to_homepage(){
    window.location.href = 'homepage.html';
}