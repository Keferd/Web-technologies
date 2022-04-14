/*
Реализация AJAX с помощью асинхронного метода fetch. Современный вариант реализации AJAX.
*/

var sendbtn = document.querySelector(".contact-us__input-submit");    // выбираем DOM-елемент (кнопку)

// Привязываем к элементу обработчик события "click"
sendbtn.addEventListener("click", function (e) {
    /* Инструкция preventDefault позволяет переопределить стандартное поведение браузера,
    если ее убрать, то браузер по-умолчанию обновит страницу после отправки данных формы */
    //e.preventDefault();
    // Получаем данные полей формы
    let fullname= document.getElementsByName("fullname")[0].value;
    let email = document.getElementsByName("email")[0].value;
    let message = document.getElementsByName("message")[0].value;
    
    // Преобразуем полученные данные в JSON
    let formdata = JSON.stringify({ fullname: fullname, email: email, message: message});
    console.log(formdata);

    formparse = JSON.parse(formdata);
    let full = formparse["fullname"];
    console.log(full);
    if (formparse["fullname"] != "" && formparse["email"] != "") {
        // Отправляем запрос через fetch (необходимо выставить соответствующий заголовок (headers)!)
        fetch("/api/contact_request",
        {
            method: "POST",
            body: formdata,
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then( response => {
            // fetch в случае успешной отправки возвращает Promise, содержащий response объект (ответ на запрос)
            // Возвращаем json-объект из response и получаем данные из поля message
            response.json().then(function(data) {
                console.log(data)
                // let statfield = document.getElementById("statusfield");
                // statfield.textContent = data.message;
                //Сontact_UsConfirmDialog(data['message'])
                alert(data['message']);
                //statfield.textContent.bold();
                //alert(data.message);
            });
        })
        .catch( error => {
            alert(error);
            console.error('error:', error);
        });
    }
});
