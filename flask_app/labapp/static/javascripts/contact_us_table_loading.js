var pages = document.getElementById("contact-us__table");    


document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/contactrequest/userid",
    {
        method: "GET",
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then( request => {
        request.json().then(function(data) {
            let requests = data['contactrequests'];
            for (let id in requests){
                pages.innerHTML += `
                    <tr>
                        <td>` + requests[id]['fullname'] + `</td>
                        <td>` + requests[id]['email'] + `</td>
                        <td>` + requests[id]['message'] + `</td>
                        <td>` + requests[id]['cratedAt'] + `</td>
                        <td>` + requests[id]['updatedAt'] + `</td>
                    </tr>
                `;
            }
        });
    })
    .catch( error => {
        alert(error);
        console.error('error:', error);
    });
  
});