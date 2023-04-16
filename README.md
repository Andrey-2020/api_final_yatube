# api_final
api final

## Технологии
- Django REST Framework

- Вьюсеты. Расширенные возможности

- Роутеры и класс ReadOnlyModelViewSet

- Преобразование форматов. Сериализаторы

- Аутентификация по токену. Djoser и Simple JWT

- Кастомный пермишен в permissions.py унаследованный от permissions.BasePermission

- Фильтрация DjangoFilterBackend и поиск SearchFilter.  Встроенные фильтрующие бэкенды импортируются из библиотеки filters.
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Andrey-2020/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Создать пользователя:

```
Придумайте новую пару «логин-пароль» и отправьте POST-запрос на 
http://127.0.0.1:8000/auth/users/, передав их в полях username и password.

```

Получить токен:

```
http://127.0.0.1:8000/api/v1/jwt/create/ (POST): передаём логин и пароль, получаем токен.
```
{
"username": "string",
"password": "string"
}

Создание публикации:

```
http://127.0.0.1:8000/api/v1/posts/ (POST): Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
```
