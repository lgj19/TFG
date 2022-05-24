from tkinter import *
import re

import sys
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
sys.path.insert(0, '../entities')
sys.path.insert(1, '../database')
sys.path.insert(2, '../../src')
from generarArticulo import *
from querysMysql import *




def cargarPlantillasBD():
    plantillas = recuPlantillas()
    nombrePlantillas = []
            
    for plantilla in plantillas:
        nombrePlantillas.append(plantilla.titulo)
        
    cboxPlantilla['values'] = nombrePlantillas

def seleccionarPlantilla(event):
    global plantillaSelected
    plantillaSelected = recuPlantilla(tvarPlantilla.get())


def generarParrafo():
    print("Párrafo generado!")

def guardarParrafo():
    tituloPlantilla = tvarPlantilla.get()
    plantilla = recuPlantilla(tituloPlantilla)
    tituloParrafo = tb_tituloParrafo.get()

    contenidoParrafo = str(tb_parrafoGenerado.get("1.0", END))
    rowsAffected = insertaParrafo(tituloParrafo, contenidoParrafo, int(plantilla.id))
    
    if(rowsAffected == 1):
        informe  = getattr(messagebox, 'show{}'.format('info'))
        informe("Informe", "Parrafo añadido correctamente.")
    else:
        advertencia = getattr(messagebox, 'show{}'.format('warning'))
        advertencia("Advertencia", "El párrafo no se ha podido añadir.")




ws = Tk()
ws.geometry("950x750")
ws.title("Generador de párrafos")


frameParrafo = Frame()
frameParrafo.pack(side=TOP)

#Título del formulario
lbl_titulo = Label(frameParrafo, text="Crear Párrafo", font="Georgia 16 bold")
lbl_titulo.pack(pady=(30,30))

#Para introducir el nombre del párrafo
lb_tituloParrafo = Label(frameParrafo, font="Georgia 13", text="Título del párrafo: ")
lb_tituloParrafo.pack()
tb_tituloParrafo = Entry(frameParrafo, justify="center", width=50, font="Georgia 12")
tb_tituloParrafo.pack(pady=(0,10))

#Contenido del párrafo
lb_introducirParrafo = Label(frameParrafo, text="Contenido inicial del párrafo: ", font="Georgia 13")
lb_introducirParrafo.pack(pady=(10,0))
tb_introducirParrafo = ScrolledText(frameParrafo, font="Georgia 12", height=5, width=60, padx=40)
tb_introducirParrafo.pack()
tb_introducirParrafo.insert('end', "Introduce aquí el párrafo...")


#Label generar texto
lb_tituloGenerarTexto = Label(frameParrafo, font="Georgia 13", text="Opciones de generación de texto: ")
lb_tituloGenerarTexto.pack(pady=(30,0))
#Opciones de generación de texto
varSinonimosCB = IntVar(value=1)
sinonimosCB = Checkbutton(frameParrafo, font="Georgia 12", text="Sinónimos", variable=varSinonimosCB, onvalue=1, offvalue=0)
sinonimosCB.pack()
varSintaxisCB = IntVar(value=0)
sintaxisCB = Checkbutton(frameParrafo, font="Georgia 12", text="Sintaxis", variable=varSintaxisCB, onvalue=1, offvalue=0)
sintaxisCB.pack()

#Botón para guardar párrafo en la plantilla
btnGuardarParrafo = Button(frameParrafo, font="Georgia 13 bold", text ="Generar párrafo", command = generarParrafo)
btnGuardarParrafo.pack(pady=(0,20))

#Label Texto generado
lb_parrafoGenerado = Label(frameParrafo, font="Georgia 13", text="Párrafo generado: ")
lb_parrafoGenerado.pack(pady=(10,0))

#Contenido del texto generado
tb_parrafoGenerado = ScrolledText(frameParrafo, font="Georgia 12", height=5, width=60, padx=40)
tb_parrafoGenerado.insert('end', "Esto es un ejemplo para comprobar")
tb_parrafoGenerado.configure(state="disabled")
tb_parrafoGenerado.pack()

#Label Seleccionar plantilla
lb_tituloPlantillaAGuardar = Label(frameParrafo, font="Georgia 13", text="Seleccionar plantilla donde introducir el párrafo: ")
lb_tituloPlantillaAGuardar.pack(pady=(30,0))

#Combobox de plantillas
tvarPlantilla = StringVar()
cboxPlantilla = Combobox(frameParrafo, font="Georgia 13", textvariable=tvarPlantilla, width=35, postcommand=cargarPlantillasBD)
cboxPlantilla.pack()
cboxPlantilla.bind('<<ComboboxSelected>>', seleccionarPlantilla)
cboxPlantilla['state'] = 'readonly'

#Botón para guardar párrafo en la plantilla
btnGuardarParrafo = Button(frameParrafo, font="Georgia 13 bold", text ="Guardar párrafo", command = guardarParrafo)
btnGuardarParrafo.pack(pady=(30,20))

ws.mainloop()