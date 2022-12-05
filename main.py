from doctest import master
from tkinter import *
from window import *

def main():
    root = Tk()
    root.wm_title("Base de Datos") #se le coloca el titulo de la interfaz grafica de usuario llamando 
    call_loop = Window(root)
    call_loop.mainloop()

if __name__ == "__main__":
    main()