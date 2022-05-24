from tkinter.ttk import Combobox
from tkinter import *

import sys
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
sys.path.insert(0, '../entities')
sys.path.insert(1, '../database')
sys.path.insert(2, '../../src')
from generarArticulo import *
from querysMysql import *

def crearPlantilla():
    tituloPlantilla = tb_tituloPlantilla.get()

    if(existePlantilla(tituloPlantilla) == 0):
        insertaPlantilla(tituloPlantilla)
        informe  = getattr(messagebox, 'show{}'.format('info'))
        informe("Informe", "Plantilla creada correctamente.")
    else:
        advertencia = getattr(messagebox, 'show{}'.format('warning'))
        advertencia("Advertencia", "Ya existe una plantilla con ese nombre.")

    tb_tituloPlantilla.delete(0, 'end')

ws = Tk()
ws.geometry("750x300")
ws.title("Generador de plantillas")

framePlantilla = Frame()
framePlantilla.pack(side=TOP)
#Título del formulario
lbl_titulo = Label(framePlantilla, text="Crear Plantilla", font="Georgia 16 bold", pady=10)
lbl_titulo.pack()

#Para introducir el nombre de la plantilla
lb_tituloPlantilla = Label(framePlantilla, font="Georgia 13", text="Título: ")
lb_tituloPlantilla.pack(pady=(35,10))
tb_tituloPlantilla = Entry(framePlantilla, justify="center", width=50, font="Georgia 12")
tb_tituloPlantilla.pack(pady=(0,10))

#Botón para almacenar la plantilla
btnCrearPlantilla = Button(framePlantilla, font="Georgia 13 bold", text ="Crear plantilla", command = crearPlantilla)
btnCrearPlantilla.pack(pady=(50,10))


ws.mainloop()