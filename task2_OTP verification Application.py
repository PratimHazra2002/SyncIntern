import tkinter as tk
import smtplib
import random


def generate_otp():
    return random.randint(100000, 999999)


def verify_otp():
    entered_otp = otp_entry.get()

    if entered_otp == str(otp):
        result_label.config(text="OTP verification successful!")
    else:
        result_label.config(text="OTP verification failed!")


otp = generate_otp()

sender_email = "codeforpyhton007@gmail.com"
password = "gxdbubmahhszimli"
message = f"OTP Verification\n\nYour OTP is: {otp}"
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    receiver = "pratimhazra2019@gmail.com"
    server.sendmail(sender_email, receiver, message)
    print("OTP sent successfully")
    server.quit()
except Exception as e:
    print("An error occurred while sending the OTP:", e)

window = tk.Tk()
window.title("OTP Verification")
window.geometry("400x400")

title_label = tk.Label(window, text="OTP VERIFIER", font="arial 20", fg="black", bg="Yellow")
title_label.pack(pady=10)

otp_label = tk.Label(window, text="Otp:", font="arial 10", fg="white", bg="green")
otp_label.pack(pady=10)
otp_entry = tk.Entry(window)
otp_entry.pack(pady=10)

verify_button = tk.Button(window, text="Verify", fg="white", bg="red", command=verify_otp)
verify_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
verify_otp()
