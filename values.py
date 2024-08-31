import random

def rendimiento():
    # Definir los posibles valores y sus probabilidades asociadas
    valores = [3, 4, 5, 2, 1, 6]
    probabilidades = [0.25, 0.25, 0.21875, 0.21875, 0.03125, 0.03125]
    
    # Seleccionar un valor basado en las probabilidades definidas
    return random.choices(valores, probabilidades)[0]

def calcular_estrellas_precio(precio):
    # Precio en millones, convierte a estrellas
    if precio < 0.2:
        return 1  # Menos de 100K
    elif 0.1 <= precio < 1:
        return 2  # 250K a 1M
    elif 1 <= precio < 10:
        return 3  # 1M a 10M
    elif 10 <= precio < 30:
        return 4  # 10M a 30M
    elif 30 <= precio < 60:
        return 5  # 30M a 60M
    else:
        return 6  # Más de 60M

def calcular_estrellas_rendimiento(rendimiento):
    # Mapea el rendimiento a estrellas
    if rendimiento == 6:
        return 6
    elif rendimiento == 5:
        return 5
    elif rendimiento == 4:
        return 4
    elif rendimiento == 3:
        return 3
    elif rendimiento == 2:
        return 2
    else:  # rendimiento == 1
        return 1

def calcular_estrellas_edad(edad):
    # Edad convierte a estrellas
    if edad > 39:
        return 1
    elif 35 <= edad <= 38:
        return 2
    elif 30 <= edad <= 34:
        return 3
    elif 24 <= edad <= 29:
        return 6
    elif 20 <= edad <= 23:
        return 5
    else:  # edad < 20
        return 4

def calcular_media(precio, rendimiento, edad):
    # Calcula la media de las estrellas de las tres variantes
    estrellas_precio = calcular_estrellas_precio(precio)
    estrellas_rendimiento = calcular_estrellas_rendimiento(rendimiento)
    estrellas_edad = calcular_estrellas_edad(edad)
    
    # Calcular la media de las estrellas
    media_estrellas = (estrellas_precio + estrellas_precio + estrellas_rendimiento + estrellas_edad) / 4
    
    # Sumar 1 estrella al resultado final y asegurarse de que esté en el rango de 1 a 6
    media_estrellas = min(6, media_estrellas + 1)
    
    # Redondear a una cifra decimal
    return round(media_estrellas, 1)

# Ejemplos de prueba con diferentes escenarios de jugadores
pruebas = [
    (0.5, 3, 37),    # Jugador con precio bajo, rendimiento medio, edad avanzada
    (50, 5, 24),      # Jugador con precio medio, buen rendimiento, edad óptima
    (15, 2, 30),      # Jugador con precio medio, bajo rendimiento, edad en su mejor momento
    (0.25, 6, 18),     # Joven con gran rendimiento y precio bajo
    (90, 6, 28),      # Precio alto, gran rendimiento, edad óptima
    (0.2, 1, 40),     # Precio muy bajo, bajo rendimiento, edad avanzada
    (5, 4, 22),       # Jugador joven con buen rendimiento y precio accesible
    (25, 3, 34),      # Jugador en su mejor momento con precio medio y rendimiento aceptable
]

# Ejecutar las pruebas
for precio, rendimiento, edad in pruebas:
    media = calcular_media(precio, rendimiento, edad)
    print(f"Precio: {precio}M, Rendimiento: {rendimiento}, Edad: {edad} -> Media Estrellas: {media}")
