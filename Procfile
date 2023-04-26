web: python manage.py runserver 0.0.0.0:$PORT

sudo systemctl restart nginx
gunicorn -c conf/gunicorn_config.py church.wsgi
