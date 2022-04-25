var pages = document.getElementById("family__content-media");    


document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/cats",
    {
        method: "GET",
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then( request => {
        request.json().then(function(data) {
            let cats = data['cats'];
            for (let id in cats){
                pages.innerHTML += `
                    <div class="family__content-block">
                    <img class="family__content-img"src="static/images/cats/` + cats[id]['path'] + `" alt="` + cats[id]['name'] + `">
                    <p>` + cats[id]['content'] + `</p>
                    </div>
                `;
            }
        });
    })
    .catch( error => {
        alert(error);
        console.error('error:', error);
    });
  
});