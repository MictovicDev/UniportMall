import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mictovic.settings')


app = Celery('mictovic')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_data': {
        'task': 'socials.tasks.obtain_data',
        'schedule': 1.0
    }
}


app.autodiscover_tasks()


