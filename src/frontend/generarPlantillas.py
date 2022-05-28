from glob import glob
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
from recuEntitiesBD import *


plantillaSelected = []
parrafoSelected = []

def mensajeOK(mensaje):
    informe  = getattr(messagebox, 'show{}'.format('info'))
    informe("Informe", mensaje)

def mensajeAdvertencia(mensaje):
    advertencia = getattr(messagebox, 'show{}'.format('warning'))
    advertencia("Advertencia", mensaje)
    
def crearPlantilla():
    tituloPlantilla = tb_tituloPlantilla.get()

    if(existePlantilla(tituloPlantilla) == 0):
        insertaPlantilla(tituloPlantilla)
        mensajeOK("Plantilla creada correctamente.")
    else:
        mensajeAdvertencia("Ya existe una plantilla con ese nombre.")

    tb_tituloPlantilla.delete('end', 0)


def crearParrafo():
    tituloParrafo = tb_tituloParrafo.get()

    if(existeParrafo(tituloParrafo, plantillaSelected.id) == 0):
        insertaParrafo(tituloParrafo, 
          tb_introducirParrafo.get("0.0", END), plantillaSelected.id)
        mensajeOK("Párrafo creado correctamente.")
    else:
        mensajeAdvertencia("Ya existe un párrafo con ese nombre.")
    
    tb_tituloParrafo.delete('end', 0)
    tb_introducirParrafo.delete('1.0', END)

def cargarPlantillasBD():
    plantillas = recuPlantillas()
    nombrePlantillas = []
            
    for plantilla in plantillas:
        nombrePlantillas.append(plantilla.titulo)
        
    cboxPlantilla['values'] = nombrePlantillas



def seleccionarPlantilla(event):
    global plantillaSelected
    plantillaSelected = recuPlantilla(tvarPlantilla.get())



ws = Tk()
ws.geometry("750x600")
ws.title("Generador de plantillas")

framePlantilla = Frame()
framePlantilla.pack(side=TOP)
#Título del formulario
lbl_titulo = Label(framePlantilla, text="Crear Plantilla", font="Georgia 16 bold", pady=10)
lbl_titulo.pack()

#Para introducir el nombre de la plantilla
lb_tituloPlantilla = Label(framePlantilla, font="Georgia 13", text="Título: ")
lb_tituloPlantilla.pack(pady=(15,0), side=LEFT)
tb_tituloPlantilla = Entry(framePlantilla, justify="center", width=30, font="Georgia 12")
tb_tituloPlantilla.pack(pady=(15,0), side=LEFT)

#Botón para almacenar la plantilla
btnCrearPlantilla = Button(ws, font="Georgia 13 bold", text ="Crear plantilla", command = crearPlantilla)
btnCrearPlantilla.pack(pady=(15,0))



#Título del formulario
lbl_titulo = Label(ws, text="Crear Párrafo", font="Georgia 16 bold")
lbl_titulo.pack(pady=(70,10))


frameParrafo = Frame()
frameParrafo.pack(side=TOP)

#Label Seleccionar plantilla
lb_tituloPlantillaAModificar = Label(frameParrafo, font="Georgia 13", text="Seleccionar plantilla: ")
lb_tituloPlantillaAModificar.pack(pady=(10,0), side=LEFT)

#Combobox de plantillas
tvarPlantilla = StringVar()
cboxPlantilla = Combobox(frameParrafo, font="Georgia 13", textvariable=tvarPlantilla, width=35, postcommand=cargarPlantillasBD)
cboxPlantilla.pack(pady=(20,0), side=LEFT)
cboxPlantilla.bind('<<ComboboxSelected>>', seleccionarPlantilla)
cboxPlantilla['state'] = 'readonly'

frameParrafo2 = Frame()
frameParrafo2.pack(side=TOP)



frameParrafo3 = Frame()
frameParrafo3.pack(side=TOP)

#Para introducir el nombre del párrafo

lb_tituloParrafo = Label(frameParrafo3, font="Georgia 13", text="Título del párrafo: ")
lb_tituloParrafo.pack(pady=(20,10), side=LEFT)
tb_tituloParrafo = Entry(frameParrafo3, justify="center", width=50, font="Georgia 12")
tb_tituloParrafo.pack(pady=(20,10), side=LEFT)



#Contenido del párrafo
lb_introducirParrafo = Label(ws, text="Contenido inicial del párrafo: ", font="Georgia 13")
lb_introducirParrafo.pack(pady=(30,0))
tb_introducirParrafo = ScrolledText(ws, font="Georgia 12", height=5, width=60, padx=40)
tb_introducirParrafo.pack()
tb_introducirParrafo.insert('end', "Introduce aquí el párrafo...")


#Botón para almacenar el párrafo
btnCrearPlantilla = Button(ws, font="Georgia 13 bold", text ="Crear párrafo", command = crearParrafo)
btnCrearPlantilla.pack(pady=(15,0))

ws.mainloop()