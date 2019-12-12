from tkinter import *
from tkinter import messagebox
from datetime import datetime
import time
import sqlite3


root = Tk()
root.geometry("{}x{}".format(500, 500))
root.title("Eventer")

# Main Window
lbl0 = Label(root, text="Create New Event")
lbl0.place(rely = 0.05, relx=0.05, relwidth=0.9, relheight=0.1)

lbl1 = Label(root, text="Event:", anchor=E)
lbl1.place(rely = 0.2, relx=0.05, relwidth=0.25, relheight=0.08)
ent1 = Entry(root)
ent1.place(rely = 0.2, relx=0.3, relwidth=0.65, relheight=0.08)

lbl2 = Label(root, text="Description:", anchor=E)
lbl2.place(rely = 0.35, relx=0.05, relwidth=0.25, relheight=0.08)
ent2 = Entry(root)
ent2.place(rely = 0.35, relx=0.3, relwidth=0.65, relheight=0.08)

lbl3 = Label(root, text="Date:", anchor=E)
lbl3.place(rely = 0.5, relx=0.05, relwidth=0.25, relheight=0.08)
ent3 = Entry(root)
ent3.place(rely = 0.5, relx=0.3, relwidth=0.65, relheight=0.08)

root.mainloop()
