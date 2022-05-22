class Equipo:
    id = 0
    siglas = "XXX"
    anyoFundacion = 0000
    nombre = "Nombre completo del equipo"
    temporada = 0000

    def __init__(self, row):
        self.id = row[1]  
        self.nombre = row[2]
        self.temporada = row[3]
        self.siglas = row[5]
        self.anyoFundacion = row[6]


    def __str__(self):
        return '''Equipo: {} 
        id: {} 
        siglas: {} 
        año de fundación: {}
        temporada del nombre: {}
        '''.format(self.nombre, self.id, self.siglas, self.anyoFundacion, self.temporada)

    