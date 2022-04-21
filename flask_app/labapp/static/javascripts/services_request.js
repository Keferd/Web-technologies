var pages = document.getElementById("main__two-column");    

// this.container = document.createElement('div');
// document.body.appendChild(this.container);
// pages.insertAdjacentElement('beforeend', this.container);

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
                let newpage = document.createElement('div');
                newpage.className += " main__two-column__element";
                document.body.appendChild(newpage);
                newpage.innerHTML = `
                    <div class="main__two-column__element__image">
                        <img src="static/images/our-services/` + services[id]['path'] + `">
                    </div>
                    <h3>` + services[id]['name'] + `</h3>
                    <p>` + services[id]['content'] + `</p>
                `;
                pages.insertAdjacentElement('beforeend', newpage);
            }

            $(document).ready(function() {
                $(".main__two-column__element p").hide();
                });
                $(".main__two-column__element p").click(function () {
                $(this).hide("slow");
                });
                $(".main__two-column__element h3").click(function () {
                $(this).next("p").show("slow");
                });
                
                $(".main__two-column__element img").hover(
                                function() {
                                    $(this).animate({
                                        width: "36px",
                                        height: "36px",
                                        borderRadius: "2%"
                                    }, "slow");
                                }, function() {
                                    $(this).animate({
                                        width: "32px",
                                        height: "32px",
                                        borderRadius: "10%"
                                    }, "slow");
                                });
                
                
        });
    })
    .catch( error => {
        alert(error);
        console.error('error:', error);
    });
  
});