# Онлайн платформа торговых сетей электроники
Данное веб-приложение для управления сетью по продаже электроники, представляющей собой иерархическую структуру.
Приложение разработано с использованием Django и Django REST framework.

Стек технологий:
* Python 3.12
* Django 5.0.1
* djangorestframework 3.14.0
* PostgreSQL 10+

## Работа с проектом 
1. Установить виртуально окружение командой: `python -m venv env` и установить зависимости:
`pip install -r requirements.txt`
2. Создать базу данных PostreSQL и провести миграции командой: `python manage.py migrate`
3. Переименовать файл '.env-sample' в '.env' и заполнить соответствующие поля
4. Запустить сервер командой python manage.py runserever
5. Командой `python manage.py csu` можно создать суперпользователя для входа в админку.

### Данные для входа на страницу администрирования:

* Почта: admin@admin.com
* Пароль: password

## О проекте

### Модели
1. Link - модель звена сети. Тип звена один из трех вариантов: Завод, ИП и розничная сеть. Уровень звена в иерархии сети
определяется по закупкам. Завод всегда имеет 0 уровень и не может иметь поставщика. ИП и розничная сеть имеют уровень 1 
в случае если закупки ведутся напрямую с завода, в противном случае уровень этих звеньев - 2. Уровень звена определяется
при его создании.
2. Contact - модель контактов. Модель с контактными данными звена сети. Связанна с моделью Link полем OneToOneField 
(поле OneToOneField выбрано т.к. разные звенья не могут иметь одинаковых контактов).
3. Product - модель продукции, продаваемой звеном сети. Связь с Link при помощи ManyToMany, т.к. один и то же товар 
может продаваться различными звеньями сети.

### Админка
Страница администрирования позволяет посмотреть существующие звенья сети. Так же добавлена возможность обнулить долг 
выбранных звеньев сети при помощи кастомного действия (при помощи API изменение задолженности запрещено). Добавлены 
фильтры по городу, типу и уровню в иерархии

### API
Реализован CRUD механизм для модели Link, доступ к которому имеют только активные сотрудники. При просмотре списка всех 
звеньев сети доступна фильтрация по стране 

### Эндпоинты 
http://127.0.0.1:8000/link/factory/create/ - создание завода

http://127.0.0.1:8000/link/create/ - создание других звеньев

(при создании завода создаются новые объекты модели Product, при создании других звеньев новые продукты не создаются, а 
используются уже существующие)

http://127.0.0.1:8000/link/list/ - просмотр списка всех звеньев, для фильтрации используется:

http://127.0.0.1:8000/link/list/?contact__country=<страна_по_которой_проходит_поиск>

http://127.0.0.1:8000/link/<int:pk>/ - просмотр отдельного звена сети, где <int:pk> - id звена

http://127.0.0.1:8000/link/edit/<int:pk>/ - изменение звена 
http://127.0.0.1:8000/link/delete/<int:pk>/ - удаление звена 