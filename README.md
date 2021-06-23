# API for Votings
Задача: спроектировать и разработать API для системы опросов пользователей

## Описание ТЗ:

##### _Функционал для администратора системы:_
- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

##### _Функционал для пользователей системы:_
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя


## Окружение проекта:
  * python 3.8
  * Django 2.2.10
  * djangorestframework

* Склонируйте репозиторий с помощью git
```bash
git clone https://github.com/josephRTi/Votings.git
```
* Настраиваем virtualenv и пакеты в нем:
```bash
cd Votings
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

* Миграции
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```
* Запуск приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/

(автодокументирование на swagger по адресу http://127.0.0.1:8000/swagger/ )

### Документация
### Получение токена пользователя
* Request method: POST
* URL: http://localhost:8000/api/auth/token
* Body: 
    * username: 
    * password: 

### Регистрация пользователя
* Request method: POST
* URL: http://localhost:8000/api/auth/
* Body: 
    * username: 
    * password: 
    * (optional) email: 

### Создание опроса
* Request method: POST
* URL: http://localhost:8000/api/surveys/create/
* Body: 
    * survey_name: 
    * pub_date: 
    * end_date:
    * survey_description:
    * is_active:

### Редактирование опроса
* Request method: POST
* URL: http://localhost:8000/api/surveys/update/<int:pk>
* Body: 
    * survey_name: 
    * pub_date: 
    * end_date:
    * survey_description:
    * is_active:

### Удаление опроса
* Request method: POST
* URL: http://localhost:8000/api/surveys/delete/<int:pk>

### Создание ответа
* Request method: POST
* URL: http://localhost:8000/api/answers/create/
* Body: 
    * (fk) question:
    *  answer:

### Редактирование ответа
* Request method: POST
* URL: http://localhost:8000/api/answers/update/<int:pk>
* Body: 
    * (fk) question:
    *  answer:

### Удаление ответа
* Request method: POST
* URL: http://localhost:8000/api/answers/delete/<int:pk>

### Создание вопроса
* Request method: POST
* URL: http://localhost:8000/api/questions/create/
* Body: 
    * (fk) survey:
    *  question_text:
    *  question_type:

### Редактирование вопроса
* Request method: POST
* URL: http://localhost:8000/api/questions/update/<int:pk>
* Body: 
    * (fk) survey:
    *  question_text:
    *  question_type:

### Удаление вопроса
* Request method: POST
* URL: http://localhost:8000/api/questions/delete/<int:pk>

### Создание факта голосования
* Request method: POST
* URL: http://localhost:8000/api/votefacts/create/
* Body: 
    * (fk) author:
    * (fk) survey:
    * (fk) question:
    * (fk) answer:
    * create_date:

### Редактирование факта голосования
* Request method: POST
* URL: http://localhost:8000/api/votefacts/update/<int:pk>
* Body: 
    * (fk) author:
    * (fk) survey:
    * (fk) question:
    * (fk) answer:
    * create_date:

### Удаление факта голосования
* Request method: POST
* URL: http://localhost:8000/api/votefacts/delete/<int:pk>

### Получение ответов некоторого пользователя
* Request method: GET
* URL: http://localhost:8000/api/votefacts/getAll
* params: user_id=<int:pk>
