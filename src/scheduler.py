import datetime
import time
from config import CLASS_SCHEDULE, CHECK_INTERVAL
from meeting_bot import join_meet

def run_scheduler():
    while True:
        now = datetime.datetime.now().strftime("%A %H:%M")  # e.g. "Monday 09:50"
        if now in CLASS_SCHEDULE:
            print(f"Time to join class at {now}")
            driver = join_meet(CLASS_SCHEDULE[now])
            return driver  # returns driver so you can decide later when to leave
        else:
            print(f"No class at {now}, checking again in {CHECK_INTERVAL}s...")
            time.sleep(CHECK_INTERVAL)