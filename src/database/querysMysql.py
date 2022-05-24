import pruebaMysql as MySQL
import entities.Equipo as Equipo
import entities.Jugador as Jugador
import entities.Partido as Partido
import entities.Plantilla as Plantilla

#db = MySQL.database() #Crearla en cada función y cerrar conexión

#recuperar el equipo local
def recuEqLocal(idEqL, tempo):
  db = MySQL.database()
  equipoLocal = []

  for row in db.getEquipo(idEqL, tempo):
    equipoLocal = Equipo.Equipo(row)

  del db
  return equipoLocal


#Recuperar el equipo visitante
def recuEqVisi(idEqV, tempo):
  db = MySQL.database()
  equipoVisitante = []

  for row in db.getEquipo(idEqV, tempo):
    equipoVisitante = Equipo.Equipo(row)

  del db
  return equipoVisitante


#Recuperar partido
def recuPartido(idEqL, idEqV, tempo):
  db = MySQL.database()
  partido = []

  for row in db.getPartido(idEqL, idEqV, tempo):
    partido = Partido.Partido(row)

  del db
  return partido


#Recuperar los jugadores del equipo local
def recuJugsEqL(idEqL, idPartido):
  db = MySQL.database()
  jugadoresLocales = []

  for row in db.getJugadores(idEqL, idPartido):
    jugador = Jugador.Jugador(row)
    jugadoresLocales.append(jugador)
  
  del db
  return jugadoresLocales
  

#Recuperar los jugadores del equipo visitante
def recuJugsEqV(idEqV, idPartido):
  db = MySQL.database()
  jugadoresVisitantes = []

  for row in db.getJugadores(idEqV, idPartido):
    jugador = Jugador.Jugador(row)
    jugadoresVisitantes.append(jugador)

  del db
  return jugadoresVisitantes


#Recuperar equipos por temporada
def recuEqsTemp(temporada):
  db = MySQL.database()
  equipos = []

  for row in db.getEquiposPorTemporada(temporada):
    equipo = Equipo.Equipo(row)
    equipos.append(equipo)

  del db
  return equipos


#Recuperar equipo por nombre y temporada
def recuEqNombre(nombreEq, temporada):
  db = MySQL.database()
  equipo = []

  for row in db.getEquipoPorNombre(nombreEq, temporada):
      equipo = Equipo.Equipo(row)

  del db
  return equipo



#Recuperar plantilla:
def recuPlantilla(tituloPlantilla):
  db = MySQL.database()
  plantilla = []

  for row in db.getPlantilla(tituloPlantilla):
    plantilla = Plantilla.Plantilla(row)

    for row in db.getParrafos(plantilla.id):
      plantilla.parrafos.append(Plantilla.Parrafo(row))

  del db
  return plantilla


#Recuperar plantillas:
def recuPlantillas():
  db = MySQL.database()
  plantillas = []

  for row in db.getPlantillas():
    plantilla = Plantilla.Plantilla(row)
    plantillas.append(plantilla)
  
  del db
  return plantillas

def insertaPlantilla(titulo):
  db = MySQL.database()
  
  plantilla = db.insertPlantilla(titulo)
  
  del db
  return plantilla

def existePlantilla(titulo):
  db = MySQL.database()
  
  numPlantillas = db.existsPlantilla(titulo)
  
  del db
  return int(numPlantillas)

def insertaParrafos(parrafos, idPlantilla):
  db = MySQL.database()

  parrafos = db.insertParrafos(parrafos, idPlantilla)
  
  del db
  return parrafos

def insertaParrafo(titulo, contenido, idPlantilla):
  db = MySQL.database()

  parrafo = db.insertParrafo(titulo, contenido, idPlantilla)
  
  del db
  return parrafo

def existeParrafo(tipo, idPlantilla):
  db = MySQL.database()
  
  parrafo = db.existsParrafo(tipo, idPlantilla)
  
  del db
  return parrafo

#Recuperar plantillas:
def recuParrafos(idPlantilla):
  db = MySQL.database()
  parrafos = []

  for row in db.getParrafos(idPlantilla):
    parrafo = Plantilla.Plantilla(row)
    parrafos.append(parrafo)
  
  del db
  return parrafos