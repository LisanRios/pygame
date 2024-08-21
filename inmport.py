import requests
import csv
import pandas as pd
import json

def cargarEquipo():
    # Obtener el nombre del equipo desde el usuario
    equipo_nombre = input("Ingrese el nombre del equipo: ")

    # Hacer la petición a la API para buscar el equipo
    url = f"https://transfermarkt-api.fly.dev/clubs/search/{equipo_nombre}"
    response = requests.get(url)
    
    # Asegurarse de que la respuesta sea válida
    if response.status_code != 200:
        print(f"Error en la solicitud: {response.status_code}")
        return

    datos = response.json()
    
    # Acceder a la lista de equipos
    equipos = datos.get('results', [])
    
    if not equipos:
        print("No se encontraron equipos.")
        return

    # Mostrar los equipos encontrados al usuario
    print("Equipos encontrados:")
    for i, equipo in enumerate(equipos):
        print(f"{i+1}. {equipo['name']} (ID: {equipo['id']})")

    # Obtener la elección del usuario por ID
    id_equipo = input("Ingrese el ID del equipo para ver los jugadores: ")

    # Encontrar el equipo seleccionado
    equipo_seleccionado = next((e for e in equipos if e['id'] == id_equipo), None)
    
    if equipo_seleccionado is None:
        print("ID de equipo no válido.")
        return

    # Obtener el ID del equipo seleccionado
    club_id = equipo_seleccionado["id"]

    # Hacer la petición a la API para obtener los jugadores del equipo
    url = f"https://transfermarkt-api.fly.dev/clubs/{club_id}/players"
    response = requests.get(url)
    
    # Asegurarse de que la respuesta sea válida
    if response.status_code != 200:
        print(f"Error en la solicitud: {response.status_code}")
        return

    datos = response.json()

    # Imprimir los datos para inspección
    print("Datos de la respuesta para jugadores:")
    print(datos)

    # Extraer la lista de jugadores
    players = datos["players"]

    # Convertir la lista de jugadores a un DataFrame
    df = pd.json_normalize(players)

    # Guardar el DataFrame en un archivo CSV.
    df.to_csv('data/players_data.csv', index=False)
    

cargarEquipo()
