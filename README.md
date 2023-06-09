# Простое Flask API приложение tickets

Реализация на Python, Flask, PostgreSQL, SQLAlchemy, uWSGI, Redis. API было реализовано с большим количеством 
ендпоинтов, чем было указано в требованиях к задаче, они отмечены в списке ниже.

Контейнеризация проекта не доведена до конца.
Просьба обратить вниммание на проект [контейнеризированного блога на Django 
с использованием Elasticsearch](https://github.com/mmanylov/django_blog_w_elasticsearch_containerized).

## Описание функциональности

Тикет-система должна состоять из:
- Тикетов, у тикетов могут быть комментарии;
- Тикет создается в статусе “открыт”, может перейти в “отвечен” или “закрыт”, из
"отвечен" в “ожидает ответа” или “закрыт”, статус “закрыт” финальный (нельзя
изменить статус или добавить комментарий).
  
Тикет имеет свойства:
- ID;
- Дата создания;
- Дата изменения;
- Тема;
- Текст;
- Email;
- Статус.

API ендпоинты:
- Получить все тикеты (нет в требованиях к задаче);
- Создать тикет;
- Получить тикет;
- Удалить тикет (нет в требованиях к задаче);
- Изменить статус тикета;
- Получить все комментарии по данному тикету (нет в требованиях к задаче);
- Добавить комментарий к тикету;
- Удалить комментарий (нет в требованиях к задаче).

## Реализация

Данное приложение написано с использованием библиотек Flask, Flask-SQLAlchemy, Flask-Migrate, redis и прочих.

## Развертывание

Приложение написано для развертывания на Ubuntu 20.04 с установленным nginx, postgres и python 3.

Для развертывания приложения необходимо создать виртуальное окружение и выполнить установку необходимых зависимостей из 
файла ```tickets/requirements.txt```.  Далее следует выполнить создание базы данных для проекта, в данном случае она 
должна называться ```tickets```, и создать пользователя, в данном случае - ```ticketsuser``` с паролем ```easypass```. 
После чего нужно выполнить миграции базы при помощи команды ```flask db upgrade```.

Конфигурация сервиса ```systemd``` находится в файле ```tickets/tickets.service```, в котором необходимо изменить 
параметры в секции ```Service``` на подходящие.
Для добавления сервиса в систему необходимо скопировать файл ```tickets/tickets.service``` в директорию 
```/etc/systemd/system/```.
Для старта сервиса использовать команду ```sudo systemctl start tickets.service```.
Для просмотра статуса сервиса выполнить ```sudo systemctl status tickets.service```.
Для автоматиечкого старта сервиса при старте системы необходимо выполнить ```sudo systemctl enable tickets.service```.

Конфигурация nginx веб-сервера находится в файле ```tickets/app.conf```.
Для добавления в конфигурацию системного nginx необходимо скопировать файл ```tickets/app.conf``` в директорию 
```/etc/nginx/sites-available```, а также выполнить 
линковку ```sudo ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled```.
Далее следует перезагрузить конфигурацию nginx при помощи команды ```sudo systemctl reload nginx```, а также 
добавить nginx в исключения фаервола при помощи команды ```sudo ufw allow 'Nginx Full'```.

Для тестирования приложения в ручную можно использовать Postman.
Для данного приложения в репозиториии имееется коллекция методов, 
которые можно импортировать из файла ```flask_tickets.postman_collection.json```.
