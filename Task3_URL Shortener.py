import pyshorteners
import re
import pyperclip
from tkinter import *


def identify_urls():
    url = url_entry.get()
    pattern = r'https?://\S+|www\.\S+'
    urls = re.findall(pattern, url)
    if urls:
        shorten_url(url)
    else:
        final_url.config(text="No URLs found! Please retry and give a proper URL!")


def shorten_url(url):
    short_url = pyshorteners.Shortener()
    final_url.config(text=short_url.tinyurl.short(url))
    final = final_url.cget("text")
    pyperclip.copy(final)

window = Tk()
window.title('URL shortener Service')
window.geometry("400x400")

Url_label = Label(window, text="Enter URL: ", font="arial 10", fg="white", bg="brown")
Url_label.pack(pady=10)
url_entry = Entry(window)
url_entry.pack(pady=10)
frame = Frame(window)
frame.pack(pady=10)
generate_button = Button(frame, text="Generate shortened URL", fg="black", bg="cyan", command=identify_urls)
generate_button.grid(row=0, column=0, padx=10)
generated_url = Label(window, text="Generated shortened URL: ", font="arial 10", fg="white", bg="blue")
generated_url.pack(pady=10)
final_url = Label(window)
final_url.pack(pady=10)

window.mainloop()
