# task_manager
TodoApp with JWT

# Проект "Task Manager" на Django REST Framework

Проект "Task Manager" - это простое веб-приложение для управления задачами с использованием Django REST Framework (DRF) для создания API. Приложение позволяет пользователям создавать, просматривать, обновлять и удалять задачи. Также реализована аутентификация пользователей с помощью JWT (JSON Web Token).

                                                     ВАЖНО!
Проект может быть развёрнут в контейнере Docker или может быть запущен на локальном сервере.

1)Вариант развёртывания в контейнере:

1.Клонирование репозитория: 
- git clone https://github.com/adamant-antithesis/task_manager.git

2.Перейти в каталог task_manager(на уровень каталога с файлом manage.py):
- cd task_manager

3.Создайте и запустите контейнеры командой:
- docker-compose up --build 

4.Используйте Postman для доступа к эндпоинтам.


2)Вариант запуска на локальном сервере:

## Требования

- Python 3.x
- Django 3.x
- Django REST Framework (DRF)
- djangorestframework-simplejwt

## Установка и настройка

1.Клонирование репозитория: 
- git clone https://github.com/adamant-antithesis/task_manager.git

2.Перейти в каталог task_manager(на уровень каталога с файлом manage.py):
- cd task_manager

3.Установка зависимостей: 
- pip install -r requirements.txt

4.Создание базы данных с именем: 
- todobase

Войдите в оболочку PostgreSQL с помощью команды psql. Для этого введите следующую команду и нажмите Enter:

- psql -U <имя-пользователя> (используйте стандартное имя пользователя - postgres, пароль - postgres)

После входа в оболочку PostgreSQL введите команду для создания базы данных todobase. Введите следующее:

- CREATE DATABASE todobase;

5.Выход из оболочки PostgreSQL:

Чтобы выйти из оболочки PostgreSQL, введите команду \q и нажмите Enter.

6.Создание и применение миграций (вы должны находиться в каталоге task_manager на уровне с файлом manage.py):

python manage.py makemigrations
python manage.py migrate

7. Создание суперпользователя для управление административной панелью: 
- python manage.py createsuperuser

8. Команда для запуска тестов:
- python manage.py test tasks

9.Запуск сервера: 
- python manage.py runserver

10.Используйте Postman для доступа к эндпоинтам.

                                                 API ENDPOINTS

1. Доступ к административной панели Django.

----GET /admin/

Полная ссылка: http://127.0.0.1:8000/admin/
Описание: Административный интерфейс Django. В браузере перейдите по ссылке и аутентифицируйтесь по данным супер-пользователя.
Функция: Позволяет администратору управлять данными в админ-панели.


2. Модель User

----POST /api/users/

Полная ссылка: http://127.0.0.1:8000/api/users/
Описание: Создание нового пользователя.
Функция: Регистрирует нового пользователя в системе.(Поля username и email должны быть уникальны)

Данные для передачи:

{
    "username": "username",
    "first_name": "first_name",
    "last_name": "last_name",
    "email": "email",
    "password": "password"
}

3.Аутентификация


----POST /api/token/

Полная ссылка: http://127.0.0.1:8000/api/token/
Описание: Получение токена доступа.
Функция: Аутентификация пользователя и выдача токена доступа для доступа к защищенным эндпоинтам.

Данные для передачи:

{
    "username": "username",
    "password": "password"
}


----POST /api/token/refresh/

Полная ссылка: http://127.0.0.1:8000/api/token/refresh/
Описание: Обновление токена доступа.
Функция: Обновляет и предоставляет новый токен доступа на основе предыдущего.
Refresh получается авторизованным пользователем вместе с access по адресу - http://127.0.0.1:8000/api/token/

Данные для передачи:

{
    "refresh": "refresh(полученный из ответа POST /api/token/"
}

4.Модель Task

----GET /api/tasks/

Полная ссылка: http://127.0.0.1:8000/api/tasks/
Описание: Получение списка задач.
Функция: Позволяет получить список всех задач.

Данные для передачи:

Не требует данных. Требуется аутентификация с токен - Autorization - Bearer Token - {access_token}


----POST /api/tasks/

Полная ссылка: http://127.0.0.1:8000/api/tasks/
Описание: Создание новой задачи. Требуется аутентификация с токен - Autorization - Bearer Token - {access_token}
Функция: Позволяет создать новую задачу, связанную с текущим пользователем.

Данные для передачи:

{
    "title": "title,
    "description": "description",
    "status": "status (Варианты: New, In Progress, Completed),
}


----GET /api/tasks/int:pk/

Полная ссылка: http://127.0.0.1:8000/api/tasks/int:pk/
Описание: Получение деталей задачи по идентификатору.
Функция: Возвращает детали конкретной задачи по ее уникальному идентификатору (pk).

Данные для передачи:

Не требует данных. Требуется аутентификация с токен - Autorization - Bearer Token - {access_token}


----PUT /api/tasks/int:pk/

Полная ссылка: http://127.0.0.1:8000/api/tasks/int:pk/
Описание: Обновление задачи. Изменение доступно только автору задачи.
Функция: Позволяет обновить информацию о существующей задаче.

Данные для передачи:

{
    "title": "title",
    "description": "description",
    "status": "status(New, In Progress, Completed)",
}

----PATCH /api/tasks/int:pk/

Полная ссылка: http://127.0.0.1:8000/api/tasks/int:pk/
Описание: Частичное обновление задачи. Изменение доступно только автору задачи.
Функция: Позволяет частично обновить информацию о существующей задаче.

Данные для передачи(лично ничего, либо несколько полей):

{
    "title": "title",
    "description": "description",
    "status": "status(New, In Progress, Completed)"
}


----DELETE /api/tasks/int:pk/

Полная ссылка: http://127.0.0.1:8000/api/tasks/int:pk/
Описание: Удаление задачи. Удаление доступно только автору задачи.
Функция: Позволяет удалить задачу по ее уникальному идентификатору.

Данные для передачи:

Не требует данных. Требуется аутентификация с токен - Autorization - Bearer Token - {access_token}


----GET /api/user-tasks/

Полная ссылка: http://127.0.0.1:8000/api/user-tasks/
Описание: Получение списка задач текущего пользователя.
Функция: Возвращает список задач, связанных с текущим аутентифицированным пользователем.

Данные для передачи:

Не требует данных. Требуется аутентификация с токен - Autorization - Bearer Token - {access_token}


----PUT /api/tasks/int:pk/complete/

Полная ссылка: http://127.0.0.1:8000/api/tasks/int:pk/complete/
Описание: Пометить задачу как завершенную.
Функция: Меняет статус задачи на "Completed".

Не требует данных. Требуется аутентификация с токен - Autorization - Bearer Token - {access_token}


----GET /api/tasks/status/str:status/

Полная ссылка: http://127.0.0.1:8000/api/tasks/status/str:status/
Описание: Получение списка задач по статусу.
Функция: Возвращает список задач с заданным статусом.

Не требует данных. Требуется аутентификация с токен - Autorization - Bearer Token - {access_token}

Варианты статусов в ссылке: new, in_progress, completed
