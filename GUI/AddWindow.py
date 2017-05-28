from tkinter import *
import platform
class window:
    def __init__(self):
        # locations and sizes for linux mint
        if platform.system() == "linux":

            addMovie = Tk()
            addMovie.title("Add a new movie")
            addMovie.minsize(400, 250)
            addMovie.maxsize(400, 250)

            self.textField = Entry(addMovie, width=20)
            self.textField.place(relx=0, x=100, y=15)
            self.textField.focus_set()

            textLabel = Label(addMovie, text="Movie name", width=10, height=1)
            textLabel.place(relx=0, x=7, y=8)

            self.subbed = IntVar()
            self.premier = IntVar()

            isSubbed = Checkbutton(addMovie, text="Subitiles", variable=self.subbed)
            isSubbed.place(relx=0, x=5, y=50)

            isPremier = Checkbutton(addMovie, text="Premier", variable=self.premier)
            isPremier.place(relx=0, x=5, y=70)

            addButton = Button(addMovie, text="Insert Movie", command=self.detect)
            addButton.place(relx=0, x=5, y=100)

            addMovie.mainloop()
        # locations and sizes for windows 10
        elif platform.system() == "Windows":

            addMovie = Tk()
            addMovie.title("Add a new movie")
            addMovie.minsize(400, 250)
            addMovie.maxsize(400, 250)

            self.textField = Entry(addMovie, width=20)
            self.textField.place(relx=0, x=10, y=30)
            self.textField.focus_set()

            textLabel = Label(addMovie, text="Movie name", width=10, height=1)
            textLabel.place(relx=0, x=7, y=8)

            self.subbed = IntVar()
            self.premier = IntVar()

            isSubbed = Checkbutton(addMovie,text="Subitiles", variable=self.subbed)
            isSubbed.place(relx= 0, x=5, y=50)

            isPremier = Checkbutton(addMovie, text="Premier", variable=self.premier)
            isPremier.place(relx=0, x=5, y=70)

            addButton = Button(addMovie, text="Insert Movie", command=self.detect)
            addButton.place(relx=0, x=5, y=100)

            addMovie.mainloop()

    def detect(self):
        if self.premier.get() == 1:
            print("Premier")
        else:
            print("Not premier")
        if self.subbed.get() == 1:
            print("Subbed")
        else:
            print("Not Subbed")
        print(self.textField.get())

ventana = window()