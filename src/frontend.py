from tkinter import *
from tkinter.ttk import Combobox
import entities.Plantilla as Plantilla
import pruebaMysql as mysql
import entities.Equipo as Equipo

db = mysql.database()
equipos = []
plantillaSelected = Plantilla.Plantilla([-1,False,"nada"])
TEMPORADAS = ('1994/95', '1995/96', '1996/97', '1997/98', '1998/99', '1999/00', '2000/01', '2001/02', '2002/03',
              '2003/04', '2004/05', '2005/06', '2006/07', '2007/08', '2008/09', '2009/10', '2010/11', '2011/12',
              '2012/13', '2013/14', '2014/15', '2015/16', '2016/17')

def agregarEquipos(event):
    temporada = tvarTemporada.get()[:4]
    for row in mysql.database.getEquiposPorTemporada(db, temporada):
        equipo = Equipo.Equipo(row)
        equipos.append(equipo)
        
    nombreEquipos = []
    for equipo in equipos:
        nombreEquipos.append(equipo.nombre)
    cboxEquipoLocal['values'] = cboxEquipoVisitante['values'] = nombreEquipos

def cargarPlantillasBD():
    plantillas = []
    nombrePlantillas = []
    
    for row in mysql.database.getPlantillas(db):
        plantillas.append(Plantilla.Plantilla(row))
        
    for plantilla in plantillas:
        nombrePlantillas.append(plantilla.titulo)
        
    cboxPlantilla['values'] = nombrePlantillas

def seleccionarPlantilla(event):
    for row in mysql.database.getPlantilla(db, tvarPlantilla.get()):
        plantillaSelected.id = row[0]
        plantillaSelected.es_semilla = row[1]
        plantillaSelected.titulo = row[2]
    
    for row in mysql.database.getParrafos(db, plantillaSelected.id):
        plantillaSelected.parrafos.append(Plantilla.Parrafo(row))

def generarTexto():
    print(plantillaSelected)
    
    


ws = Tk()
ws.geometry("480x400")
ws.title("Simple Text Editor")
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

#CheckList párrafos

#Botón de Generar plantilla
btnGenerarPlantilla = Button( text ="Generar texto", command = generarTexto)
btnGenerarPlantilla.grid(row=6, column=1, pady=15)

ws.mainloop()