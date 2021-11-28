FROM python:3.9
RUN python -m pip install --upgrade pip
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

# Copy project
COPY . /app/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate 
# RUN python manage.py search_index --rebuild 
# RUN python manage.py create_db 

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

