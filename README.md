# SkyPro Дипломный проект
# Трекер задач сотрудников
# TaskTracker

## Задание
Необходимо реализовать серверное приложение для работы с базой данных.
Требования к базе данных:
1. БД реляционная (желательно Postgres)
2. БД представляет собой трекер задач и содержит следующие таблицы:
- таблица сотрудников (ФИО, должность, ...);
- таблица задач (наименование, ссылка на родительскую задачу, если есть 
зависимость, исполнитель, срок, статус, ...).

Реализовать на Python REST API (желательно FastAPI) со следующими эндпоинтами:
- CRUD для сотрудников и задач
- "Занятые сотрудники": Запрашивает из БД список сотрудников и их задачи, 
отсортированный по количеству активных задач.
- "Важные задачи":
  1. Запрашивает из БД задачи не взятые в работу, и от которых зависят 
     другие задачи, взятые в работу.
  2. Реализует поиск по сотрудникам, которые могут взять такие
     задачи (наименее загруженный сотрудник или сотрудник выполняющий 
     родительскую задачу если ему назначено максимум на 2 задачи больше, 
     чем у наименее загруженного сотрудника).
  3. Возвращает Список объектов [{Важная задача, Срок, [ФИО сотрудника]}].
    
Желательно реализовать валидацию данных.

### Некоторые уточнения и дополнения к заданию
1. Одна задача - один сотрудник, но один сотрудник может обрабатывать 
несколько задач.
2. Одна задача - одна родительская задача, но одна родительская задача может 
иметь несколько потомком.
3. Уровень вложения порожденных задача неограничен (?).
4. Важные задачи: задачи, не взятые в работу, потомки задач, взятых в работу.

5. Список сотрудников, которые могут взять задачу. Условия: 
   - имеет меньше всех заданий;
   - выполняет родительскую задачу, но имеет задач не больше чем на 2 наименее 
   загруженного сотрудника.
6. Список важных задач со сроком и исполнителем. 

## Направление: 
backend

## Тэги:
Git, Readme, PEP8, Swagger, FastAPI, JSON, Сторонние API

## Запуск на выполнение дипломного проекта

Используется Python 3.12
Описание работ для PyCharm в Windows.

1. Создать и активировать виртуальное окружение.
python -m venv venv
.\venv\Scripts\activate

2. Установить зависимости проекта, указанные в файле requirements.txt
pip install -r requirements.txt 
или средствами PyCharm.

3. Проверить наличие установленного PostgreSQL
4. Создать файл .env на основе sample.env

4. Запустить сервер
uvicorn main:app --reload 

При запуске отображается список сотрудников с принятыми задачами

localhost:8000/employees/ - список сотрудников.
localhost:8000/employees/busy - список занятых сотрудников и задания.
localhost:8000/employees/free - свободные сотрудники для задания?
localhost:8000/tasks/ - список заданий и работа с заданиями.
localhost:8000/tasks/important/ - список важных заданий.

5. Работать с базой данных или просматривать документацию API можно:
localhost:8000/docs или
localhost:8000/redoc

6. После первого запуска программы можно заполнить базу данных из скрипта 
tasktracker.sql. В этом файле только данные.