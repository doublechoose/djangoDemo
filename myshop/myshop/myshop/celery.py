import os
from celery import Celery
from django.conf import settings

# set the default django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTING_MODULE','myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
