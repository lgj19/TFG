print('------------ generarArticulos.py ------------')

import sqlite3
conn = sqlite3.connect('database.sqlite')

cursor = conn.execute("SELECT * FROM actor WHERE id=1")
print("El primer actor: ")
for row in cursor:
  print(row)
conn.close()