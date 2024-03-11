document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById("searchForm").addEventListener("submit", function (e) {
      e.preventDefault() // Cancel the default action
        var search_str = document.getElementById('search_str').value;
        fetch('/search_all/' + search_str, {
            method: 'GET',
            })
            .then(resp => resp.json()) // or, resp.json(), etc.
            .then(data => {
                console.log(data.Search)
                $('#search_result').empty();
                $('#search_result').append('<h3> Reader :</h3>');
                if (typeof data.Search.Reader !== 'string') {
                    console.log("check")
                    $.each(data.Search.Reader, function(index, reader){
                        $('#search_result').append('<ul>'+ reader + '</ul>');
                    })
                }
                else{
                    $('#search_result').append('<ul>'+ data.Search.Reader + '</ul>');
                }

                $('#search_result').append('<h3> Writer :</h3>');
                if (typeof data.Search.Writer !== 'string') {
                    $.each(data.Search.Writer, function(index, writer){
                        $('#search_result').append('<ul>'+ writer + '</ul>');
                    })
                }
                else{
                    $('#search_result').append('<ul>'+ data.Search.Writer + '</ul>');
                }

                $('#search_result').append('<h3> Book :</h3>');
                if (typeof data.Search.Book !== 'string') {
                    $.each(data.Search.Book, function(index, book){
                        $('#search_result').append('<ul>'+ book + '</ul>');
                    })
                }
                else{
                    $('#search_result').append('<ul>'+ data.Search.Book + '</ul>');
                }
                // document.getElementById("search_result").innerHTML = data.Search.Reader;
            })
            .catch(error => {
            console.error(error);
        });
    });
});