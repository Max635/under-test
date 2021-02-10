""" Script to start background jobs """
from apscheduler.schedulers.background import BackgroundScheduler
from emailManager import emailer


def start():
    """ Starts scheduler job everyday at 8 am """
    scheduler = BackgroundScheduler()
    scheduler.add_job(emailer.init_emailing, 'cron', hour='8')
    scheduler.start()
