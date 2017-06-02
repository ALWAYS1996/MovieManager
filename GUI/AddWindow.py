from tkinter import *
from tkinter import ttk, StringVar
from tkinter.messagebox import *
import platform

path = ""

class window:

    def __init__(self):
        # locations and sizes for linux mint
        if platform.system() == "Linux":

            self.addMovie = Toplevel()
            self.addMovie.title("Add a new movie")
            self.addMovie.minsize(300, 150)
            self.addMovie.maxsize(300, 150)

            self.textField = Entry(self.addMovie, width=20)
            self.textField.place(relx=0, x=10, y=30)

            self.textLabel = Label(self.addMovie, text="Movie name", width=10, height=1)
            self.textLabel.place(relx=0, x=7, y=10)

            self.amountLabel = Label(self.addMovie, text="Amount", width=10, height=1)
            self.amountLabel.place(relx=0, x=200, y=10)

            self.amountField = Entry(self.addMovie, width=8)
            self.amountField.place(relx=0, x=210, y=30)

            self.subbed = IntVar()
            self.premier = IntVar()

            self.isSubbed = Checkbutton(self.addMovie, text="Subtitles", variable=self.subbed)
            self.isSubbed.place(relx=0, x=5, y=60)

            self.isPremier = Checkbutton(self.addMovie, text="Premier", variable=self.premier)
            self.isPremier.place(relx=0, x=5, y=80)

            self.addButton = Button(self.addMovie, text="Insert Movie", command=self.detect)
            self.addButton.place(relx=0, x=125, y=100)

            self.value = StringVar()
            self.box = ttk.Combobox(self.addMovie, textvariable=self.value, state="readonly")
            self.box["values"] = ("Action", "Terror", "Romance", "Animated", "Drama", "Comedy")
            self.box.place(relx=0, x=95, y=70)
            self.box.current(0)

            self.addMovie.mainloop()
        # locations and sizes for windows 10
        elif platform.system() == "Windows":

            self.addMovie = Toplevel()
            self.addMovie.title("Add a new movie")
            self.addMovie.minsize(300, 150)
            self.addMovie.maxsize(300, 150)

            self.textField = Entry(self.addMovie, width=25)
            self.textField.place(relx=0, x=20, y=30)

            self.textLabel = Label(self.addMovie, text="Movie name", width=10, height=1)
            self.textLabel.place(relx=0, x=17, y=8)

            self.amountLabel = Label(self.addMovie, text="Amount", width=10, height=1)
            self.amountLabel.place(relx=0, x=200, y=8)

            self.amountField = Entry(self.addMovie, width=8)
            self.amountField.place(relx=0, x=212, y=30)

            self.subbed = IntVar()
            self.premier = IntVar()

            self.isSubbed = Checkbutton(self.addMovie,text="Subitiles", variable=self.subbed)
            self.isSubbed.place(relx= 0, x=15, y=50)

            self.isPremier = Checkbutton(self.addMovie, text="Premier", variable=self.premier)
            self.isPremier.place(relx=0, x=15, y=70)

            self.addButton = Button(self.addMovie, text="Insert Movie", command=self.detect)
            self.addButton.place(relx=0, x=15, y=100)

            self.value = StringVar()
            self.box = ttk.Combobox(self.addMovie, textvariable=self.value, state="readonly")
            self.box["values"] = ("Drama", "Comedy", "Childish", "Action", "Romance", "Fiction")
            self.box.place(relx=0, x=115, y=65)
            self.box.current(0)

            self.addMovie.mainloop()

    def detect(self):

        global path
        readFile = open(path, "r+")
        reading = [line.rstrip('\n') for line in readFile]
        auxSplit = reading[-1].split(",")
        code = int(auxSplit[0])
        code += 1
        strCode = str(code)

        sub = StringVar
        pre = StringVar
        gender = StringVar

        if self.premier.get() == 1:
            pre = "1"
        else:
            pre = "0"
        if self.subbed.get() == 1:
            sub = "1"
        else:
            sub = "0"

        if self.box.get() == "Drama":
            gender = "1000"
        elif self.box.get() == "Comedy":
            gender = "2000"
        elif self.box.get() == "Childish":
            gender = "3000"
        elif self.box.get() == "Action":
            gender = "4000"
        elif self.box.get() == "Romance":
            gender = "5000"
        else:
            gender = "6000"

        if self.textField.get() == "" or self.amountField.get() == "":
            showwarning("Blank space", "Please don't let any space in blank", parent=self.addMovie)
        elif self.textField.get().find(",") != -1:
            showinfo("Commas", "Commas", parent=self.addMovie)
        else:
            readFile.write(strCode + "," + self.textField.get() + "," + gender + "," + self.amountField.get() + "," + sub + "," + pre + "\n")
            showinfo("Successfully", "Movie inserted correctly", parent=self.addMovie)

def setPath(file):
    global path
    path = file