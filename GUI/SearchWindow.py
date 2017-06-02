from tkinter import *
from tkinter import ttk, StringVar
import platform
import Domain.ListController

class window:

    def __init__(self):
        #locations and sizes for linux mint
        if platform.system() == "Linux":
            search = Toplevel()
            search.title("Search for a movie")
            search.minsize(580, 330)
            search.maxsize(580, 330)

            self.textField = Entry(search, width=20)
            self.textField.place(relx=0, x=100, y=15)
            self.textField.focus_set()

            textLabel = Label(search, text="Movie name", width=10, height=2)
            textLabel.place(relx=0, x=10, y=10)

            searchButton = Button(search, text="Search", width=10, height=1, command=self.searchCommand)
            searchButton.place(relx=0, x=270, y=10)

            boxLabel = Label (search, text="Search by", width=8, height=2)
            boxLabel.place(relx=0, x=440, y=2)

            value = StringVar()
            box = ttk.Combobox(search, textvariable=value, state="readonly")
            box["values"] = ("Title", "Gender")
            box.place(relx=0, x=390, y=30)
            box.current(0)

            tree = ttk.Treeview(search)
            tree["columns"] = ("Code", "Title", "Gender", "Total", "Subtitled", "Premier")
            tree.place(relx=0, x= 20, y=60)
            tree.column("Code", width=40, anchor="center")
            tree.heading("Code",text="Code")
            tree.column("Title", width=230, anchor="center")
            tree.heading("Title", text="Title")
            tree.column("Gender", width=70, anchor="center")
            tree.heading("Gender", text="Gender")
            tree.column("Total", width=40, anchor="center")
            tree.heading("Total", text="Total")
            tree.column("Subtitled", width=80, anchor="center")
            tree.heading("Subtitled", text="Subtitled")
            tree.column("Premier", width=80, anchor="center")
            tree.heading("Premier", text="Premier")
            tree["show"] = "headings"

            search.mainloop()
            #locations and sizes for windows 10
        elif platform.system() == "Windows":
            search = Toplevel()
            search.title("Search for a movie")
            search.minsize(540, 340)
            search.maxsize(540, 340)

            textLabel = Label(search, text="Movie name", width=15, height=2)
            textLabel.place(relx=0, x=20, y=20)

            self.textField = Entry(search)
            self.textField.place(relx=0, x=120, y=30)

            searchButton = Button(search, text="Search", width=10, height=1, command=self.searchCommand)
            searchButton.place(relx=0, x=250, y=25)

            boxLabel = Label(search, text="Show", width=15, height=2)
            boxLabel.place(relx=0, x=360, y=2)

            value = StringVar()
            self.box = ttk.Combobox(search, textvariable=value, state="readonly")
            self.box["values"] = ("All", "Premier only", "Subbed only", "Premier/Subbed", "Not Premier/Subbed")
            self.box.place(relx=0, x=350, y=30)
            self.box.current(0)

            self.tree = ttk.Treeview(search)
            self.tree["columns"] = ("Code", "Title", "Gender", "Total", "Subtitled", "Premier")
            self.tree.place(relx=0, x=20, y=60)
            self.tree.column("Code", width=40, anchor="center")
            self.tree.heading("Code", text="Code")
            self.tree.column("Title", width=220, anchor="center")
            self.tree.heading("Title", text="Title")
            self.tree.column("Gender", width=70, anchor="center")
            self.tree.heading("Gender", text="Gender")
            self.tree.column("Total", width=40, anchor="center")
            self.tree.heading("Total", text="Total")
            self.tree.column("Subtitled", width=60, anchor="center")
            self.tree.heading("Subtitled", text="Subtitled")
            self.tree.column("Premier", width=60, anchor="center")
            self.tree.heading("Premier", text="Premier")
            self.tree["show"] = "headings"

            search.mainloop()

    def searchCommand(self):
        if self.box.get() == "All":
            auxHead = Domain.ListController.dramaHead
            nodes = Domain.ListController.dramaNodes
            for x in range(0,nodes):
                self.tree.insert("", "end", values=auxHead.data)
                auxHead = auxHead.nextNode
        elif self.box.get() == "Premier only":
            pass
        elif self.box.get() == "Subbed only":
            pass
        elif self.box.get() == "Premier/Subbed":
            pass
        else:
            pass