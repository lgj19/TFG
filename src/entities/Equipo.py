class Equipo:
    id = 0
    siglas = "XXX"
    anyoFundacion = 0000
    nombre = "Nombre completo del equipo"
    temporada = 0000
    
    def __init__(self, id, siglas, anyo, nombre, temporada):
        self.id = id
        self.siglas = siglas
        self.anyoFundacion = anyo
        self.nombre = nombre
        self.temporada = temporada

    def __str__(self):
        cadena = "";

    