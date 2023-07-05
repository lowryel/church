web: python manage.py runserver 0.0.0.0:$PORT


gunicorn -c conf/gunicorn_config.py church.wsgi
