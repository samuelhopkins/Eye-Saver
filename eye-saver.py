
import sys
import subprocess
import datetime
import time
import logging
from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.daemonic = False
sched.start()

logging.basicConfig()

def save():
	subprocess.call("./save-my-eyes.sh", shell=True)

# Schedules job_function to be run once each minute
sched.add_cron_job(save,  minute="*/20")



if __name__=="__main__":
	save()