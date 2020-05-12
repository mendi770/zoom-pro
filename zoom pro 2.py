from datetime import date, datetime, timedelta
import os
import time, threading

now = datetime.now()
mint = now.minute
hour = now.hour


zoom = r"C:\Users\Owner\AppData\Roaming\Zoom\bin\Zoom.exe"
msg = r"C:\Users\Owner\Desktop\פייתון\קובץ .py\zoom pro\aaa.VBS"

dely = 0


def time_converter_h(e):
    # time
    if e == 1:
        e = 3600
    else:
        e = e * 60 * 60
    e = float(e)
    return e


if hour > 12:
    d_h = 20 - hour
    d_m = 60 - mint
else:
    d_h = 12 - hour
    d_m = 60 - mint

d_m_h = time_converter_h(d_m)
d_h_h = time_converter_h(d_h)

dely = d_h_h + d_m_h

print(d_h_h)
print(d_m_h)
print(dely)


def zoom_open():
    # os.system(msg)
    os.system(zoom)


if __name__ == '__main__':
    t = threading.Timer(dely, zoom_open)
    t.start()
