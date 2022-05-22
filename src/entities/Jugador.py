class Jugador:
    id = 0
    esEntrenador = False
    esArbitro = False
    esTitular = False
    nombre = "Nombre del jugador"
    nombreCompleto = "Nombre completo"
    primerApellido = "Primer apellido"
    segundoApellido = "Segundo apellido"
    nacionalidad = "XXX"
    lugarNacimiento = "Ciudad (Provincia/Estado)"
    fechaNacimiento = "YYYY-MM-DD HH:MM:SS"
    posicion = "X"
    altura = "x.yy"
    peso = "xxx.y"
    debutACB = "YYYY-MM-DD HH:MM:SS"
    twitter = "Apodo de twitter"
    
    dorsal = 0
    minutos = 0
    puntosTotales = 0
    tirosDe2 = 0
    intentosDe2 = 0
    tirosDe3 = 0
    intentosDe3 = 0
    tirosDe1 = 0
    intentosDe1 = 0
    rebotesOfensivos = 0
    rebotesDefensivos = 0
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
    
    def __init__(self, row):
        self.id = row[3]
        self.nombre = row[4]
        self.primerApellido = row[5]
        self.segundoApellido = row[6]
        self.dorsal = row[7]
        self.esEntrenador = row[8]
        self.esArbitro = row[9]
        self.esTitular = row[10]
        self.minutos = row[11]/60
        self.puntosTotales = row[12]
        self.intentosDe2 = row[13]
        self.tirosDe2 = row[14]
        self.intentosDe3 = row[15]
        self.tirosDe3 = row[16]
        self.intentosDe1 = row[17]
        self.tirosDe1 = row [18]
        self.rebotesOfensivos = row[20]
        self.rebotesDefensivos = row[19]
        self.asistencias = row[21]
        self.robos = row[22]
        self. perdidas = row[23]
        self.contraataques = row[24]
        self.tapones = row[25]
        self.taponesRecibidos = row[26]
        self.mates = row[27]
        self.faltas = row[28]
        self.faltasRecibidas = row[29]
        self.valoracion = row[31]
        self.masMenos = row[30]
        self.nombreCompleto = row[36]
        self.nacionalidad = row[37]
        self.lugarNacimiento = row[38]
        self.fechaNacimiento = row[39]
        self.posicion = row[40]
        self.altura = row[41]
        self.peso = row[42]
        self.debutACB = row[44]
        self.twitter = row[45]
        
    def __str__(self):
        return '''Información del jugador:
        ID: {}
        Es entrenador: {},
        Nombre completo: {},
        Posición: {},
        Twitter: {}
        
        '''.format(self.id, self.esEntrenador, self.nombreCompleto, self.posicion, self.twitter)
        
    