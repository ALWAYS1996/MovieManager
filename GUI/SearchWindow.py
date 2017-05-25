from tkinter import *
from tkinter import ttk, StringVar

class window:

    def __init__(self):
        search = Tk()
        search.title("Search for a movie")
        search.minsize(540, 500)
        search.maxsize(540, 500)
        textLabel = Label(search, text="Movie name", width=15, height=2)
        textLabel.place(relx=0, x=20, y=20)
        textField = Entry(search)
        textField.place(relx=0, x=120,y=30)
        searchButton = Button(search, text="Search", width=10, height=1,command=searchCommand)
        searchButton.place(relx=0, x= 250, y= 25)
        boxLabel = Label (search, text="Search by", width=15, height=2)
        boxLabel.place(relx=0, x=360, y =2)
        value = StringVar()
        box = ttk.Combobox(search, textvariable=value, state="readonly")
        box["values"] = ("Title","Gender")
        box.place(relx=0, x=350, y =30)
        box.current(0)
        search.mainloop()

def searchCommand():
    pass

