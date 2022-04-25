var pages = document.getElementById("blog__pages");


document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/jokes",
    {
        method: "GET",
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then( request => {
        
        request.json().then(function(data) {
            let joke = data['jokes'];
            for (let id in joke){
                pages.innerHTML += `
                    <div class="blog__content-block">
                        <div class="blog__img-container">
                            <img class="blog__content-image" src="static/images/blog/Gregory.png" alt="Shlepa">
                        </div>
                        <button onclick="jokeFavoriteAdd(` + joke[id]['id'] + `)">Добавить</button>
                        <p style="font-weight:bold;">` + joke[id]['name'] + `</p>
                        <br>
                        <p>` + joke[id]['content'] + `
                        </p>
                        <br>
                    </div>  
                `;
            }
            pages.innerHTML += `
                <script src="static/javascripts/jokeFavoriteAdd.js"></script>
            `
        });
    })
    .catch( error => {
        alert(error);
        console.error('error:', error);
    });
  
});
