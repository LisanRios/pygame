import os
import pandas as pd  # Corrección aquí: Importar pandas con el alias pd
import requests

def importTeam(nombre_club, carpeta):
    # Hacer la petición a la API para buscar el equipo
    url = f"https://transfermarkt-api.fly.dev/clubs/search/{nombre_club}"
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

    # Encontrar el equipo seleccionado
    equipo_seleccionado = next((e for e in equipos if e['name'] == nombre_club), None)
    
    if equipo_seleccionado is None:
        print("No se encontró el equipo")
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
    players = datos.get("players", [])

    if not players:
        print("No se encontraron jugadores.")
        return

    # Convertir la lista de jugadores a un DataFrame
    df = pd.json_normalize(players)

    # Guardar el DataFrame en un archivo CSV.
    nombre_archivo = os.path.join(carpeta, nombre_club + ".csv")
    df.to_csv(nombre_archivo, index=False)
    print(f"Datos de {nombre_club} guardados en {nombre_archivo}.")

def importLeague():
    # Obtener el nombre de la competición desde el usuario
    competition_name = input("Ingrese el nombre de la competición: ")

    # Hacer la petición a la API para buscar la competición
    url = f"https://transfermarkt-api.fly.dev/competitions/search/{competition_name}"
    response = requests.get(url)
    
    # Asegurarse de que la respuesta sea válida
    if response.status_code != 200:
        print(f"Error en la solicitud: {response.status_code}")
        return

    datos = response.json()
    
    # Acceder a la lista de competiciones
    competitions = datos.get('results', [])
    
    if not competitions:
        print("No se encontraron competiciones.")
        return

    # Mostrar las competiciones encontradas al usuario
    print("Competiciones encontradas:")
    for i, competition in enumerate(competitions):
        print(f"{i+1}. {competition['name']} (ID: {competition['id']})")

    # Obtener la elección del usuario por ID
    id_competition = input("Ingrese el ID de la competición para ver los clubes: ")

    # Encontrar la competición seleccionada
    competition_seleccionada = next((e for e in competitions if e['id'] == id_competition), None)
    
    if competition_seleccionada is None:
        print("ID de competición no válido.")
        return

    # Obtener el ID de la competición seleccionada
    competition_id = competition_seleccionada["id"]

    # Hacer la petición a la API para obtener los clubes de la competición
    url = f"https://transfermarkt-api.fly.dev/competitions/{competition_id}/clubs"
    response = requests.get(url)
    
    # Asegurarse de que la respuesta sea válida
    if response.status_code != 200:
        print(f"Error en la solicitud: {response.status_code}")
        return

    datos = response.json()

    # Imprimir los datos para inspección
    print("Datos de la respuesta para clubes:")
    print(datos)

    # Extraer la lista de clubes
    clubs = datos.get("clubs", [])

    if not clubs:
        print("No se encontraron clubes.")
        return

    # Mostrar los clubes encontrados al usuario
    print("Clubes encontrados:")
    for i, club in enumerate(clubs):
        print(f"{i+1}. {club['name']} (ID: {club['id']})")

    # Crear una carpeta con el nombre de la competición
    carpeta = os.path.join("data", competition_name)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Importar cada club en la competición
    for club in clubs:
        importTeam(club['name'], carpeta)

# Ejecutar la función principal
importLeague()
