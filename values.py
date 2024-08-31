import random

def rendimiento():
    # Definir los posibles valores y sus probabilidades asociadas
    valores = [3, 4, 5, 2, 1, 6]
    probabilidades = [0.25, 0.25, 0.21875, 0.21875, 0.03125, 0.03125]
    
    # Seleccionar un valor basado en las probabilidades definidas
    return random.choices(valores, probabilidades)[0]


def calcular_valor_jugador(precio, rendimiento, edad):
    # Calcula el valor del precio
    if precio < 3:
        valor_precio = precio * 10 + 50
    elif precio < 100:
        valor_precio = precio
    else:
        valor_precio = (precio - 70) / 2 + 50
    valor_precio = max(50, min(99, valor_precio))
    
    # Calcula el valor del rendimiento
    valor_rendimiento = (rendimiento / 6) * 49 + 50
    
    # Ajuste por edad
    if edad < 20:
        ajuste_edad = 4
    elif 20 <= edad <= 23:
        ajuste_edad = 3
    elif 24 <= edad <= 29:
        ajuste_edad = 2
    elif 30 <= edad <= 33:
        ajuste_edad = 1
    else:  # edad >= 34
        ajuste_edad = 0
    
    # Calcular el valor total
    valor_total = (valor_precio + valor_rendimiento) / 2 + ajuste_edad
    
    # Asegurarse de que el valor esté entre 50 y 99
    valor_total = max(50, min(99, valor_total))
    
    # Redondear el valor total al número entero más cercano
    return round(valor_total)


# Ejemplo de uso
precio = 90  # Precio en millones de euros
valor_rendimiento = rendimiento()
print(f"El rendimiento del jugador es: {valor_rendimiento}")
edad = 37  # Edad del jugador

valor_calculado = calcular_valor_jugador(precio, valor_rendimiento, edad)
print(f"El valor del jugador es: {valor_calculado}")




