import time
from plyer import notification

f = open("time.txt","r")
s = f.read()

sleeptime = s.split(":")


while True:
    curr = time.time()
    timestr = time.ctime(curr)
    temp = timestr.split()
    timelist = temp[3].split(":")
    timelist.pop()
    time.sleep(2)
    if(timelist == sleeptime):
        notification.notify(
            title="Studying Hard? But Wake Up",
            message="It's a fact that if you get rest after 60 minutes of continuous studying, it will boost your productivity ✌️",
            app_name="Wake Up Reminder",
            app_icon="D:\wakeup.ico",
            timeout=10,
            toast=False,
            
    )
        break

