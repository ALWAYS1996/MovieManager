from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
import GUI.SearchWindow
import GUI.AddWindow
import Domain.ListController

file = ""

class buttons:

    def __init__(self, window):
        buttonLoadFile = Button(window, text="Load File", width=10, height=2,command=loadFile, fg="blue")
        buttonLoadFile.place(relx=0, x=50, y=50)
        buttonSearchMovie = Button(window, text="Search Movie", width=10, height=2,command=searchMovie, fg="red")
        buttonSearchMovie.place(relx=0, x=150, y=50)
        buttonNewMovie = Button(window, text="New Movie", width=10, height=2,command=newMovie, fg="green")
        buttonNewMovie.place(relx=0, x=250, y=50)

def loadFile():
    global file
    savedFile = file
    Tk().withdraw()
    file = askopenfilename()
    if file.endswith(".csv"):
        showinfo("File info", "File loaded successfully")
        Domain.ListController.initalizeList(file)
        GUI.AddWindow.setPath(file)
    else:
        showerror("File error", "File format not valid")
        file = savedFile

def searchMovie():
    global file
    if file != "":
        auxSearchWindow = GUI.SearchWindow.window()
    else:
        showerror("File error", "No file loaded")

def newMovie():
    global file
    if file != "":
        auxAddWindow = GUI.AddWindow.window()
    else:
        showerror("File error", "No file loaded")

window = Tk()
window.title("Registro Peliculas")
window.maxsize(380,150)
window.minsize(380,150)

bg= PhotoImage(file="background.ppm")
labelBG = Label(window, image=bg)
labelBG.pack()

initButton = buttons(window)

window.mainloop()