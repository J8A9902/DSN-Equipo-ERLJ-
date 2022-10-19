
from celery import Celery
from config import CELERY_BROKER

def make_celery(app):
    celery=Celery(__name__,backend = CELERY_BROKER, broker=CELERY_BROKER)
    celery.conf.update(app.config)
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task=ContextTask
    return celery