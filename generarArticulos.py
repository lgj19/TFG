print('------------ generarArticulos.py ------------')

import sqlite3
import Jugador
import Partido
import Equipo

ID_PARTIDO = 1
ANYO_PARTIDO = 2016
ID_EQ_L = 1
ID_EQ_V = 11

conn = sqlite3.connect('database.sqlite')

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




conn.close()