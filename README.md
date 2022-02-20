# API_YAMDB
REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке. (Коллективный проект 3 студентов Яндекс.Практикум)

### Технологический стек
![Django-app workflow](https://github.com/needred/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание

API для сервиса YaMDb.

Позволяет работать со следующими сущностями:
- Отзывы
- Коментарии к отзывам
- Пользователи
- Категории (типы) произведений
- Категории жанров
- Произведения (на которые пишут отзывы)

### Как запустить проект:

Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone https://github.com/needred/infra_sp2
cd infra_sp2
```

Перейдите в папку с проектом:
```
cd api_yamdb
```

Cоздайте и активируйте виртуальное окружение:
```
python3 -m venv venv
. venv/bin/activate
python3 -m pip install --upgrade pip
```

Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Перейдите в папку с файлом docker-compose.yaml:
```
cd infra
```

Разверните контейнеры:
```
docker-compose up -d --build
```

Выполните миграции:
```
docker-compose exec web python manage.py migrate
```

Создайте суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```

Соберите статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```

Создайте дамп (резервную копию) базы:
```
docker-compose exec web python manage.py dumpdata > fixtures.json
```

Остановите приложение в контейнерах:
```
docker-compose down -v
```

Запустите pytest (при запущенном виртуальном окружении):
```
cd infra_sp2 && pytest
```


### Шаблон наполнения .env
```
# указываем, с какой БД работаем
DB_ENGINE=django.db.backends.postgresql
# имя базы данных
DB_NAME=
# логин для подключения к базе данных
POSTGRES_USER=
# пароль для подключения к БД (установите свой)
POSTGRES_PASSWORD=
# название сервиса (контейнера)
DB_HOST=
# порт для подключения к БД
DB_PORT=
```

### Документация API YaMDb
Доступна по эндпойнту:
```json
/redoc/
```

### Авторы
Авторы:
===
[needred](https://github.com/needred)
[svs7771](https://github.com/svs7771)
[frollow](https://github.com/frollow)
Проект разрабатывался в команде, ссылка на репозиторий:
https://github.com/svs7771/api_yamdb
