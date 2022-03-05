#!/usr/bin/env python3.9
from tkinter import *
from tkinter import messagebox
import random


def generate_5():
    values = random.sample(range(-100, 100), 5)
    oeal = str(values)
    han = oeal.replace(',',' ').replace('[','').replace(']','')

    text_entry.delete('1.0', END)
    text_entry.insert(END, str(han))

def generate_100():

    values = random.sample(range(-100, 1000), 100)
    oeal = str(values)
    han = oeal.replace(',',' ').replace('[','').replace(']','')

    strippedText = str(han).replace('[','').replace(']','')

    text_entry.delete('1.0', END)
    text_entry.insert(END, strippedText)

def generate_500():
    values = random.sample(range(-1000, 1000), 500)
    oeal = str(values)
    han = oeal.replace(',','').replace('[','').replace(']','')

    text_entry.delete('1.0', END)
    text_entry.insert(END, str(han))


def generate():
    if len(entrynbr1.get()) == 0:
        messagebox.showinfo(title="Required Field", message="Please provide a valid lower limit value", icon='warning')
    elif len(entrynbr2.get()) == 0:
        messagebox.showinfo(title="Required Field", message="Please provide a valid upper limit value", icon='warning')
    elif len(entrynbr3.get()) == 0:
        messagebox.showinfo(title="Required Field", message="Please provide a positve integer as the amount of numbers to generate", icon='warning')
    else:
        pass
    
    srt = int(entrynbr1.get())
    rng = int(entrynbr2.get())
    sze = int(entrynbr3.get())

    
    
    values = random.sample(range(srt, rng), sze)
    oeal = str(values)
    han = oeal.replace(',',' ').replace('[','').replace(']','')

    text_entry.delete('1.0', END)
    text_entry.insert(END, str(han))


def copy_to_cliboard():
    top.clipboard_append(text_entry.get('1.0', END))


def exit():
    msg = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if msg == 'yes':
       top.destroy()
    else:
        pass


top = Tk()

top.title("Numbers Generator")
top.minsize(600, 700)
top.resizable(0, 0)
top.iconbitmap("/goinfre/otoufah/unnamed.ico")


lblnbr1 = Label(top, text="Start",bg='azure')
lblnbr1.place(x=120, y=50)

entrynbr1 = Entry(top, border=2)
entrynbr1.place(x=200, y=50)

lblnbr2 = Label(top, text="Range",bg='azure')
lblnbr2.place(x=120, y=100)

entrynbr2 = Entry(top, border=2)
entrynbr2.place(x=200, y=100)

lblnbr3 = Label(top, text="Size",bg='azure')
lblnbr3.place(x=120, y=150)

entrynbr3 = Entry(top, border=2)
entrynbr3.place(x=200, y=150)

lblnbr1 = Button(top, border=4,text="Fast 5",bg='azure',padx=10, pady=5,command=generate_5)
lblnbr1.place(x=450, y=50)

lblnbr1 = Button(top, border=4,text="Fast 100",bg='azure',padx=10, pady=5,command=generate_100)
lblnbr1.place(x=450, y=100)

lblnbr1 = Button(top, border=4,text="Fast 500",bg='azure',padx=10, pady=5,command=generate_500)
lblnbr1.place(x=450, y=150)

gen = Button(top, border=4 ,text="Generate Numbers", bg='LightBlue1',padx=10, pady=5, command=generate)
gen.place(x=220, y=200)

clp = Button(top, border=4 ,text="Copy To Clipboard",padx=10, pady=5, bg='LightBlue1',command=copy_to_cliboard)
clp.place(x=220, y=240)

butt = Button(top, border=4, text="Exit", bg='azure', padx=5, pady=5, command=exit)
butt.place(x=470, y=220)

text_entry = Text(top, width=80, height=27, border=4, relief=RAISED)
text_entry.pack()
text_entry.place(x=10, y=270)



top['background'] = 'azure'

top.mainloop()