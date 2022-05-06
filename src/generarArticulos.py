print('\n------------ generarArticulos.py ------------\n')

import pruebaMysql as MySQL
import entities.Equipo as Equipo
import entities.Jugador as Jugador
import entities.Partido as Partido

TEMPORADA = 2010
TIPO_PARTIDO = "regular"
ID_PARTIDO = -1;
EQUIPO_LOCAL = 20
EQUIPO_VISITANTE = 10

db = MySQL.database()
idPartido = 0

equipoLocal = []
equipoVisitante = []
partido = []
JugadoresLocales = []
JugadoresVisitantes = []

#recuperar el equipo local
for row in db.getEquipo(EQUIPO_LOCAL, TEMPORADA):
  equipoLocal = Equipo.Equipo(row)
  #print(equipoLocal)

#Recuperar el equipo visitante
for row in db.getEquipo(EQUIPO_VISITANTE, TEMPORADA):
  equipoVisitante = Equipo.Equipo(row)
  #print(equipoVisitante)

#Recuperar partido
for row in db.getPartido(EQUIPO_LOCAL, EQUIPO_VISITANTE, TEMPORADA):
  partido = Partido.Partido(row)
  ID_PARTIDO = partido.id
  #print(partido)

#Recuperar los jugadores del equipo local
print(" ---------------- JUGADORES DEL EQUIPO LOCAL ----------------\n")
for row in db.getJugadores(EQUIPO_LOCAL, ID_PARTIDO):
  jugador = Jugador.Jugador(row)
  JugadoresLocales.append(jugador)
  #print(jugador)
  
#Recuperar los jugadores del equipo visitante
print("\n---------------- JUGADORES DEL EQUIPO VISITANTE ----------------\n")
for row in db.getJugadores(EQUIPO_VISITANTE, ID_PARTIDO):
  jugador = Jugador.Jugador(row)
  JugadoresVisitantes.append(jugador)
  #print(jugador)