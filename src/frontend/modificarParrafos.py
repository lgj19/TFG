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
from recuEntitiesBD import *
from GLNFunctions import *




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
    sinonimos = []
    cadena = "\t\t\tPALABRAS PARECIDAS:\n\n"
    splitPalabras = tb_sinonimos.get().split(", ")
    
    for palabra in splitPalabras:
        sinonimos = obtenerSinonimos(palabra)
        cadena += palabra + ": { "
        for sinonimo in sinonimos:
            cadena += sinonimo + ", "
        if(cadena[-2] == ','):
            cadena = cadena[:-2]
        cadena += "}\n\n"
    tb_sugerencias.insert("1.0", cadena)

    

def guardarParrafo():
    tituloPlantilla = tvarPlantilla.get()
    plantilla = recuPlantilla(tituloPlantilla)
    tituloParrafo = tvarParrafo.get()

    contenidoParrafo = str(tb_introducirParrafo.get("0.0", END))
    print("contenido del parrafo: " + contenidoParrafo)
    rowsAffected = modificaParrafo(tituloParrafo, contenidoParrafo, plantilla.id)
    
    if(rowsAffected == 1):
        informe  = getattr(messagebox, 'show{}'.format('info'))
        informe("Informe", "Parrafo añadido correctamente.")
    else:
        advertencia = getattr(messagebox, 'show{}'.format('warning'))
        advertencia("Advertencia", "El párrafo no se ha podido añadir.")

def cargarParrafosBD():
    parrafos = recuParrafos(plantillaSelected.id)
    nombreParrafos = []

    for parrafo in parrafos:
        nombreParrafos.append(parrafo.tipoParrafo)
    cboxParrafo['values'] = nombreParrafos

def seleccionarParrafo(event):
    global parrafoSelected
    parrafoSelected = recuParrafo(tvarParrafo.get())
    tb_introducirParrafo.delete("0.0", END)
    tb_introducirParrafo.insert('end', parrafoSelected.contenido)

ws = Tk()
ws.geometry("950x750")
ws.title("Modificador de párrafos")


frameSeleccionPlantilla = Frame()
frameSeleccionPlantilla.pack(side=TOP)

#Título del formulario
lbl_titulo = Label(frameSeleccionPlantilla, text="Modificar Párrafo", font="Georgia 16 bold")
lbl_titulo.pack(pady=(30,30))


#Label Seleccionar plantilla
lb_tituloPlantillaAGuardar = Label(frameSeleccionPlantilla, font="Georgia 13", text="Seleccionar plantilla: ")
lb_tituloPlantillaAGuardar.pack(pady=(20,0), side=LEFT)

#Combobox de plantillas
tvarPlantilla = StringVar()
cboxPlantilla = Combobox(frameSeleccionPlantilla, font="Georgia 13", textvariable=tvarPlantilla, width=35, postcommand=cargarPlantillasBD)
cboxPlantilla.pack(pady=(20,0), side=LEFT)
cboxPlantilla.bind('<<ComboboxSelected>>', seleccionarPlantilla)
cboxPlantilla['state'] = 'readonly'

frameSeleccionParrafo = Frame()
frameSeleccionParrafo.pack(side=TOP)

#Label Seleccionar párrafos
lb_tituloParrafoAModificar = Label(frameSeleccionParrafo, font="Georgia 13", text="Seleccionar párrafo: ")
lb_tituloParrafoAModificar.pack(pady=(10,0), side=LEFT)

#Combobox de párrafos
tvarParrafo = StringVar()
cboxParrafo = Combobox(frameSeleccionParrafo, font="Georgia 13", textvariable=tvarParrafo, width=35, postcommand=cargarParrafosBD)
cboxParrafo.pack(pady=(20,0), side=LEFT)
cboxParrafo.bind('<<ComboboxSelected>>', seleccionarParrafo)
cboxParrafo['state'] = 'readonly'

#Para introducir el nombre del párrafo
frameCrearParrafo = Frame()
frameCrearParrafo.pack(side=TOP)

#Contenido del párrafo
lb_introducirParrafo = Label(frameCrearParrafo, text="Contenido inicial del párrafo: ", font="Georgia 13")
lb_introducirParrafo.pack(pady=(10,0))
tb_introducirParrafo = ScrolledText(frameCrearParrafo, font="Georgia 12", height=5, width=60, padx=40)
tb_introducirParrafo.pack()
tb_introducirParrafo.insert('end', "Introduce aquí el párrafo...")

#Label Texto generado
lb_sugerencias = Label(frameCrearParrafo, font="Georgia 13", text="Sugerencias: ")
lb_sugerencias.pack(pady=(10,0))

#Contenido del texto generado
tb_sugerencias = ScrolledText(frameCrearParrafo, font="Georgia 12", height=5, width=60, padx=40)
tb_sugerencias.pack()

#Label generar texto
frameSinonimos = Frame()
frameSinonimos.pack(side=TOP)
lb_tituloGenerarTexto = Label(frameSinonimos, font="Georgia 13", text="Opciones de generación de texto: ")
lb_tituloGenerarTexto.pack(pady=(30,0))
#Opciones de generación de texto
lb_sinonimos = Label(frameSinonimos, font="Georgia 13", text="Buscar sinónimos: ")
lb_sinonimos.pack(pady=(10,0), side=LEFT)

tb_sinonimos = Entry(frameSinonimos, justify="center", width=50, font="Georgia 12", )
tb_sinonimos.pack(pady=(10,0), side=LEFT)
tb_sinonimos.insert(0,"Formato: adj1, adj2, ..., adjN")

#Botón para guardar párrafo en la plantilla
btnGuardarParrafo = Button(ws, font="Georgia 13 bold", text ="Generar sugerencias", command = generarSugerencias)
btnGuardarParrafo.pack(pady=(20,30))


framePlantilla = Frame(ws)
framePlantilla.pack(side=TOP)



#Botón para guardar párrafo en la plantilla
btnGuardarParrafo = Button(framePlantilla, font="Georgia 13 bold", text ="Guardar párrafo", command = guardarParrafo)
btnGuardarParrafo.pack(pady=(20,30))

ws.mainloop()