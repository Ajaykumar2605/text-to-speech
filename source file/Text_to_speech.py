import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
import requests
from io import BytesIO
from PIL import Image, ImageTk

bg_colour = "#539eba"

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
        elif speed == 'Normal':
            engine.setProperty('rate', 180)
        else:
            engine.setProperty('rate', 60)
        setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            engine.save_to_file(text, 'sample.mp3')
            engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        setvoice()

def load_image(url):
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))

# Create the main window
root = Tk()
root.title("Text to Speech")
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg=bg_colour)

# Load images from GitHub URLs
def get_image(url, size):
    image = load_image(url)
    image = image.resize(size)
    return ImageTk.PhotoImage(image)

icon_url = "https://github.com/Ajaykumar2605/Text-to-Speech/blob/main/source%20file/icon/iconlog.png?raw=true"
logo_url = "https://github.com/Ajaykumar2605/Text-to-Speech/blob/main/source%20file/icon/Applogo.png?raw=true"
speak_icon_url = "https://github.com/Ajaykumar2605/Text-to-Speech/blob/main/source%20file/icon/speaklogo.png?raw=true"
save_icon_url = "https://github.com/Ajaykumar2605/Text-to-Speech/blob/main/source%20file/icon/save.png?raw=true"

# Set window icon
image_icon = get_image(icon_url, (32, 32))
root.iconphoto(False, image_icon)

# Top panel
Top_frame = Frame(root, bg="white", width=900, height=80)
Top_frame.place(x=0, y=0)
Logo = get_image(logo_url, (100, 70))
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)
Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black").place(x=100, y=20)

# Text box
text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=20, y=130, width=500, height=250)
Label(root, text="VOICE", font="arial 15 bold", bg=bg_colour, fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg=bg_colour, fg="white").place(x=760, y=160)

# Slide box for gender
gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

# Slide box for speed
speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=740, y=200)
speed_combobox.set('Normal')

# Speak button
imageicon = get_image(speak_icon_url, (30, 30))
btn = Button(root, text="SPEAK", compound=LEFT, image=imageicon, width=130, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

# Save button
imageicon2 = get_image(save_icon_url, (30, 30))
save = Button(root, text="SAVE", compound=LEFT, image=imageicon2, width=130, font="arial 14 bold", command=download)
save.place(x=740, y=280)

# Copyright logo
footer_frame = tk.Frame(root, pady=10)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
copyright_notice = tk.Label(footer_frame, text="© 2024 Ajay Kumar. All rights reserved.", anchor='e')
copyright_notice.pack(side=tk.BOTTOM, padx=10)

root.mainloop()
