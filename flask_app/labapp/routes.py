# -*- coding: utf-8 -*-
# Подключаем объект приложения Flask из __init__.py
from . import dbservice
from labapp import app, db
# Подключаем библиотеку для "рендеринга" html-шаблонов из папки templates
from flask import render_template, make_response, request, Response, jsonify, json

import json


"""

    Модуль регистрации маршрутов для запросов к серверу, т.е.
    здесь реализуется обработка запросов при переходе пользователя на определенные адреса веб-приложения

"""

# Обработка запроса к индексной странице
@app.route('/')
@app.route('/index')
def index():
    # "рендеринг" (т.е. вставка динамически изменяемых данных) index.html и возвращение готовой страницы
    return render_template('index.html', title='Главная', pname='HOME')

# Обработка запроса к странице contact-us.html
@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html', title='Контакты', pname='CONTACT')

# Обработка запроса к странице blog.html
@app.route('/blog')
def blog():
    return render_template('blog.html', title='Анекдоты', pname='BLOG')

# Обработка запроса к странице family.html
@app.route('/family')
def family():
    return render_template('family.html', title='Семья', pname='PORTFOLIO')

# Обработка запроса к странице our-services.html
@app.route('/our-services')
def our_services():
    return render_template('our-services.html', title='Сервисы', pname='SERVICES')

# Обработка запроса к странице team.html
@app.route('/team')
def team():
    return render_template('team.html', title='Команда', pname='TEAM')

# Обработка GET-запроса на все jokes
@app.route('/api/jokes', methods=['GET'])
def get_jokes():
    jokes = dbservice.get_jokes_all()
    return json_response(jokes)

# Обработка GET-запроса на jokes по id
@app.route('/api/joke/<int:id>', methods=['GET'])
def get_joke(id):
    joke = dbservice.get_joke_by_id(id)
    return json_response(joke)

# Обработка POST-запроса на jokes по id
@app.route('/api/joke', methods=['POST'])
def post_joke():
    if not request.json or not 'name' in request.json or not 'content' in request.json:
        return bad_request()
    else:
        response = dbservice.create_joke(request.json)
        return json_response(response)

# Обработка PUT-запроса на jokes по id
@app.route('/api/joke/<int:id>', methods=['PUT'])
def update_joke(id):
    if not request.json or not 'name' in request.json or not 'content' in request.json:
        return bad_request()
    else:
        response = dbservice.update_contact_req_by_id(id, request.json)
        return json_response(response)

# Обработка DELETE-запроса на jokes по id
@app.route('/api/joke/<int:id>', methods=['DELETE'])
def delete_joke(id):
    joke = dbservice.delete_joke_by_id(id)
    return json_response(joke)

# Обработка GET-запроса на все cats
@app.route('/api/cats', methods=['GET'])
def get_cats():
    cats = dbservice.get_cats_all()
    return json_response(cats)

# Обработка GET-запроса на все services
@app.route('/api/services', methods=['GET'])
def get_services():
    services = dbservice.get_services_all()
    return json_response(services)

# Обработка POST-запроса для демонстрации AJAX
@app.route('/api/contactrequest', methods=['POST'])
def post_contact():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в этом объекте нет, например, обязательного поля 'firstname'
    if not request.json or not 'firstname' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе отправляем json-ответ
    else:
        msg = request.json['firstname'] + ", ваш запрос получен !"
        return json_response({ 'message': msg })

@app.route('/api/contact_request', methods=['POST'])
def post_contact_r():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в этом объекте нет, например, обязательного поля 'firstname'
    if not request.json or not 'fullname' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе отправляем json-ответ
    else:
        response = dbservice.create_contact_req(request.json)
        return json_response(response)

@app.route('/api/contact-request/<int:id>', methods=['PUT'])
# Обработка запроса на обновление записи в БД
def update_contact_req_by_id(id):
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в данных нет обязательного поля 'reqtext'
    if not request.json or not 'reqtext' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе обновляем запись в БД и отправляем json-ответ
    else:
        response = dbservice.update_contact_req_by_id(id, request.json)
        return json_response(response)


@app.route('/api/contact-request/<int:id>', methods=['DELETE'])
# Обработка запроса на удаление записи в БД по id
def delete_contact_req_by_id(id):
    response = dbservice.delete_contact_req_by_id(id)
    return json_response(response)

@app.route('/api/contact-request/<date>', methods=['DELETE'])
# Обработка запроса на удаление записи в БД по дате
def delete_contact_req_by_date(date):
    response = dbservice.delete_contact_req_by_date(date)
    return json_response(response)

@app.route('/api/jokes/copy', methods=['POST'])
def copy_old_to_jokes():
    jokes = dbservice.get_jokes_old_all()
    for item in jokes:
        dbservice.create_joke(item)
    return json_response(jokes)

"""

    Реализация response-методов, возвращающих клиенту стандартные коды протокола HTTP

"""

# Возврат html-страницы с кодом 404 (Не найдено)
@app.route('/notfound')
def not_found_html():
    return render_template('404.html', title='404', err={ 'error': 'Not found', 'code': 404 })

# Формирование json-ответа. Если в метод передается только data (dict-объект), то по-умолчанию устанавливаем код возврата code = 200
# В Flask есть встроенный метод jsonify(dict), который также реализует данный метод (см. пример метода not_found())
def json_response(data, code=200):
    return Response(status=code, mimetype="application/json", response=json.dumps(data))

# Пример формирования json-ответа с использованием встроенного метода jsonify()
# Обработка ошибки 404 протокола HTTP (Данные/страница не найдены)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)

# Обработка ошибки 400 протокола HTTP (Неверный запрос)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)


