from tkinter import *
from tkinter.filedialog import askopenfilename

class buttons:

    def __init__(self, window):
        buttonLoadFile = Button(window, text="Load File", width=10, height=2,command=loadFile, fg="blue")
        buttonLoadFile.place(relx=0, x=50, y=50)
        buttonSearchMovie = Button(window, text="Search Movie", width=10, height=2,command=searchMovie, fg="red")
        buttonSearchMovie.place(relx=0, x=150, y=50)
        buttonNewMovie = Button(window, text="New Movie", width=10, height=2,command=newMovie, fg="green")
        buttonNewMovie.place(relx=0, x=250, y=50)

def loadFile():
    Tk().withdraw()
    filename = askopenfilename()
    print(filename)
def searchMovie():
    import GUI.SearchWindow
    auxSearchWindow = GUI.SearchWindow.window()
def newMovie():
    import GUI.AddWindow
    auxAddWindow = GUI.AddWindow.window()

window = Tk()
window.title("Registro Peliculas")
window.maxsize(380,150)
window.minsize(380,150)

bg= PhotoImage(file="background.ppm")
labelBG = Label(window, image=bg)
labelBG.pack()

initButton = buttons(window)

window.mainloop()
