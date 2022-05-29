import mysql.connector

class database:
      
  connector = None
  cursor = None
  result = None
  query = ""
  
  def __init__(self):
    self.connector = mysql.connector.connect(
      host ="localhost",
      user ="root",
      passwd ="414ee7d2",
      database = "acb"
    )
    
    self.cursor = self.connector.cursor()
    
    
  def __del__(self):
    self.connector.close()
    
    
  def getEquipo(self, idTeam, season):
    query = ''' SELECT * 
      FROM teamName JOIN team ON team.id=team_id 
      WHERE team.id={} AND season={}
    '''.format(idTeam, season)
    
    self.cursor.execute(query)
    self.result = self.cursor.fetchall()
    return self.result
  
  
  def getJugadores(self, idTeam, idGame):
    query = ''' SELECT * 
      FROM participant p JOIN actor ON actor.id = actor_id 
      WHERE p.team_id={} AND p.game_id={}
    '''.format(idTeam, idGame)
    
    self.cursor.execute(query)
    self.result = self.cursor.fetchall()
    return self.result
  
  def getPartido(self, idTeamLocal, idTeamVisi, temporada):
    temporada = '"' + str(temporada) +'%"'
    
    query = ''' SELECT *
      FROM game
      WHERE team_home_id={} AND team_away_id={} 
      AND competition_phase="regular" AND kickoff_time =
        (SELECT MAX(kickoff_time) FROM game WHERE team_home_id={} AND team_away_id={} 
         AND competition_phase="regular" AND kickoff_time LIKE {})
    '''.format(idTeamLocal, idTeamVisi, idTeamLocal, idTeamVisi, temporada)
    
    self.cursor.execute(query)
    self.result = self.cursor.fetchall()
    return self.result
  
  def getEquiposPorTemporada(self, temporada):
    query = ''' SELECT *
      FROM teamName JOIN team ON team.id = team_id
      WHERE season={}
    '''.format(temporada)
    self.cursor.execute(query)
    self.result = self.cursor.fetchall()
    return self.result
  
  def getEquipoPorNombre(self, nombre, temporada):
    query = ''' SELECT *
      FROM teamName JOIN team ON team.id = team_id
      WHERE name ="{}" AND season ={}'''.format(nombre, temporada)
    self.cursor.execute(query)
    self.result = self.cursor.fetchall()
    return self.result
  
  def getPlantilla(self, titulo):
    query = ''' SELECT *
      FROM plantilla
      WHERE titulo = "{}";
    '''.format(titulo)
    self.cursor.execute(query)
    self.result = self.cursor.fetchall()
    return self.result
  
  def getPlantillas(self):
    query = ''' SELECT * FROM plantilla '''
    self.cursor.execute(query)
    self.result = self.cursor.fetchall()
    return self.result
  
  def getParrafos(self, idPlantilla):
    query = '''SELECT *
      FROM parrafo
      WHERE id_plantilla = {}
    '''.format(idPlantilla)
    
    self.cursor.execute(query)
    self.result = self.cursor.fetchall()
    return self.result

  def getParrafo(self, tipoParrafo):
    query = "SELECT * FROM parrafo WHERE tipo_parrafo = %s"
    val = [tipoParrafo]
    
    self.cursor.execute(query, val)
    self.result = self.cursor.fetchall()
    return self.result

  def insertPlantilla(self, titulo):
    query = "INSERT INTO plantilla (titulo) VALUES (%s)"
    val = [titulo]

    self.cursor.execute(query, val)
    self.connector.commit()
    self.result = self.cursor.rowcount
    return self.result

  def existsPlantilla(self, titulo):
    query = "SELECT COUNT(*) FROM plantilla WHERE titulo=%s"
    val = [titulo]

    self.cursor.execute(query, val)
    self.result = self.cursor.fetchone()[0]
    return self.result
  
  def insertParrafos(self, parrafos, idPlantilla):
    query = ''' INSERT INTO parrafo
      (id_plantilla, contenido, tipo_parrafo)
      VALUES
      (%s, %s, %s)
      '''
    val = []

    for p in parrafos:
      val.append([idPlantilla, p.contenido, p.tipoParrafo])

    self.cursor.executemany(query, val)
    self.connector.commit()
    self.result = self.cursor.rowcount
    return self.result

  def insertParrafo(self, titulo, contenido, idPlantilla):
    query = ''' INSERT INTO parrafo
      (tipo_parrafo, contenido, id_plantilla)
      VALUES
      (%s, %s, %s)
      '''
    val = [titulo, contenido, idPlantilla]

    self.cursor.execute(query, val)
    self.connector.commit()
    self.result = self.cursor.rowcount
    return self.result

  def updateParrafo(self, titulo, contenido, idPlantilla):
    query = ''' UPDATE parrafo
      SET tipo_parrafo=%s, contenido=%s, id_plantilla=%s
      WHERE tipo_parrafo=%s
      '''
    val = [titulo, contenido, idPlantilla, titulo]

    self.cursor.execute(query, val)
    self.connector.commit()
    self.result = self.cursor.rowcount
    return self.result

  def existsParrafo(self, tipoParrafo, idPlantilla):
    query = ''' SELECT COUNT(*) FROM parrafo
      WHERE id_plantilla=%s AND tipo_parrafo=%s
      '''
    val = [idPlantilla, tipoParrafo]

    self.cursor.execute(query, val)
    self.result = self.cursor.fetchone()[0]
    return self.result

    