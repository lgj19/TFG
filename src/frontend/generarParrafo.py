from tkinter import *
import re

import sys
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
sys.path.insert(0, '../entities')
sys.path.insert(1, '../database')
sys.path.insert(2, '../../src')
sys.path.insert(3, '../GLN')
from generarArticulo import *
from querysMysql import *
from generateText import *




def cargarPlantillasBD():
    plantillas = recuPlantillas()
    nombrePlantillas = []
            
    for plantilla in plantillas:
        nombrePlantillas.append(plantilla.titulo)
        
    cboxPlantilla['values'] = nombrePlantillas

def seleccionarPlantilla(event):
    global plantillaSelected
    plantillaSelected = recuPlantilla(tvarPlantilla.get())


def generarSugerencias():
    print("Introducir sugerencias.")
    

def guardarParrafo():
    tituloPlantilla = tvarPlantilla.get()
    plantilla = recuPlantilla(tituloPlantilla)
    tituloParrafo = tb_tituloParrafo.get()

    contenidoParrafo = str(tb_introducirParrafo.get("1.0", END))
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
frameCrearParrafo = Frame(frameParrafo)
frameCrearParrafo.pack(side=TOP)
lb_tituloParrafo = Label(frameCrearParrafo, font="Georgia 13", text="Título del párrafo: ")
lb_tituloParrafo.pack(side=LEFT)
tb_tituloParrafo = Entry(frameCrearParrafo, justify="center", width=50, font="Georgia 12")
tb_tituloParrafo.pack(pady=(0,10), side=LEFT)

#Contenido del párrafo
lb_introducirParrafo = Label(frameParrafo, text="Contenido inicial del párrafo: ", font="Georgia 13")
lb_introducirParrafo.pack(pady=(10,0))
tb_introducirParrafo = ScrolledText(frameParrafo, font="Georgia 12", height=5, width=60, padx=40)
tb_introducirParrafo.pack()
tb_introducirParrafo.insert('end', "Introduce aquí el párrafo...")

#Label Texto generado
lb_sugerencias = Label(frameParrafo, font="Georgia 13", text="Sugerencias: ")
lb_sugerencias.pack(pady=(10,0))

#Contenido del texto generado
tb_sugerencias = ScrolledText(frameParrafo, font="Georgia 12", height=5, width=60, padx=40)
tb_sugerencias.pack()

#Label generar texto
frameSinonimos = Frame(frameParrafo)
frameSinonimos.pack(side=TOP)
lb_tituloGenerarTexto = Label(frameSinonimos, font="Georgia 13", text="Opciones de generación de texto: ")
lb_tituloGenerarTexto.pack(pady=(30,0))
#Opciones de generación de texto
lb_sinonimos = Label(frameSinonimos, font="Georgia 13", text="Buscar sinónimos: ")
lb_sinonimos.pack(pady=(10,0), side=LEFT)

tb_sinonimos = Entry(frameSinonimos, justify="center", width=50, font="Georgia 12", )
tb_sinonimos.pack(pady=(10,0), side=LEFT)
tb_sinonimos.insert(0,"Formato: adj1, adj2, ..., adjN")

frameSintaxis = Frame(frameParrafo)
frameSintaxis.pack(side=TOP)

lb_sintaxis = Label(frameSintaxis, font="Georgia 13", text="Modificar sintaxis en una frase: ")
lb_sintaxis.pack(pady=(10,0), side=LEFT)

tb_sintaxis = Entry(frameSintaxis, justify="center", width=50, font="Georgia 12", )
tb_sintaxis.pack(pady=(10,0), side=LEFT)
tb_sintaxis.insert(0,"Esta frase es un ejemplo.")


#Botón para guardar párrafo en la plantilla
btnGuardarParrafo = Button(frameParrafo, font="Georgia 13 bold", text ="Generar sugerencias", command = generarSugerencias)
btnGuardarParrafo.pack(pady=(20,30))


framePlantilla = Frame(frameParrafo)
framePlantilla.pack(side=TOP)

#Label Seleccionar plantilla
lb_tituloPlantillaAGuardar = Label(framePlantilla, font="Georgia 13", text="Seleccionar plantilla: ")
lb_tituloPlantillaAGuardar.pack(pady=(20,0), side=LEFT)

#Combobox de plantillas
tvarPlantilla = StringVar()
cboxPlantilla = Combobox(framePlantilla, font="Georgia 13", textvariable=tvarPlantilla, width=35, postcommand=cargarPlantillasBD)
cboxPlantilla.pack(pady=(20,0), side=LEFT)
cboxPlantilla.bind('<<ComboboxSelected>>', seleccionarPlantilla)
cboxPlantilla['state'] = 'readonly'

#Botón para guardar párrafo en la plantilla
btnGuardarParrafo = Button(frameParrafo, font="Georgia 13 bold", text ="Guardar párrafo", command = guardarParrafo)
btnGuardarParrafo.pack(pady=(20,30))

ws.mainloop()