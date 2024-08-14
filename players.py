import random

#------------------------Variables temporales----------------------------
#Son variables que dependen de otras clases/obejos/eventos que de manera temporal seran constantes por razones de prueba
tiempoDeJuego = 22
nivelRubi = [95, 99]
nivelDiamante = [86, 94]
nivelOro = [74, 86]
nivelPlata = [64, 74]
nivelBronce = [25, 64]


#------------------------RELACION CON BASE DE DATOS----------------------
#Son variables que estan en la base de datos que de manera temporal seran constantes por razones de prueba
positions = ["GK", "RB", "CB", "LB", "CDM", "CM", "CAM", "RW", "LW", "ST"]


class JugadorDeFutbol:
    def __init__(self):
        self.pace = 0
        self.shooting = 0
        self.passing = 0
        self.dribbling = 0
        self.defense = 0
        self.physical = 0

    def numeroAleatorio(self, min, max):
        return random.randint(min, max)
    
    def rango(self, rango):
        return random.randint(rango[0], rango[1])

    def saberStats(self, posicion):
        great = [86, 99]
        good = [65, 85]
        poor = [25, 64]
        
        stats = {
            "GK": {
                "pace": self.rango(great),
                "shooting": self.rango(poor),
                "passing": self.rango(great),
                "dribbling": self.rango(poor),
                "defense": self.rango(great),
                "pphysical": self.rango(great),
            },
            "RB": {
                "pace": self.rango(great),
                "shooting": self.rango(poor),
                "passing": self.rango(good),
                "dribbling": self.rango(good),
                "defense": self.rango(good),
            },
            "CB": {
                "pace": self.rango(great),
                "shooting": self.rango(poor),
                "passing": self.rango(good),
                "dribbling": self.rango(poor),
                "defense": self.rango(great),
            },
            "LB": {
                "pace": self.rango(great),
                "shooting": self.rango(poor),
                "passing": self.rango(good),
                "dribbling": self.rango(good),
                "defense": self.rango(good),
            },
            "CDM": {
                "pace": self.rango(),
                "shooting": self.rango(),
                "passing": self.rango(),
                "dribbling": self.rango(),
                "defense": self.rango(),
            },
            "CM": {
                "pace": self.rango(),
                "shooting": self.rango(),
                "passing": self.rango(),
                "dribbling": self.rango(),
                "defense": self.rango(),
            },
            "CAM": {
                "pace": self.rango(),
                "shooting": self.rango(),
                "passing": self.rango(),
                "dribbling": self.rango(),
                "defense": self.rango(),
            },
            "RW": {
                "pace": self.rango(),
                "shooting": self.rango(),
                "passing": self.rango(),
                "dribbling": self.rango(),
                "defense": self.rango(),
            },
            "LW": {
                "pace": self.rango(),
                "shooting": self.rango(),
                "passing": self.rango(),
                "dribbling": self.rango(),
                "defense": self.rango(),
            },
            "ST": {
                "pace": self.rango(),
                "shooting": self.rango(nivelDiamante),
                "passing": self.rango(),
                "dribbling": self.rango(),
                "defense": self.rango(),
            },
        }
        return stats[posicion]
    
    def seleccionarPosicion(self):
        posicion = random.choice(positions)
        if posicion == "GK":
            return ["GK"]
        else:
            cantidad_posiciones = random.randint(1, 3)
            posiciones = positions.copy()
            indice = posiciones.index(posicion)
            posiciones_seleccionadas = []
            for _ in range(cantidad_posiciones):
                indice = random.randint(0, len(posiciones) - 1)
                posicion_seleccionada = posiciones[indice]
                posiciones_seleccionadas.append(posicion_seleccionada)
                posiciones.remove(posicion_seleccionada)
            return posiciones_seleccionadas

    def goal(self):
        return self.shooting * self.numeroAleatorio(1, 10)

    def steal(self):
        return self.dribbling * self.numeroAleatorio(1, 10)

    def dribble(self):
        return self.dribbling * self.numeroAleatorio(1, 10)

    def block(self):
        return self.defense * self.numeroAleatorio(1, 10)

    def passe(self):
        return self.passing * self.numeroAleatorio(1, 10)

    def fatigue(self):
        # Calcular la fatiga como la diferencia entre el físico actual y 22
        cansancio = self.physical - tiempoDeJuego

        if cansancio <= 0:
            # Si la fatiga es mayor o igual a la condición física, la fatiga será del 100%
            self.physical = 0
            return "100.00% | Physical: 0"
        else:
            # Calcular el porcentaje de fatiga
            porcentaje_fatiga = (tiempoDeJuego * 100) / self.physical

            # Reducir todos los atributos en función del porcentaje de fatiga
            self.pace = int(self.pace * (1 - porcentaje_fatiga / 100))
            self.shooting = int(self.shooting * (1 - porcentaje_fatiga / 100))
            self.passing = int(self.passing * (1 - porcentaje_fatiga / 100))
            self.dribbling = int(self.dribbling * (1 - porcentaje_fatiga / 100))
            self.defense = int(self.defense * (1 - porcentaje_fatiga / 100))
            
            # Reducir el físico en la cantidad de la fatiga
            self.physical -= tiempoDeJuego

            # Retornar el porcentaje de fatiga y la nueva condición física
            return f"{porcentaje_fatiga:.2f}% | Physical: {self.physical}"
   

    def average(self):
        return (self.pace + self.shooting + self.passing + self.dribbling + self.defense + self.physical) // 5
    

# Crear una instancia y probar los métodos
persona1 = JugadorDeFutbol()

# Llamada a la función seleccionarPosicion y mostrar el resultado
print("Posiciones seleccionadas:", persona1.seleccionarPosicion())

# Mostrar los atributos iniciales del jugador
print(f"Velocidad (pace): {persona1.pace}")
print(f"Tiro (shooting): {persona1.shooting}")
print(f"Pase (passing): {persona1.passing}")
print(f"Regate (dribbling): {persona1.dribbling}")
print(f"Defensa (defense): {persona1.defense}")
print(f"Físico (physical): {persona1.physical}")

# Mostrar el promedio de las habilidades
print(f"Promedio de habilidades: {persona1.average()}")

# Llamadas a los métodos
print(f"Resultado de un tiro a puerta (goal): {persona1.goal()}")
print(f"Resultado de un robo de balón (steal): {persona1.steal()}")
print(f"Resultado de un regate (dribble): {persona1.dribble()}")
print(f"Resultado de un bloqueo (block): {persona1.block()}")
print(f"Resultado de un pase (passe): {persona1.passe()}")

# Aplicar fatiga y mostrar el resultado
print(f"Fatiga post partido: {persona1.fatigue()}")

print("\nDespués de aplicar fatiga:")

# Mostrar el promedio de las habilidades despues de la fatiga
print(f"Promedio de habilidades: {persona1.average()}")

print(f"Velocidad (pace): {persona1.pace}")
print(f"Tiro (shooting): {persona1.shooting}")
print(f"Pase (passing): {persona1.passing}")
print(f"Regate (dribbling): {persona1.dribbling}")
print(f"Defensa (defense): {persona1.defense}")
print(f"Físico (physical): {persona1.physical}")
