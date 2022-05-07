class Plantilla:
    id = -1
    es_semilla = False
    titulo = "Título de la plantilla"
    parrafos = []
    
    def __init__(self, row):
        self.id = row[0]
        self.semilla = row[1]
        self.titulo = row[2]

    def __str__(self):
        parrafos = ""
        
        for parrafo in self.parrafos:
            parrafos += str(parrafo) + '\n'
            
        return ''' Titulo: {}
            ID: {}
            Es semilla: {}
            Párrafos: 
                {}
        '''.format(self.titulo, self.id, self.es_semilla, parrafos)
    
class Parrafo:
    id = -1
    contenido = "Contenido de Párrafo"
    id_plantilla = -1
    tipoParrafo = "Tipo del párrafo"
    
    def __init__(self, row):
        self.id = row[0]
        self.id_plantilla = row[2]
        self.contenido = row[1]
        self.tipoParrafo = row[3]
    
    def __str__(self):
        return ''' ID: {}, ID de la plantilla: {}
            Tipo del párrafo: {}
            Contenido: {}
        '''.format(self.id, self.id_plantilla, self.tipoParrafo, self.contenido)
