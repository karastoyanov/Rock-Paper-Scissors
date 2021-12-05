import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from PIL import ImageTk
import sys
import random

win = Tk()

x = IntVar()
x.set(1)
def add():
    x.set(x.get() + 1)

label = Label(win, textvariable=x)
label.pack()

button = Button(win, text="Increment", command=add)
button.pack()

win.mainloop()
