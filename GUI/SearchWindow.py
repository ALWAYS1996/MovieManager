from tkinter import *
from tkinter import ttk, StringVar

class window:

    def __init__(self):

        search = Tk()
        search.title("Search for a movie")
        search.minsize(540, 340)
        search.maxsize(540, 340)

        textLabel = Label(search, text="Movie name", width=15, height=2)
        textLabel.place(relx=0, x=20, y=20)

        textField = Entry(search)
        textField.place(relx=0, x=120, y=30)

        searchButton = Button(search, text="Search", width=10, height=1, command=searchCommand)
        searchButton.place(relx=0, x=250, y=25)

        boxLabel = Label (search, text="Search by", width=15, height=2)
        boxLabel.place(relx=0, x=360, y=2)

        value = StringVar()
        box = ttk.Combobox(search, textvariable=value, state="readonly")
        box["values"] = ("Title", "Gender")
        box.place(relx=0, x=350, y =30)
        box.current(0)

        tree = ttk.Treeview(search)
        tree["columns"] = ("Code", "Title", "Gender", "Total", "Subtitled", "Premier")
        tree.place(relx=0, x= 20, y=60)
        tree.column("Code", width=40, anchor ="center")
        tree.heading("Code",text="Code")
        tree.column("Title", width=220, anchor="center")
        tree.heading("Title", text="Title")
        tree.column("Gender", width=70, anchor="center")
        tree.heading("Gender", text="Gender")
        tree.column("Total", width=40, anchor="center")
        tree.heading("Total", text="Total")
        tree.column("Subtitled", width=60, anchor="center")
        tree.heading("Subtitled", text="Subtitled")
        tree.column("Premier", width=60, anchor="center")
        tree.heading("Premier", text="Premier")
        tree["show"] = "headings"

        search.mainloop()

def searchCommand():
    pass

