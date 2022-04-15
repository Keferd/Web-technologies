# -*- coding: utf-8 -*-
# Подключаем объект приложения Flask из __init__.py
from labapp import app, db
# Подключаем библиотеку для "рендеринга" html-шаблонов из папки templates
from flask import render_template, make_response, request, Response, jsonify, json

import json
from . import dbservice  

"""

    Модуль регистрации маршрутов для запросов к серверу, т.е.
    здесь реализуется обработка запросов при переходе пользователя на определенные адреса веб-приложения

"""

# Структура основного навигационнго меню веб-приложения,
# оформленное в виде массива dict-объектов

jokes = [
    {
        id: 1,
        "name": 'Появился, значит, в Зоне Чёрный сталкер.',
        "text": 'Появился, значит, в Зоне Чёрный сталкер. К лагерю ночью повадился ходить и там сует руку в палатку и говорит: «Водички попить!»',
    },
    {
        id: 2,
        "name": 'Долг и свобода',
        "text": 'Встречаются двое сталкеров, ну и один говорит: — На днях к Долгу заходил… — Ну и? — Что и? И остался должен. Ха. А потом',
    },
    {
        id: 3,
        "name": 'Сталкер и доктор',
        "text": 'Сталкер пришел к доктору и говорит: — Доктор, я совсем не могу спать… Мне снится, будто я заперт в саркофаге…',
    },
    {
        id: 4,
        "name": 'Заблудившийся',
        "text": 'Заблудился как-то долговец и кричит:— Люди, отзовитесь, кто-нибудь! Аууу! Тут его кто то догоняет и…',
    },
    {
        id: 5,
        "name": 'Ходячая аномалия',
        "text": 'Бродит, говорят, по зоне ходячая аномалия — непьющий и некурящий сталкер.',
    },
    {
        id: 6,
        "name": 'Признание',
        "text": 'У блок-поста прихватили новичка-сталкера и давай пытать:— С какой целью вы пытались проникнуть',
    }
]

cats = [
    {
        id: 1,
        "name": 'Caracal',
        "path": 'caracal.jpg',
        "text": 'Карака́л, или степная рысь (лат. Caracal caracal, от тюрк. qara qulaq — «чёрное ухо»), — хищное млекопитающее семейства кошачьих. Долгое время каракала относили к рысям (Lynx), на которых он похож внешне, однако из-за ряда генетических особенностей его выделили в отдельный род. Несмотря на это, каракал всё же немного ближе стоит к рысям, чем другие кошки, при этом будучи гораздо ближе к пуме по морфологическим признакам. Близок каракал и к африканскому сервалу, с которым хорошо скрещивается в неволе.',
    },
    {
        id: 2,
        "name": 'Lynx',
        "path": 'lynx.jpg',
        "text": 'Рысь — типичная кошка, хотя величиной с крупную собаку, которую отчасти напоминает своим укороченным телом и длинноногостью. Очень характерна голова рыси: сравнительно небольшая, округлая и очень выразительная. Рост обычной рыси достигает до 55 см, канадской- от 48 см до 56 см, а пиренейской — от 60 до 70 см. От других кошачьих рыси отличаются коротким хвостом и кисточками на концах ушей. Масса тела рыси от 5 до 30 кг.',
    },
    {
        id: 3,
        "name": 'Ocelot',
        "path": 'ocelot.png',
        "text": 'Оцелот (через европейские языки от аст. tlalocelotl «оцелот», tlalli «поле» + ocelotl «ягуар», лат. Leopardus pardalis) — хищное млекопитающее из семейства кошачьих, обитающее в Америке.',
    },
    {
        id: 4,
        "name": 'Tiger',
        "path": 'tiger.jpg',
        "text": 'Тигр (лат. Panthera tigris) — вид хищных млекопитающих семейства кошачьих, один из пяти представителей рода пантера (лат. Panthera), который относится к подсемейству больших кошек. Слово «тигр» происходит от др.-греч. τίγρις, которое в свою очередь восходит к др.-перс. *tigri от корня «*taig» со значением «острый; быстрый»',
    },
    {
        id: 5,
        "name": 'Lion',
        "path": 'lion.jpg',
        "text": 'Лев (лат. Panthera leo) — вид хищных млекопитающих, один из пяти представителей рода пантер (Panthera), относящегося к подсемейству больших кошек (Pantherinae) в составе семейства кошачьих (Felidae). Наряду с тигром — самая крупная из ныне живущих кошек, масса некоторых самцов может достигать 250 кг.',
    },
    {
        id: 6,
        "name": 'Black-panther',
        "path": 'black-panther.jpg',
        "text": 'Чёрные панте́ры — тёмноокрашенные особи из рода пантер, представляющих собой генетический вариант окраски — проявление меланизма. Чёрная пантера не является самостоятельным видом, это леопард (азиатский, африканский) или ягуар.',
    },
    {
        id: 7,
        "name": 'Manul',
        "path": 'manul.jpg',
        "text": 'Ману́л, также палласов кот (лат. Otocolobus manul) — хищное млекопитающее семейства кошачьих. Внешностью и размерами похож на домашнюю кошку, но отличается более коротким и массивным туловищем и лапами, а также длинным и густым светло-серым мехом. Округлые уши низко посажены по бокам головы. Длина головы и туловища составляет от 45 до 65 см, длина хвоста — от 21 до 31 см, масса составляет 2,5—4,5 кг.',
    },
    {
        id: 8,
        "name": 'Cat',
        "path": 'cat.jpg',
        "text": 'Ко́шка (лат. Felis catus) — домашнее животное, одно из наиболее популярных (наряду с собакой) «животных-компаньонов». С точки зрения научной систематики, домашняя кошка — млекопитающее семейства кошачьих отряда хищных. Нередко домашнюю кошку рассматривают как подвид лесной кошки (Felis silvestris) — Felis s. catus, однако, с точки зрения современной биологической систематики (2017 год), домашняя кошка является отдельным биологическим видом.',
    }
]

