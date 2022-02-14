import os
from celery import Celery

app = Celery('advertisement_django')   
app.autodiscover_tasks()
