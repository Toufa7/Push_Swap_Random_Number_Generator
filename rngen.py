#!/usr/bin/env python3.9
from tkinter import *
from tkinter import messagebox
import random

def generate_5():
    values = random.sample(range(-100, 100), 5)
    hola = str(values)
    han = hola.replace(',', ' ').replace('[', '').replace(']', '')

    text_entry.delete('1.0', END)
    text_entry.insert(END, str(han))

def generate_100():

# with the help of random we can generate a sequence of numbers 
    values = random.sample(range(-21474, 21474), 100)
    hola = str(values)
    han = hola.replace(',', ' ').replace('[', '').replace(']' ,'')

    ynwa = str(han).replace('[', '').replace(']', '')

    text_entry.delete('1.0', END)
    text_entry.insert(END, ynwa)

def generate_500():
    values = random.sample(range(-2147, 2147), 500)
    hola = str(values)
    han = hola.replace(',', '').replace('[', '').replace(']', '')

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
    hola = str(values)
    han = hola.replace(',', ' ').replace('[', '').replace(']', '')

    text_entry.delete('1.0', END)
    text_entry.insert(END, str(han))


def copy_to_cliboard():
    poms.clipboard_clear() # don't save the data that already been copy
    poms.clipboard_append(text_entry.get('1.0', END).rstrip())


def exit():
    msg = messagebox.askquestion ('Exit','Are you sure you want to exit the application',icon = 'warning')
    if msg == 'yes':
       poms.destroy()
    else:
        pass


poms = Tk()

poms.title("Number Generator") #title of the Program
poms.minsize(600, 700)
poms.resizable(0, 0) # blocking resizing
poms.attributes('-alpha',1.8) # for transparance 

# This well be label that has start 
lblnbr1 = Label(poms, text="Start",bg='azure')
lblnbr1.place(x=120, y=50)
# This well host the value provide to be a start (lower limit value)
entrynbr1 = Entry(poms, border=2, justify = CENTER)
entrynbr1.place(x=200, y=50)

lblnbr2 = Label(poms, text="Range", bg='azure')
lblnbr2.place(x=120, y=100)

# This well host the value provide to be a Range (upper limit value)
entrynbr2 = Entry(poms, border=2, justify = CENTER)
entrynbr2.place(x=200, y=100)

lblnbr3 = Label(poms, text="Size",bg='azure')
lblnbr3.place(x=120, y=150)

entrynbr3 = Entry(poms, border=2, justify = CENTER)
entrynbr3.place(x=200, y=150)

lblnbr1 = Button(poms, border=4, text="Fast 5", bg='azure', padx=10, pady=7, command=generate_5)
lblnbr1.place(x=450, y=50)

lblnbr1 = Button(poms, border=4, text="Fast 100", bg='azure', padx=10, pady=7, command=generate_100)
lblnbr1.place(x=450, y=100)

lblnbr1 = Button(poms, border=4, text="Fast 500", bg='azure', padx=10, pady=7, command=generate_500)
lblnbr1.place(x=450, y=150)

gen = Button(poms, border=4 ,text="Generate Numbers", bg='LightBlue1',padx=10, pady=5, command=generate)
gen.place(x=220, y=200)

clp = Button(poms, border=4 , text="Copy To Clipboard", padx=10, pady=5, bg='LightBlue1', command=copy_to_cliboard)
clp.place(x=220, y=240)

butt = Button(poms, border=4, text="Exit", bg='azure', padx=5, pady=5, command=exit)
butt.place(x=470, y=220)

text_entry = Text(poms, width=80, height=27, border=4, relief=RAISED)
text_entry.pack()
text_entry.place(x=10, y=270)

poms['background'] = 'azure'

poms.mainloop()
