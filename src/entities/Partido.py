class Partido:
  id = 0
  idEquipoLocal = 0
  idEquipoVisitante = 0
  faseCompeticion = "fase de la competición"
  jornada = 0
  pabellon = "Pabellon"
  publico = 0
  fechaPartido = "YYYY-MM-DD HH:MM:SS"
  puntosTotalLocal = 0
  puntosTotalVisitante = 0
  puntos1QLocal = 0
  puntos1QVisitante = 0
  puntos2QLocal = 0
  puntos2QVisitante = 0
  puntos3QLocal = 0
  puntos3QVisitante = 0
  puntos4QLocal = 0
  puntos4QVisitante = 0
  puntosExtraLocal = 0
  puntosExtraVisitante = 0
  
  def __init__():
    return     
  def __init__(self, row):
      
    self.id = row[0]
    self.idEquipoLocal = row[2]
    self.idEquipoVisitante = row[3]
    self.faseCompeticion = row[4]
    self.jornada = row[6]
    self.pabellon = row[7]
    self.publico = row[8]
    self.fechaPartido = row[9]
    self.puntosTotalLocal = row[10]
    self.puntosTotalVisitante = row[11]
    self.puntos1QLocal = row[12]
    self.puntos1QVisitante = row[13]
    self.puntos2QLocal = row[14]
    self.puntos2QVisitante = row[15]
    self.puntos3QLocal = row[16]
    self.puntos3QVisitante = row[17]
    self.puntos4QLocal = row[18]
    self.puntos4QVisitante = row[19]
    self.puntosExtraLocal = row[20]
    self.puntosExtraVisitante = row[21]
    
  def __str__(self):
      return '''Datos del partido:
      ID: {}
      ID del equipo local: {}
      ID del equipo visitnte: {}
      fase: {}
      jornada: {}
      pabellón: {}
      público: {}
      fecha del partido: {}
      puntos del equipo local:
        [totales: {}, Q1: {}, Q2: {}, Q3: {}, Q4: {}, QE: {}]
      puntos del equipo visitante:
        [totales: {}, Q1: {}, Q2: {}, Q3: {}, Q4: {}, QE: {}]
      '''.format(self.id, self.idEquipoLocal, self.idEquipoVisitante, self.faseCompeticion, 
                 self.jornada, self.pabellon, self.publico, self.fechaPartido,
                 self.puntosTotalLocal, self.puntos1QLocal, self.puntos2QLocal,
                 self.puntos3QLocal, self.puntos4QLocal, self.puntosExtraLocal, 
                 self.puntosTotalVisitante, self.puntos1QVisitante, self.puntos2QVisitante,
                 self.puntos3QVisitante, self.puntos4QVisitante, self.puntosExtraVisitante)
    
    
  