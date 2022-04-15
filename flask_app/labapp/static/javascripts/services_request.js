var pages = document.getElementById("main__two-column");    

this.container = document.createElement('div');
document.body.appendChild(this.container);
pages.insertAdjacentElement('beforeend', this.container);

document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/services",
    {
        method: "GET",
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then( request => {
        
        request.json().then(function(data) {
            let services = data['services'];
            for (let id in services){
                this.container.innerHTML += `
                    <div class="main__two-column__element">
                    <div class="main__two-column__element__image">
                        <img src="static/images/our-services/` + services[id]['path'] + `">
                    </div>
                    <h3>` + services[id]['name'] + `</h3>
                    <p>` + services[id]['content'] + `</p>
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