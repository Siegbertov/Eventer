from tkinter import *
from tkinter import messagebox
from datetime import datetime
import time
import sqlite3


def create_new():
    nameV = ent1.get()
    descriptionV = ent2.get()
    dateV = ent3.get()

    if nameV == "" or descriptionV == "" or dateV == "":
        messagebox.showerror("Error", "No Empty Entry")
    else:
        conn = sqlite3.connect("events.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS events(name TEXT, description TEXT, date TEXT)")
        insert_txt = "INSERT INTO events(name, description, date) VALUES(?, ?, ?);"
        insert_data = (nameV, descriptionV, dateV)

        c.execute(insert_txt, insert_data)
        conn.commit()
        c.close()
        conn.close()
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)


def show_events(): # TODO change to showing by least closest date
    top = Toplevel()
    top.title("Upcomming Events")
    top.geometry("{}x{}".format(300, 300))
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    getting_txt = "SELECT * FROM events"
    c.execute(getting_txt)
    data = c.fetchall()
    cur = time.strftime("%d/%m/%Y")
    for row in data:
        name, descr, date = row[0], row[1], row[2]
        d1 = datetime.strptime(cur, "%d/%m/%Y")
        d2 = datetime.strptime(date, "%d/%m/%Y")
        lbl_text = str(abs((d2 - d1).days)) + " days left: " + name + ":\n" + descr
        Label(top, text=lbl_text).pack()


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

# Buttons
btn = Button(root, text="Add", command=create_new)
btn.place(relx=0.1, rely=0.7, relheight=0.1, relwidth=0.8)

show_btn = Button(root, text="Show Upcoming Events", command=show_events)
show_btn.place(relx=0.1, rely=0.8, relheight=0.1, relwidth=0.8)

root.mainloop()
