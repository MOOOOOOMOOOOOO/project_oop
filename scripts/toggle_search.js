function toggle_search() {
    const searchBar = document.getElementById("searchBar")
    const searchInput = document.getElementById("search_str")

    console.log(searchBar)

    searchBar.style.display = "flex";
    searchInput.focus();
}

function toggle_search_off(){
    var searchBar = document.getElementById("searchBar")

    console.log(searchBar)

    searchBar.style.display = "none";
}
