release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py createsuperuser --noinput --email $ADMIN_EMAIL --employee_id $ADMIN_EMPLOYEE_ID
web: gunicorn ekeycare.wsgi --log-file -