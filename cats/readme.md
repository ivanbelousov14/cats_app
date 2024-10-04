# Тестовое приложение
## for using:

1. Clone repository https://github.com/ivanbelousov14/cats_app
2. From Folder 'cats_app/cats' enter command: __poetry install__ (if windows os, if Linux - uncommented block with "curl" in Dockerfile)
3. Run command: __docker-compose up -d__
4. Run command: __docker-compose exec api poetry run python manage.py migrate__
5. Go to the __127.0.0.1:8000__
6. Url swagger: __127.0.0.1/api/schema/swagger/__

