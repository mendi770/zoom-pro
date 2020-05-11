from datetime import date, datetime, timedelta
import os
import time, threading

now = datetime.now()
mint = now.minute
hour = now.hour
print(hour)

zoom = r"C:\Users\Owner\AppData\Roaming\Zoom\bin\Zoom.exe"
msg = r"C:\Users\Owner\Desktop\פייתון\קובץ .py\zoom pro\aaa.VBS"

dely = 0


def f(e):
    if e == 1:
        e = 3600
    else:
        e = e * 60 * 60
    print(e)


def time_ֿzoom():
    print("שיעור")
    os.system(msg)
    os.system(zoom)


if hour > 12:
    d = 20 - hour
else:
    d = 12 - hour
print(d)
dely = d
threading.Timer(dely, time_ֿzoom()).start()

