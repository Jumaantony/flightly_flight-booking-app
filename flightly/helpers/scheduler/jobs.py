import logging

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, register_job
from django.conf import settings

from flightly.flight_booking.tasks import SendEmailReminder

scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)


@register_job(scheduler, "interval", hours=12, replace_existing=False)
def email_reminder_job():
    SendEmailReminder()()


def start():
    if settings.DEBUG:
        logging.basicConfig()
        logging.getLogger('Flightly BG Scheduler').setLevel(logging.DEBUG)

    register_events(scheduler)
    scheduler.start()
