"""My Digital Clock"""

from tkinter import*
from tkinter.ttk import* # Style the tkinter widgets
from time import strftime # time format

root = Tk()
root.title("Digital Clock")

def time():
    str = strftime('%H:%M:%S %p')
    label.config(text=str)
    label.after(1000,time) # After every second calling the time()


label = Label(root, font= ("ds-digital",80),background = "grey",foreground="cyan")
label.pack(anchor='center')
time()

mainloop()