celery -A tasks worker -l  info & gunicorn -b 0.0.0.0:5000 app:app