import datetime
import time

def countdown(enddate):
    while True:
        difference = enddate - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            print("Kickoff has been reached!")
            break
        print(str(difference.days) + " days "
              + str(count_hours) + " hours "
              + str(count_minutes) + " minutes "
              + str(count_seconds) + " seconds "
              )
        time.sleep(1)


setdate = datetime.datetime(2024, 1, 6, 12, 0, 0)
countdown(setdate)