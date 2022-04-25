function jokeFavoriteAdd(id) {
    console.log("Избранное")
    fetch("/api/joke/favorite/" + id,
        {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then( response => {
            response.json().then(function(data) {
                console.log(data)
                alert(data['message']);
            });
        })
        .catch( error => {
            alert(error);
            console.error('error:', error);
        });
}