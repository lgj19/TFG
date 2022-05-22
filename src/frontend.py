from tkinter import *
from tkinter.ttk import Combobox
import entities.Plantilla as Plantilla
from generarArticulo import *
import math

from querysMysql import *


equipos = [] #Equipos seleccionados del partido
plantillaSelected = Plantilla.Plantilla([-1,False,"nada"]) #Plantilla de redacción

TEMPORADAS = ('1994/95', '1995/96', '1996/97', '1997/98', '1998/99', '1999/00', '2000/01', '2001/02', '2002/03',
              '2003/04', '2004/05', '2005/06', '2006/07', '2007/08', '2008/09', '2009/10', '2010/11', '2011/12',
              '2012/13', '2013/14', '2014/15', '2015/16', '2016/17') #Las temporadas de la liga ACB

def agregarEquipos(event):
    equipos = []
    cboxEquipoLocal.set(''); cboxEquipoVisitante.set('')
    temporada = tvarTemporada.get()[:4]
    nombreEquipos = []

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
    #CheckButtons --> párrafos
    Label(ws, text="Seleccionar párrafos: ", pady=5, padx=15).grid(row=6, column=0)
    
    arrParrafosLen = len(plantillaSelected.parrafos)
    
    arrChB = [Checkbutton] * arrParrafosLen
    arrVarChB = [IntVar] * arrParrafosLen
    for i in range(len(arrVarChB)): arrVarChB[i] = IntVar()
    
    for i in range(arrParrafosLen):
        arrChB[i] = Checkbutton(ws, text=plantillaSelected.parrafos[i].tipoParrafo,
                                variable=arrVarChB[i], onvalue=1, offvalue=0)
    
    for i in range(len(arrChB)):
        arrChB[i].grid(row=7+math.trunc(i/3), column=i%3)
    

def generarTexto():
    nombreEqL = tvarEquipoLocal.get()
    nombreEqV = tvarEquipoVisitante.get()
    tituloPlant = tvarPlantilla.get()
    temporada = tvarTemporada.get()[:4]

    articuloFinal = inyeccionPlantilla(nombreEqL, nombreEqV, temporada, tituloPlant)
    print("Generación de texto...")
        
    
    


ws = Tk()
ws.geometry("550x550")
ws.title("Generador de textos de la ACB")
#ws.grid_rowconfigure(0, weight=1)
#ws.grid_columnconfigure(0, weight=1)

#Título de la sección del partido
Label(ws, text="Datos del partido", font="Georgia 16 bold", pady=15).grid(row=0, column=1)

#Nombre del combobox para seleccionar el año de la temporada
lb_temporada = Label(ws, text="Temporada: ", pady=5, padx=15).grid(row=1, column=0)

#Combobox de la temporada con los años y el manejador al seleccionar un año
tvarTemporada = StringVar()
cboxTemporada = Combobox(ws, textvariable=tvarTemporada)
cboxTemporada.grid(row=1, column=1)
cboxTemporada.bind('<<ComboboxSelected>>', agregarEquipos)
cboxTemporada['state'] = 'readonly'
cboxTemporada['values'] = TEMPORADAS

#Selección del equipo local
lbl_equipoLocal = Label(ws, text="Equipo local: ", pady=5, padx=15).grid(row=2, column=0)

#Combobox del equipo local
tvarEquipoLocal = StringVar()
cboxEquipoLocal = Combobox(ws, textvariable=tvarEquipoLocal, width=35)
cboxEquipoLocal.grid(row=2, column=1)
cboxEquipoLocal['state'] = 'readonly'

#Selección del equipo visitante
lbl_equipoVisitante = Label(ws, text="Equipo visitante: ", pady=5, padx=15).grid(row=3, column=0)

#Combobox del equipo visitante
tvarEquipoVisitante = StringVar()
cboxEquipoVisitante = Combobox(ws, textvariable=tvarEquipoVisitante, width=35)
cboxEquipoVisitante.grid(row=3, column=1)
cboxEquipoVisitante['state'] = 'readonly'

#Sección segunda para seleccionar los párrafos 
Label(ws, text="Selección de párrafos", font="Georgia 16 bold", pady=30).grid(row=4, column=1)

#Label plantilla
lbl_plantilla = Label(ws, text="Plantilla: ", pady=5, padx=15).grid(row=5, column=0)

#ComboBox plantilla
tvarPlantilla = StringVar()
cboxPlantilla = Combobox(ws, textvariable=tvarPlantilla, width=35, postcommand=cargarPlantillasBD)
cboxPlantilla.grid(row=5, column=1)
cboxPlantilla.bind('<<ComboboxSelected>>', seleccionarPlantilla)
cboxPlantilla['state'] = 'readonly'
arrChB = []
arrVarChB = []

#Botón de Generar plantilla
btnGenerarPlantilla = Button( text ="Generar texto", command = generarTexto)
btnGenerarPlantilla.grid(row=15, column=1, pady=15)

ws.mainloop()