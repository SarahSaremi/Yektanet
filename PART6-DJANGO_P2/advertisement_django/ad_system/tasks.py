import datetime

from celery import shared_task
from ad_system.models import *


@shared_task(queue='counting')
def hourly_report():
    t0 = datetime.datetime.now()
    t1 = t0 + datetime.timedelta(hours=1)

    click_num = Click.objects.filter(action_time__gt=t1, action_time__lt=t0).count()
    view_num = View.objects.filter(action_time__gt=t1, action_time__lt=t0).count()

    new_report = PeriodicReportModel(click_count=click_num, view_count=view_num)
    new_report.save()


@shared_task(queue='counting')
def daily_report():
    t0 = datetime.datetime.now()
    t1 = t0 + datetime.timedelta(days=1)

    click_num = Click.objects.filter(action_time__gt=t1, action_time__lt=t0).count()
    view_num = View.objects.filter(action_time__gt=t1, action_time__lt=t0).count()

    new_report = PeriodicReportModel(click_count=click_num, view_count=view_num)
    new_report.save()
