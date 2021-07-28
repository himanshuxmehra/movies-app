from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .views import weeklyNewsLetter

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(weeklyNewsLetter, 'interval', days=7)
    scheduler.start()