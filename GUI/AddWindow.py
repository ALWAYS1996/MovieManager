from tkinter import *
from tkinter import ttk, StringVar
import platform

class window:
    def __init__(self):
        # locations and sizes for linux mint
        if platform.system() == "Linux":

            self.addMovie = Toplevel()
            self.addMovie.title("Add a new movie")
            self.addMovie.minsize(300, 150)
            self.addMovie.maxsize(300, 150)

            self.textField = Entry(self.addMovie, width=20)
            self.textField.place(relx=0, x=100, y=15)
            self.textField.focus_set()

            self.textLabel = Label(self.addMovie, text="Movie name", width=10, height=1)
            self.textLabel.place(relx=0, x=7, y=17)

            self.subbed = IntVar()
            self.premier = IntVar()

            self.isSubbed = Checkbutton(self.addMovie, text="Subitiles", variable=self.subbed)
            self.isSubbed.place(relx=0, x=5, y=40)

            self.isPremier = Checkbutton(self.addMovie, text="Premier", variable=self.premier)
            self.isPremier.place(relx=0, x=5, y=60)

            self.addButton = Button(self.addMovie, text="Insert Movie", command=self.detect)
            self.addButton.place(relx=0, x=125, y=80)

            self.value = StringVar()
            self.box = ttk.Combobox(self.addMovie, textvariable=self.value, state="readonly")
            self.box["values"] = ("Action", "Terror", "Romance", "Animated", "Drama", "Comedy")
            self.box.place(relx=0, x=95, y=50)
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
            self.textField.focus_set()

            self.textLabel = Label(self.addMovie, text="Movie name", width=10, height=1)
            self.textLabel.place(relx=0, x=17, y=8)

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
            self.box["values"] = ("Action", "Terror", "Romance", "Animated", "Drama", "Comedy")
            self.box.place(relx=0, x=115, y=65)
            self.box.current(0)

            self.addMovie.mainloop()

    def detect(self):
        print(self.premier.get())
        if self.premier.get() == 1:
            print("Premier")
        else:
            print("Not premier")
        if self.subbed.get() == 1:
            print("Subbed")
        else:
            print("Not Subbed")
        print(self.textField.get())