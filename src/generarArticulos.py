print('------------ generarArticulos.py ------------')

import pruebaMysql as MySQL

TEMPORADA = 2010
TIPO_PARTIDO = "regular"
ID_PARTIDO = -1;
EQUIPO_LOCAL = 20
EQUIPO_VISITANTE = 10

db = MySQL.database()
idPartido = 0

print("Equipo Local:")
print(db.getEquipo(EQUIPO_LOCAL, TEMPORADA))

print("\n\nEquipo Visitante: ")
print(db.getEquipo(EQUIPO_VISITANTE, TEMPORADA))

print("\n\nPartido:")
for p in db.getPartido(EQUIPO_LOCAL, EQUIPO_VISITANTE, TEMPORADA):
  ID_PARTIDO = p[0]
  print(p)

print("\n\nJugadores locales:")
for o in db.getJugadores(EQUIPO_LOCAL, ID_PARTIDO):
  print(o)
  
print("\n\nJugadores visitantes:") 
for o in db.getJugadores(EQUIPO_VISITANTE, ID_PARTIDO):
  print(o)




















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