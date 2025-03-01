import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hakaton.settings")

app = Celery("hakaton")

app.config_from_object('hakaton.settings', namespace="CELERY")

app.autodiscover_tasks()
