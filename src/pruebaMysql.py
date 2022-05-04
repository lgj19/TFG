# importing required libraries
import mysql.connector

class database:
      
  connector = None
  cursor = None
  result = None
  query = ""
  
  def __init__(self):
    self.connector = mysql.connector.connect(
      host ="localhost",
      user ="lgj19",
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
    
    self.cursor.execute(query);
    self.result = self.cursor.fetchall()
    return self.result;
  
  
  def getJugadores(self, idTeam, idGame):
    query = ''' SELECT * 
      FROM participant p JOIN actor ON actor.id = actor_id 
      WHERE p.team_id={} AND p.game_id={}
    '''.format(idTeam, idGame)
    
    self.cursor.execute(query);
    self.result = self.cursor.fetchall()
    return self.result;
  
  def getPartido(self, idTeamLocal, idTeamVisi, temporada):
    temporada = '"' + str(temporada) +'%"'
    
    query = ''' SELECT *
      FROM game
      WHERE team_home_id={} AND team_away_id={} 
      AND competition_phase="regular" AND kickoff_time =
        (SELECT MAX(kickoff_time) FROM game WHERE team_home_id={} AND team_away_id={} 
         AND competition_phase="regular" AND kickoff_time LIKE {})
    '''.format(idTeamLocal, idTeamVisi, idTeamLocal, idTeamVisi, temporada)
    
    self.cursor.execute(query);
    self.result = self.cursor.fetchall()
    return self.result;
  
  def getEquiposPorTemporada(self, temporada):
    query = ''' SELECT *
      FROM teamName JOIN team, teamName ON team.id = team_id
      WHERE season={}
    '''.format(temporada)
    self.cursor.execute(query);
    self.result = self.cursor.fetchall()
    return self.result;
    