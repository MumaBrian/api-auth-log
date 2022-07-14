web: gunicorn work.wsgi
release: python manage.py makegrations --noinput
release:python manage.py collectstatic --noinput
release:python manage.py igrate --noinput