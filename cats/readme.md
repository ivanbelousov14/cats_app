# Тестовое приложение
## for using:
1. Create new project and create venv
2. Clone repository <https://github.com/ivanbelousov14/cats_app>
3. From Folder 'cats_app/cats' enter command: __poetry install__ (if windows os, if Linux - uncommented block with "curl" in Dockerfile)
4. Run command: __docker-compose up -d__
5. Run command: __docker-compose exec api poetry run python manage.py migrate__
6. Go to the __127.0.0.1:8000__
7. Url swagger: __127.0.0.1/api/schema/swagger/__
<hr>

__Data for tables in json files__ 