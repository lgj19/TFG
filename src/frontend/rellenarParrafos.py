from docx import Document
from docxcompose.composer import Composer
import sys

from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import *
import math
import codecs

sys.path.insert(0, '../entities')
sys.path.insert(1, '../database')
sys.path.insert(2, '../../src')
from generarArticulo import *
from Plantilla import *
from recuEntitiesBD import *





equipos = [] #Equipos seleccionados del partido
plantillaSelected = Plantilla.Plantilla([-1,False,"nada"]) #Plantilla de redacción

TEMPORADAS = ('1994/95', '1995/96', '1996/97', '1997/98', '1998/99', '1999/00', '2000/01', '2001/02', '2002/03',
              '2003/04', '2004/05', '2005/06', '2006/07', '2007/08', '2008/09', '2009/10', '2010/11', '2011/12',
              '2012/13', '2013/14', '2014/15', '2015/16', '2016/17') #Las temporadas de la liga ACB

def agregarEquipos():
    equipos = []
    nombreEquipos = []
    cboxEquipoLocal.set(''); cboxEquipoVisitante.set('')
    temporada = tvarTemporada.get()[:4]
    
    equipos = recuEqsTemp(temporada)
    
    for equipo in equipos:
        nombreEquipos.append(equipo.nombre)
    cboxEquipoLocal['values'] = cboxEquipoVisitante['values'] = nombreEquipos

def cargarPlantillasBD():
    plantillas = recuPlantillas()
    nombrePlantillas = []
            
    for plantilla in plantillas:
        nombrePlantillas.append(plantilla.titulo)
        
    cboxPlantilla['values'] = nombrePlantillas

def seleccionarPlantilla(event):
    global plantillaSelected
    plantillaSelected = recuPlantilla(tvarPlantilla.get())
    iniciarBotonesCheck()
    

def iniciarBotonesCheck():
    global arrChB, arrVarChB

    Label(ws, font="Georgia 11", text="Seleccionar párrafos: ",
     pady=5, padx=15).grid(row=6, column=0)
    
    arrParrafosLen = len(plantillaSelected.parrafos)
    arrChB = [Checkbutton] * arrParrafosLen
    arrVarChB = [IntVar] * arrParrafosLen
    
    for i in range(len(arrVarChB)): 
        arrVarChB[i] = IntVar()
    
    for i in range(arrParrafosLen):
        arrChB[i] = Checkbutton(ws, font="Georgia 10",
                     text=plantillaSelected.parrafos[i].tipoParrafo,
                     variable=arrVarChB[i], onvalue=1, offvalue=0)
    
    for i in range(len(arrChB)):
        arrChB[i].grid(row=7+math.trunc(i/3), column=i%3)
    
def seleccionartiposParrafos():
    global arrChB, arrVarChB
    tiposParrafos = []
    for i in range(len(arrVarChB)):
        if(arrVarChB[i].get() == 1):
            tiposParrafos.append(arrChB[i].cget("text"))
    return tiposParrafos

def informeOK(mensaje):
    informe  = getattr(messagebox, 'show{}'.format('info'))
    informe("Informe", mensaje)

def generarTexto():
    nombreEqL = tvarEquipoLocal.get()
    nombreEqV = tvarEquipoVisitante.get()
    tituloPlant = tvarPlantilla.get()
    temporada = tvarTemporada.get()[:4]
    nombreArticulo = entry_nombreArticulo.get()

    tiposParrafos = seleccionartiposParrafos()
    
    articuloFinal = Document()
    articuloFinal.add_heading(nombreArticulo.upper())
    composer = Composer(articuloFinal)
    
    parrafos = inyeccionPlantilla(nombreEqL, nombreEqV,
                 temporada, tituloPlant, tiposParrafos, plantillaSelected)
    composer.append(parrafos)
    
    pathFile = "../textosGenerados/{}.docx".format(nombreArticulo)
    composer.save(pathFile)
    
    informeOK("Artículo generado correctamente.")
    
    


ws = Tk()
ws.geometry("700x550")
ws.title("Generador de párrafos de la ACB")

#Título de la sección del partido
Label(ws, text="Datos del partido", font="Georgia 16 bold", pady=15).grid(row=0, column=1)

#Nombre del combobox para seleccionar el año de la temporada
lb_temporada = Label(ws, font="Georgia 11", text="Temporada: ", pady=5, padx=15).grid(row=1, column=0)

#Combobox de la temporada con los años y el manejador al seleccionar un año
tvarTemporada = StringVar()
cboxTemporada = Combobox(ws, font="Georgia 11", textvariable=tvarTemporada)
cboxTemporada.grid(row=1, column=1)
cboxTemporada.bind('<<ComboboxSelected>>', agregarEquipos)
cboxTemporada['state'] = 'readonly'
cboxTemporada['values'] = TEMPORADAS

#Selección del equipo local
lbl_equipoLocal = Label(ws, font="Georgia 11", text="Equipo local: ", pady=5, padx=15).grid(row=2, column=0)

#Combobox del equipo local
tvarEquipoLocal = StringVar()
cboxEquipoLocal = Combobox(ws, font="Georgia 11", textvariable=tvarEquipoLocal, width=35)
cboxEquipoLocal.grid(row=2, column=1)
cboxEquipoLocal['state'] = 'readonly'

#Selección del equipo visitante
lbl_equipoVisitante = Label(ws, font="Georgia 11", text="Equipo visitante: ", pady=5, padx=15).grid(row=3, column=0)

#Combobox del equipo visitante
tvarEquipoVisitante = StringVar()
cboxEquipoVisitante = Combobox(ws, font="Georgia 11", textvariable=tvarEquipoVisitante, width=35)
cboxEquipoVisitante.grid(row=3, column=1)
cboxEquipoVisitante['state'] = 'readonly'

#Sección segunda para seleccionar los párrafos 
Label(ws, text="Selección de párrafos", font="Georgia 16 bold", pady=30).grid(row=4, column=1)

#Label plantilla
lbl_plantilla = Label(ws, font="Georgia 11", text="Plantilla: ", pady=5, padx=15).grid(row=5, column=0)

#ComboBox plantilla
tvarPlantilla = StringVar()
cboxPlantilla = Combobox(ws, font="Georgia 11", textvariable=tvarPlantilla, width=35, postcommand=cargarPlantillasBD)
cboxPlantilla.grid(row=5, column=1)
cboxPlantilla.bind('<<ComboboxSelected>>', seleccionarPlantilla)
cboxPlantilla['state'] = 'readonly'
arrChB = []
arrVarChB = []

#Botón de Generar plantilla
btnGenerarPlantilla = Button( text ="Generar texto", font="Georgia 11" , command = generarTexto)
btnGenerarPlantilla.grid(row=16, column=1, pady=15)

#Label plantilla
lbl_nombreArticulo = Label(ws, font="Georgia 11", text="Nombre del artículo: ", pady=25, padx=15).grid(row=15, column=0)
entry_nombreArticulo = Entry(ws, justify="center", width=40, font="Georgia 11")
entry_nombreArticulo.grid(row=15, column=1)
ws.mainloop()