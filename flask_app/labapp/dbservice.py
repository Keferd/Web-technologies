from sqlalchemy import true
from labapp import db
from datetime import datetime
from flask import session, make_response, redirect, url_for, jsonify
import bcrypt


"""
    В данном модуле реализуются CRUD-методы для работы с БД.
    Если в вашем приложении используется несколько сущностей (таблиц) в БД, то хорошей практикой 
    будет являться реализация ОТДЕЛЬНЫХ модулей с CRUD-операциями для каждой таблицы, при этом 
    данные модули лучше группировать в отдельном пакете Python, т.е. создавать папку с файлом __init__.py
"""


"""


-------------------------------------------- JOKES_FAVORITES --------------------------------------------


"""



# Получаем список всех запросов jokes
def get_jokes_favorites(id):
    result = []    
    rows = db.session.execute(f"SELECT * FROM jokes_favorites WHERE loginId='{id}'").fetchall()
    for row in rows:
        result.append(dict(row))
    return {'favorites': result}

# Добавляем строку в jokes_favorites
def create_joke_favorite(jokeId, userId):
    check = db.session.execute(f"SELECT jokeId FROM jokes_favorites WHERE (jokeId = '{jokeId}') AND (loginId = '{userId}')").fetchone()
    if check:
        return {'message': "Уже в избранном!"}
    try:
        db.session.execute(f"INSERT INTO jokes_favorites "
                           f"(jokeId, loginId) "
                           f"VALUES ("
                           f"'{jokeId}', "
                           f"'{userId}')"
                           )
        db.session.commit()
        return {'message': "Добавлено в избранное!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}


"""


-------------------------------------------- JOKES --------------------------------------------


"""

# Получаем список всех запросов jokes
def get_jokes_all():
    result = []    
    rows = db.session.execute("SELECT * FROM jokes").fetchall()
    for row in rows:
        result.append(dict(row))
    return {'jokes': result}

# Получаем список всех запросов jokes_old (ДЛЯ ПЕРЕНОСА СТАРОЙ ТАБЛИЦЫ В НОВУЮ)
def get_jokes_old_all():
    result = []    
    rows = db.session.execute("SELECT * FROM jokes_old").fetchall()
    for row in rows:
        result.append(dict(row))
    return result

# Получаем строку из jokes по id
def get_joke_by_id(id):
    result = db.session.execute("SELECT * FROM jokes WHERE id='{id}'").fetchall()
    return dict(result)

# Удаляем строку из jokes по id
def delete_joke_by_id(id):
    try:
        db.session.execute(f"DELETE FROM jokes WHERE id = {id}")
        db.session.commit()
        return {'message': "Joke Deleted!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Изменяем строку из jokes по id
def update_joke_by_id(id, json_data):
    try:
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.execute(f"UPDATE jokes SET "
                           f"name = '{json_data['name']}', "
                           f"content = '{json_data['content']}', "
                           f"updatedAt = '{cur_time}' "
                           f"WHERE id = {id}")
        db.session.commit()
        return {'message': "Joke Updated!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Добавляем строку в jokes
def create_joke(json_data):
    try:
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.execute(f"INSERT INTO jokes "
                           f"(name, content, createdAt, updatedAt) "
                           f"VALUES ("
                           f"'{json_data['name']}', "
                           f"'{json_data['content']}', "
                           f"'{cur_time}', "
                           f"'{cur_time}')"
                           )
        db.session.commit()
        return {'message': "Joke Created!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}


"""


-------------------------------------------- CATS --------------------------------------------


"""

# Получаем список всех запросов cats
def get_cats_all():
    result = []    
    rows = db.session.execute("SELECT * FROM cats").fetchall()
    for row in rows:
        result.append(dict(row))
    return {'cats': result}

# Получаем список всех запросов cats_old (ДЛЯ ПЕРЕНОСА СТАРОЙ ТАБЛИЦЫ В НОВУЮ)
def get_cats_old_all():
    result = []    
    rows = db.session.execute("SELECT * FROM cats_old").fetchall()
    for row in rows:
        result.append(dict(row))
    return result

# Получаем строку из cats по id
def get_cat_by_id(id):
    result = db.session.execute("SELECT * FROM cats WHERE id='{id}'").fetchall()
    return dict(result)

# Удаляем строку из cats по id
def delete_cat_by_id(id):
    try:
        db.session.execute(f"DELETE FROM cats WHERE id = {id}")
        db.session.commit()
        return {'message': "Cat Deleted!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Изменяем строку из cats по id
def update_cat_by_id(id, json_data):
    try:
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.execute(f"UPDATE cats SET "
                           f"name = '{json_data['name']}', "
                           f"content = '{json_data['content']}', "
                           f"path = '{json_data['path']}', "
                           f"updatedAt = '{cur_time}' "
                           f"WHERE id = {id}")
        db.session.commit()
        return {'message': "Cat Updated!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Добавляем строку в cats
def create_cat(json_data):
    try:
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.execute(f"INSERT INTO cats "
                           f"(name, content, path, createdAt, updatedAt) "
                           f"VALUES ("
                           f"'{json_data['name']}', "
                           f"'{json_data['content']}', "
                           f"'{json_data['path']}', "
                           f"'{cur_time}', "
                           f"'{cur_time}')"
                           )
        db.session.commit()
        return {'message': "Cat Created!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}


"""


-------------------------------------------- SERVICES --------------------------------------------


"""


# Получаем список всех запросов services
def get_services_all():
    result = []    
    rows = db.session.execute("SELECT * FROM services").fetchall()
    for row in rows:
        result.append(dict(row))
    return {'services': result}

# Получаем список всех запросов services_old (ДЛЯ ПЕРЕНОСА СТАРОЙ ТАБЛИЦЫ В НОВУЮ)
def get_services_old_all():
    result = []    
    rows = db.session.execute("SELECT * FROM services_old").fetchall()
    for row in rows:
        result.append(dict(row))
    return result

# Получаем строку из services по id
def get_services_by_id(id):
    result = db.session.execute("SELECT * FROM services WHERE id='{id}'").fetchall()
    return dict(result)

# Удаляем строку из services по id
def delete_service_by_id(id):
    try:
        db.session.execute(f"DELETE FROM services WHERE id = {id}")
        db.session.commit()
        return {'message': "Service Deleted!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Изменяем строку из services по id
def update_service_by_id(id, json_data):
    try:
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.execute(f"UPDATE services SET "
                           f"name = '{json_data['name']}', "
                           f"content = '{json_data['content']}', "
                           f"path = '{json_data['path']}', "
                           f"updatedAt = '{cur_time}' "
                           f"WHERE id = {id}")
        db.session.commit()
        return {'message': "Service Updated!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Добавляем строку в services
def create_service(json_data):
    try:
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.execute(f"INSERT INTO services "
                           f"(name, content, path, createdAt, updatedAt) "
                           f"VALUES ("
                           f"'{json_data['name']}', "
                           f"'{json_data['content']}', "
                           f"'{json_data['path']}', "
                           f"'{cur_time}', "
                           f"'{cur_time}')"
                           )
        db.session.commit()
        return {'message': "Service Created!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}


"""


-------------------------------------------- CONTACTREQUESTS --------------------------------------------


"""


# Получаем список всех запросов.
def get_contact_req_all():
    result = []     # создаем пустой список
    # Получаем итерируемый объект, где содержатся все строки таблицы contactrequests
    rows = db.session.execute("SELECT * FROM contactrequests").fetchall()
    # Каждую строку конвертируем в стандартный dict, который Flask может трансформировать в json-строку
    for row in rows:
        result.append(dict(row))
    # возвращаем dict, где result - это список с dict-объектов с информацией
    return {'contactrequests': result}

# Получаем список всех запросов contactrequests по id пользователя
def get_contact_req_by_userid(id):
    result = []    
    rows = db.session.execute(f"SELECT * FROM contactrequests WHERE userId = '{id}'").fetchall()
    for row in rows:
        result.append(dict(row))
    return {'contactrequests': result}

# Получаем запрос с фильтром по id
def get_contact_req_by_id(id):
    result = db.session.execute(f"SELECT * FROM contactrequests WHERE id = {id}").fetchone()
    return dict(result)

# Получаем все запросы по id
def get_contact_req_by_author(id):
    result = []
    rows = db.session.execute(f"SELECT * FROM contactrequests WHERE id = '{id}'").fetchall()
    for row in rows:
        result.append(dict(row))
    return {'contactrequests': result}

# Получаем все запросы по имени автора
def get_contact_req_by_author(fullname):
    result = []
    rows = db.session.execute(f"SELECT * FROM contactrequests WHERE fullname = '{fullname}'").fetchall()
    for row in rows:
        result.append(dict(row))
    return {'contactrequests': result}


# Создать новый запрос
def create_contact_req(json_data):
    try:
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")     # текущая дата и время
        userId = session.get('userId')
        # INSERT запрос в БД
        db.session.execute(f"INSERT INTO contactrequests "
                           f"(fullname, email, message, cratedAt, updatedAt, userId) "
                           f"VALUES ("
                           f"'{json_data['fullname']}', "
                           f"'{json_data['email']}', "
                           f"'{json_data['message']}', "
                           f"'{cur_time}', "
                           f"'{cur_time}', "
                           f"'{userId}')"
                           )
        # Подтверждение изменений в БД
        db.session.commit()
        # Возвращаем результат
        return {'message': "ContactRequest Created!"}
        # если возникла ошибка запроса в БД
    except Exception as e:
        # откатываем изменения в БД
        db.session.rollback()
        # возвращаем dict с ключом 'error' и текcтом ошибки
        return {'message': str(e)}


# Удалить запрос по id в таблице
def delete_contact_req_by_id(id):
    try:
        # DELETE запрос в БД
        db.session.execute(f"DELETE FROM contactrequests WHERE id = {id}")
        db.session.commit()
        return {'message': "ContactRequest Deleted!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Удалить запрос по дате в таблице
def delete_contact_req_by_date(date):
    try:
        # DELETE запрос в БД
        db.session.execute(f"DELETE FROM contactrequests WHERE cratedAt = '{date}'")
        db.session.commit()
        return {'message': "ContactRequest Deleted!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}


# Обновить текст запроса по id в таблице
def update_contact_req_by_id(id, json_data):
    try:
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # текущая дата и время
        # UPDATE запрос в БД
        db.session.execute(f"UPDATE contactrequests SET message = '{json_data['message']}', "
                           f"updatedAt = '{cur_time}' WHERE id = {id}")
        db.session.commit()
        return {'message': "ContactRequest Updated!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}



"""


-------------------------------------------- ВХОД/РЕГИСТРАЦИЯ --------------------------------------------


"""


# Поиск аккаунта пользователя в БД
def login_user(form_data):
    # Получаем логин и пароль из данных формы
    username = form_data.get('login__login')
    password = form_data.get('login__password')
    if username == '':
        return redirect(url_for('login'))
    # Ищем пользователя в БД
    result = db.session.execute(f"SELECT * FROM logins WHERE username = '{username}'").fetchone()
    # если пользователь не найден переадресуем на страницу /login
    if result is None:
        return redirect(url_for('login'))
    user = dict(result)
    # если пароль не прошел проверку, переадресуем на страницу /login
    if not bcrypt.checkpw(password.encode('utf-8'), user.get('password').encode('utf-8')):
        return redirect(url_for('login'))
    # иначе регистрируем сессию пользователя (записываем логин пользователя в параметр user) и высылаем cookie "AuthToken"
    else:
        response = redirect('/')
        session['user'] = user['username']
        session['userId'] = user['id']
        response.set_cookie('AuthToken', user['username'])
        return response


# Создание пользовательского аккаунта
def register_user(form_data):
    # Получаем данные пользователя из формы
    username = form_data.get('register__login')
    password = form_data.get('register__password')
    email = form_data.get('register__email')
    # Проверяем полученные данные на наличие обязательных полей
    if username == '' or password == '' or email == '':
        return make_response(jsonify({'message': 'The data entered are not correct!'}), 400)
    # Создаем хеш пароля с солью
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    try:
        db.session.execute(f"INSERT INTO logins "
                           f"(username, password, email) "
                           f"VALUES ("
                           f"'{username}', "
                           f"'{hashed}', "
                           f"'{email}'"
                           ")")
        # Подтверждение изменений в БД
        db.session.commit()
        # Переадресуем на страницу авторизации
        return redirect(url_for('login'))
        # если возникла ошибка запроса в БД
    except Exception as e:
        # откатываем изменения в БД
        db.session.rollback()
        # возвращаем response с ошибкой сервера
        return make_response(jsonify({'message': str(e)}), 500)
