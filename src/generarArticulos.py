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
  print(equipoLocal)

#Recuperar el equipo visitante
for row in db.getEquipo(EQUIPO_VISITANTE, TEMPORADA):
  equipoVisitante = Equipo.Equipo(row)
  print(equipoVisitante)

#Recuperar partido
for row in db.getPartido(EQUIPO_LOCAL, EQUIPO_VISITANTE, TEMPORADA):
  partido = Partido.Partido(row)
  ID_PARTIDO = partido.id
  print(partido)

#Recuperar los jugadores del equipo local
print(" ---------------- JUGADORES DEL EQUIPO LOCAL ----------------\n")
for row in db.getJugadores(EQUIPO_LOCAL, ID_PARTIDO):
  jugador = Jugador.Jugador(row)
  JugadoresLocales.append(jugador)
  print(jugador)
  
#Recuperar los jugadores del equipo visitante
print("\n---------------- JUGADORES DEL EQUIPO VISITANTE ----------------\n")
for row in db.getJugadores(EQUIPO_VISITANTE, ID_PARTIDO):
  jugador = Jugador.Jugador(row)
  JugadoresVisitantes.append(jugador)
  print(jugador)




















"""
print("El partido: ")
cursor = conn.execute("SELECT * FROM game WHERE id=%d"%ID_PARTIDO)
for row in cursor:
  partido = Partido.Partido(row[0], row[2], row[3], row[4], row[6], row[7], row[8],
                    row[9], row[10], row[11], row[12], row[13], row[14],
                    row[15], row[16], row[17], row[18], row[19], row[20], row[21]);

print("El equipo local: ")
cursor = conn.execute("SELECT * FROM teamName JOIN team ON team.id=team_id WHERE team.id=%d AND season=%d" %(ID_EQ_L, ANYO_PARTIDO))
for row in cursor:
  equipoLocal = Equipo.Equipo(row[0], row[5], row[6], row[2], row[3])
  
print("El equipo visitante: ")
cursor = conn.execute("SELECT * FROM teamName JOIN team ON team.id=team_id WHERE team_id=%d AND season=%d" %(ID_EQ_V, ANYO_PARTIDO))
for row in cursor:
  equipoVisitante = Equipo.Equipo(row[0], row[5], row[6], row[2], row[3])


print("Jugadores del equipo local: ")




print("Jugadores del equipo visitante: ")

"""