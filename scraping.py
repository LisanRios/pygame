import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from io import StringIO

def obtener_tabla():
    # Menú para seleccionar el equipo de fútbol
    equipos = {
        "1": "https://es.besoccer.com/equipo/plantilla/manchester-city-fc",
        "2": "https://es.besoccer.com/equipo/plantilla/ca-river-plate",
        "3": "https://es.besoccer.com/equipo/plantilla/ca-boca-juniors",
        "4": "https://es.besoccer.com/equipo/plantilla/manchester-united-fc"
    }
    
    print("Selecciona un equipo:")
    print("1. Manchester City")
    print("2. River Plate")
    print("3. Boca Juniors")
    print("4. Manchester United")
    
    eleccion = input("Introduce el número correspondiente al equipo: ")
    url = equipos.get(eleccion)

    if url is None:
        print("Selección no válida.")
        return

    # Realizar la solicitud GET a la URL y obtener el contenido HTML
    response = requests.get(url)
    content = response.content

    # Crear un objeto BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(content, 'html.parser')

    # Encontrar todas las etiquetas de tabla en la página
    tablas = soup.find_all('table')

    # Crear la carpeta 'data' si no existe
    if not os.path.exists('data'):
        os.makedirs('data')

    # Guardar todas las tablas en un archivo CSV
    archivo_csv = os.path.join('data', 'plantillas.csv')

    with open(archivo_csv, 'w', newline='', encoding='utf-8-sig') as file:
        for i, tabla in enumerate(tablas):
            # Convertir la tabla HTML en un DataFrame de pandas usando StringIO
            html_str = str(tabla)
            df = pd.read_html(StringIO(html_str))[0]
            
            # Eliminar filas con datos incompletos (NaN)
            df.dropna(inplace=True)
            
            # Guardar en CSV, añadiendo una tabla a la vez
            if i == 0:
                df.to_csv(archivo_csv, mode='w', index=False, header=True)
            else:
                df.to_csv(archivo_csv, mode='a', index=False, header=False)

    print(f"Todas las tablas guardadas en {archivo_csv}")

# Llamada a la función principal
obtener_tabla()
