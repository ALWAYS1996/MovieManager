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

            addMovie.mainloop()
        # locations and sizes for windows 10
        else:

            addMovie = Tk()
            addMovie.title("Add a new movie")
            addMovie.minsize(400, 250)
            addMovie.maxsize(400, 250)

            self.textField = Entry(addMovie, width=20)
            self.textField.place(relx=0, x=100, y=15)
            self.textField.focus_set()

            addMovie.mainloop()