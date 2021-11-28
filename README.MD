1. Запуск Docker-compose up -d --build
Создаём пользователей и статьи. 
2. docker-compose exec web manage.py python manage.py create_db 
Чтобы создать и заполнить индекс и сопоставление Elasticsearch, используйте
3. docker-compose exec web manage.py python manage.py search_index --rebuild   
4. http://localhost:8000/blog/  - можно посмотреть все данные в базе данных (без использования elasticsearch)
5. http://localhost:8000/search/article/ - после /  в адресной строке, вставляем запрос по поиску. Имя автора или текст из статьи.
6. http://localhost:8000/search/top_authors/ - выводит топ-10 авторов по количесву публикаций.
7. http://localhost:8000/search/search_range_date/ - выводит статьи за последние 24 месяца.