services = [
    {
        id: 1,
        "name": 'Мы заботимся о наших пользователях',
        "path": 'user.png',
        "text": 'Пользователям оказывается постоянная круглосуточная поддержка. При возниковении любой непредвиденной ситуации вы можете обратится в нашу службу поддержки.',
    },
    {
        id: 2,
        "name": 'Комментарии',
        "path": 'bubble.png',
        "text": 'Вы можете свободно оставлять комментарии. Мы будем рады если вы честно поделится своим мнением. Неподобающие сообщения будут удалены. Будьте снисходительны друг к другу.',
    },
    {
        id: 3,
        "name": 'Наушники',
        "path": 'headphones.png',
        "text": 'Наденьте наушники для более захватывающего пользовательского опыта. Использование наушников позволяет получать более качественное звучание.',
    },
    {
        id: 4,
        "name": 'Анекдоты',
        "path": 'pencil.png',
        "text": 'Почувтствуйте силу АНЕКДОТОВ! На  сайте представлены лучшие анекдоты со всего мира. Также вы можете самостоятельно сочинить и выложить на всеобщее обозрение свой собственный анекдот.',
    },
    {
        id: 5,
        "name": 'Почта',
        "path": 'message.png',
        "text": 'При регистрации на сайте используется ваша почта. Также вы можете получать уведомления об обновлениях сайта на почту.',
    },
    {
        id: 6,
        "name": 'Яркость',
        "path": 'sunny.png',
        "text": 'Вы можете настроить яркость на нашем сайте с высокой точностью. Больше не чуствуйте боль в глазах при ночной работе.',
    },
    {
        id: 7,
        "name": 'Музыка',
        "path": 'musical note.png',
        "text": 'Во время работы на нашем сайте вы можете слушать свою любимую музыку. Наслаждайтесь приятным времяпрепровождением.',
    },
    {
        id: 8,
        "name": 'Шифрование',
        "path": 'padlock.png',
        "text": 'На нашем сайте используются самые современные методы шифрования. Ваши пароли и личная информация в безопасности.',
    }
]

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
    return render_template('blog.html', title='Анекдоты', pname='BLOG', jokes=jokes)

# Обработка запроса к странице family.html
@app.route('/family')
def family():
    return render_template('family.html', title='Семья', pname='PORTFOLIO', cats=cats)

# Обработка запроса к странице our-services.html
@app.route('/our-services')
def our_services():
    return render_template('our-services.html', title='Сервисы', pname='SERVICES', services=services)

# Обработка запроса к странице team.html
@app.route('/team')
def team():
    return render_template('team.html', title='Команда', pname='TEAM')

# Обработка GET-запроса на все jokes
@app.route('/api/jokes', methods=['GET'])
def get_jokes():
    jokes = dbservice.get_jokes_all()
    return json_response(jokes)

# Обработка GET-запроса на все cats
@app.route('/api/cats', methods=['GET'])
def get_cats():
    cats = dbservice.get_cats_all()
    return json_response(cats)

# Обработка GET-запроса на все jokes
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
        msg = request.json['fullname'] + ", ваш запрос получен !"
        return json_response({ 'message': msg })

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


