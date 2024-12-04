# db_changer
Скрипт для изменения плохих оценок, удаления замечаний учителей, добавления похвал в электронный дневник, написанный на Django.
### Как пользоваться
для того, чтобы поменять записи в базе данных надо:
- Поместить script.py в папке рядом с manage.py.
- Запустить скрпит через консоль `python3 script.py`.
- Ввести ФИО ученика, чьи данные хотим поменять. (нужно учитывать регистры)
- Ввести предмет для добавления похвалы. (нужно учитывать регистры)

После этого плохие оценки поменяются на 5 баллов, все замечания удалятся и добавится похвала по выбранному предмету.
### Пример
```
$ python3 script.py
Введите ФИО ученика: Иван Иванович Иванов
Введите предмет для создания похвалы: Математика
```
### Если нет развёрнутого проекта с базой данных
Следует перейти в этот репозиторий [Электронный дневник](https://github.com/devmanorg/e-diary) и следовать инструкциям электронного дневника.

## Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/)
