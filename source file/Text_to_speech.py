import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
bg_colour="#539eba"

#box
root=Tk()
root.title("Text to Speech")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg=bg_colour)#background colour

engine=pyttsx3.init()
def speaknow():
    text=text_area.get(1.0,END)
    gender= gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='normal'):
            engine.setProperty('rate',180)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()            
def download():
    text=text_area.get(1.0,END)
    gender= gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'sample.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'sample.mp3')
            engine.runAndWait()
    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

#icon
image_icon=PhotoImage(file="C:\\Users\AJAY KUMAR M\Desktop\\text to speech\source file\icon\iconlog.png")
root.iconphoto(False,image_icon)

#top panel
Top_frame=Frame(root,bg="white",width=900,height=80)
Top_frame.place(x=0,y=0)
Logo=PhotoImage(file="C:\\Users\AJAY KUMAR M\Desktop\\text to speech\source file\icon\Applogo.png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)
Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=100,y=20)

#text box
text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=20,y=130,width=500,height=250)
Label(root,text="VOICE",font="arial 15 bold",bg=bg_colour,fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg=bg_colour,fg="white").place(x=760,y=160)


#slide box for gender
gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

#slide box for speed
speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=740,y=200)
speed_combobox.set('Normal')


imageicon=PhotoImage(file="C:\\Users\AJAY KUMAR M\Desktop\\text to speech\source file\icon\speaklogo.png")
btn=Button(root,text="SPEAK",compound=LEFT,image=imageicon,width=130,font="arial 14 bold",command=speaknow)
btn.place(x=550,y=280)


imageicon2=PhotoImage(file="C:\\Users\AJAY KUMAR M\Desktop\\text to speech\source file\icon\save.png")
save=Button(root,text="SAVE",compound=LEFT,image=imageicon2,width=130,font="arial 14 bold",command=download)
save.place(x=740,y=280)
#copy right logo
footer_frame = tk.Frame(root, pady=10)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
copyright_notice = tk.Label(footer_frame, text="© 2024 Ajay Kumar. All rights reserved.", anchor='e')
copyright_notice.pack(side=tk.BOTTOM, padx=10)
root.mainloop()
