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
  def __init__(self, idPartido, idEqL, idEqV, fase, jornada, pab,
    pub, fec,ptl, ptv, p1l, p1v, p2l, p2v, p3l, p3v, p4l, p4v, pel, pev):
      
    self.id = idPartido
    self.idEquipoLocal = idEqL
    self.idEquipoVisitante = idEqV
    self.faseCompeticion = fase
    self.jornada = jornada
    self.pabellon = pab
    self.publico = pub
    self.fechaPartido = fec
    self.puntosTotalLocal = ptl
    self.puntosTotalVisitante = ptv
    self.puntos1QLocal = p1l
    self.puntos1QVisitante = p1v
    self.puntos2QLocal = p2l
    self.puntos2QVisitante = p2v
    self.puntos3QLocal = p3l
    self.puntos3QVisitante = p3v
    self.puntos4QLocal = p4l
    self.puntos4QVisitante = p4v
    self.puntosExtraLocal = pel
    self.puntosExtraVisitante = pev
    
    
    
  