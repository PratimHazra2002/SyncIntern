import datetime
from playsound import playsound
import tkinter as tk
from tkinter import messagebox


def play_alarm():
    playsound("C:\\Users\\HP\\Downloads\\Alarm Song.mp3")


def set_alarm():
    hour = int(entry_hour.get())
    minute = int(entry_minute.get())

    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    if current_hour > hour or (current_hour == hour and current_minute >= minute):
        alarm_time = datetime.datetime(now.year, now.month, now.day, hour, minute) + datetime.timedelta(days=1)
    else:
        alarm_time = datetime.datetime(now.year, now.month, now.day, hour, minute)

    time_difference = alarm_time - now
    seconds_difference = time_difference.total_seconds()

    mains.after(int(seconds_difference * 1000), play_alarm)

    messagebox.showinfo("Alarm Set", f"Alarm set for {hour:02d}:{minute:02d}\n time left {time_difference}")


mains = tk.Tk()
mains.title("Alarm")

current_date = datetime.datetime.now().strftime("%B %d, %Y")
label_date = tk.Label(mains, text=f"Date: {current_date}")
label_date.pack()

label_hour = tk.Label(mains, text="Hour (0-23):")
label_hour.pack()
entry_hour = tk.Entry(mains)
entry_hour.pack()

label_minute = tk.Label(mains, text="Minute (0-59):")
label_minute.pack()
entry_minute = tk.Entry(mains)
entry_minute.pack()

button_set_alarm = tk.Button(mains, text="Set Alarm", command=set_alarm)
button_set_alarm.pack()

mains.mainloop()
