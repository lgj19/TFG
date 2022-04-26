class Jugador:
    id = 0
    esEntrenador = False
    nombre = "Nombre del jugador"
    nombreCompleto = "Nombre completo del jugador"
    nacionalidad = "XXX"
    lugarNacimiento = "Ciudad (Provincia/Estado)"
    fechaNacimiento = "YYYY-MM-DD HH:MM:SS"
    posicion = "X"
    altura = "x.yy"
    peso = "xxx.y"
    debutACB = "YYYY-MM-DD HH:MM:SS"
    twitter = "Apodo de twitter"
    
    dorsal = 0
    titular = False
    minutos = 0
    puntosTotales = 0
    tirosDe2 = 0
    intentosDe2 = 0
    tirosDe3 = 0
    intentosDe3 = 0
    tirosDe1 = 0
    intentosDe1 = 0
    rebotesOfensivos = 0
    rebotesDefensibos = 0
    asistencias = 0
    robos = 0
    perdidas = 0
    contraataques = 0
    tapones = 0
    taponesRecibidos = 0
    mates = 0
    faltas = 0
    faltasRecibidas = 0
    valoracion = 0
    masMenos = 0
    
    def __init__(self, id, esEnt, n, nC, nacio, lugNac, fecNac, pos, alt, pes, debut, twitter):
        self.id = id
        self.esEntrenador = esEnt
        self.nombre = n
        self.nombreCompleto = nC
        self.nacionalidad = nacio
        self.lugarNacimiento = lugNac
        self.fechaNacimiento = fecNac
        self.posicion = pos
        self.altura = alt
        self.peso = pes
        self.debutACB = debut
        self.twitter = twitter
        
    def agregarDatosPartido(self, dorsal, titu, segs, pt, p2, pi2, p3, pi3, p1, pi1, rO, rD, asis,
                            rob, perd, contras, tap, tapR, mat, faltas, fR, val, mm):
        self.dorsal = dorsal
        self.titular = titu
        self.minutos = segs / 60;
        self.puntosTotales = pt
        self.tirosDe2 = p2
        self.intentosDe2 = pi2
        self.tirosDe3 = p3
        self.intentosDe3 = pi3
        self.tirosDe1 = p1
        self.intentosDe1 = pi1
        self.rebotesOfensivos = rO
        self.rebotesDefensibos = rD
        self.asistencias = asis
        self.robos = rob
        self. perdidas = perd
        self.contraataques = contras
        self.tapones = tap
        self.taponesRecibidos = tapR
        self.mates = mat
        self.faltas = faltas
        self.faltasRecibidas = fR
        self.valoracion = val
        self.masMenos = mm
        
    