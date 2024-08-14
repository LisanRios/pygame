class club:
    
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

class academia(club):
    def __init__(self, nombre, ubicacion, aula, profesor):
        super().__init__(nombre, ubicacion)
        self.aula = aula
        self.profesor = profesor
