from tkinter import *
from tkinter import ttk, StringVar
from tkinter.messagebox import *
import platform
import Domain.ListController

class window:

    def __init__(self):
        #locations and sizes for linux mint
        if platform.system() == "Linux":
            self.search = Toplevel()
            self.search.title("Search for a movie")
            self.search.minsize(580, 330)
            self.search.maxsize(580, 330)

            self.textField = Entry(self.search, width=20)
            self.textField.place(relx=0, x=100, y=15)
            self.textField.focus_set()

            self.textLabel = Label(self.search, text="Movie name", width=10, height=2)
            self.textLabel.place(relx=0, x=10, y=10)

            self.searchButton = Button(self.search, text="Search", width=10, height=1, command=self.searchCommand)
            self.searchButton.place(relx=0, x=270, y=10)

            self.boxLabel = Label (self.search, text="Show", width=8, height=2)
            self.boxLabel.place(relx=0, x=440, y=2)

            self.value = StringVar()
            self.box = ttk.Combobox(self.search, textvariable=self.value, state="readonly")
            self.box["values"] = ("All", "Premier only", "Subbed only", "Premier/Subbed", "Not Premier/Subbed")
            self.box.place(relx=0, x=390, y=30)
            self.box.current(0)

            self.tree = ttk.Treeview(self.search)
            self.tree["columns"] = ("Code", "Title", "Gender", "Total", "Subtitled", "Premier")
            self.tree.place(relx=0, x= 20, y=60)
            self.tree.column("Code", width=40, anchor="center")
            self.tree.heading("Code",text="Code")
            self.tree.column("Title", width=230, anchor="center")
            self.tree.heading("Title", text="Title")
            self.tree.column("Gender", width=70, anchor="center")
            self.tree.heading("Gender", text="Gender")
            self.tree.column("Total", width=40, anchor="center")
            self.tree.heading("Total", text="Total")
            self.tree.column("Subtitled", width=80, anchor="center")
            self.tree.heading("Subtitled", text="Subtitled")
            self.tree.column("Premier", width=80, anchor="center")
            self.tree.heading("Premier", text="Premier")
            self.tree["show"] = "headings"

            self.search.mainloop()
            #locations and sizes for windows 10
        elif platform.system() == "Windows":
            self.search = Toplevel()
            self.search.title("Search for a movie")
            self.search.minsize(540, 340)
            self.search.maxsize(540, 340)

            self.textLabel = Label(self.search, text="Movie name", width=15, height=2)
            self.textLabel.place(relx=0, x=20, y=20)

            self.textField = Entry(self.search)
            self.textField.place(relx=0, x=120, y=30)

            self.searchButton = Button(self.search, text="Search", width=10, height=1, command=self.searchCommand)
            self.searchButton.place(relx=0, x=250, y=25)

            self.boxLabel = Label(self.search, text="Show", width=15, height=2)
            self.boxLabel.place(relx=0, x=360, y=2)

            self.value = StringVar()
            self.box = ttk.Combobox(self.search, textvariable=self.value, state="readonly")
            self.box["values"] = ("All", "Premier only", "Subbed only", "Premier/Subbed", "Not Premier/Subbed")
            self.box.place(relx=0, x=350, y=30)
            self.box.current(0)

            self.tree = ttk.Treeview(self.search)
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

            self.search.mainloop()

    def searchCommand(self):
        self.tree.delete(*self.tree.get_children())

        if self.box.get() == "All":
            searchFlag = False
            if self.textField.get() != "":
                searchFlag = True
            for x in range (0,6):
                auxHead = None
                nodes = None

                sub = StringVar
                pre = StringVar
                gender = StringVar

                if x == 0:
                    gender = "Drama"
                    auxHead = Domain.ListController.dramaHead
                    nodes = Domain.ListController.dramaNodes
                elif x == 1:
                    gender = "Comedy"
                    auxHead = Domain.ListController.comedyHead
                    nodes = Domain.ListController.comedyNodes
                elif x == 2:
                    gender = "Childish"
                    auxHead = Domain.ListController.childishHead
                    nodes = Domain.ListController.childishNodes
                elif x == 3:
                    gender = "Action"
                    auxHead = Domain.ListController.actionHead
                    nodes = Domain.ListController.actionNodes
                elif x == 4:
                    gender = "Romance"
                    auxHead = Domain.ListController.romanceHead
                    nodes = Domain.ListController.romanceNodes
                else:
                    gender = "Fiction"
                    auxHead = Domain.ListController.fictionHead
                    nodes = Domain.ListController.fictionNodes

                for x in range(0,nodes):

                    if auxHead.data[4] == "1":
                        sub = "Yes"
                    else:
                        sub = "No"

                    if auxHead.data[5] == "1":
                        pre = "Yes"
                    else:
                        pre = "No"

                    if searchFlag:
                        if auxHead.data[1].lower().find(self.textField.get().lower()) != -1 :
                            self.tree.insert("", "end", values=(auxHead.data[0], auxHead.data[1], gender, auxHead.data[3], sub, pre))
                            auxHead = auxHead.nextNode
                        else:
                            auxHead = auxHead.nextNode
                    else:
                        self.tree.insert("", "end", values=(auxHead.data[0], auxHead.data[1], gender, auxHead.data[3], sub, pre))
                        auxHead = auxHead.nextNode
            if self.tree.get_children() == ():
                showwarning("No matches","No results were found", parent=self.search)

        elif self.box.get() == "Premier only":
            pass
        elif self.box.get() == "Subbed only":
            pass
        elif self.box.get() == "Premier/Subbed":
            pass
        else:
            pass