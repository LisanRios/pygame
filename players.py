import requests

# def buscarJugador():
#     print("Buscando jugador")
    
#     url = "https://retoolapi.dev/Fx4Gzq/data"
#     data = requests.get(url)
    
#     if data.status_code == 200:
#         data = data.json()
#         for e in data:
#             print(e['Column 1'])
    
    
#     return

# buscarJugador()


import requests
from bs4 import BeautifulSoup
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt 
import re 

# Variables para el nombre de los archivos
archivo_csv = 'archivo.csv'
datos_filtrados_csv = 'mercados/datos_filtrados.csv'

# URL de la página web para hacer scraping
url = "https://es.investing.com/equities/bolsas-y-mercados-argentinos-sa-historical-data"

# Obtención del contenido de la página web
request = requests.get(url)
soup = BeautifulSoup(request.text)

# Extracción de datos de la tabla HTML
tabla_html = soup.find_all("table")[0]
datos_tabla = pd.read_html(str(tabla_html))[0]

# Exportar los datos de la tabla a un archivo CSV
datos_tabla.to_csv(archivo_csv, index=None, header=True)

# Filtrar datos seleccionando solo las columnas 'Fecha' y '% var.'
datos_filtrados = datos_tabla[['Fecha', '% var.']]

# Mostrar una vista previa de los datos filtrados
print("Tabla con los datos filtrados:")
print(datos_filtrados.head())

# Exportar los datos filtrados a otro archivo CSV
datos_filtrados.to_csv(datos_filtrados_csv, index=False)

# Leer los datos del archivo CSV
datos_csv = pd.read_csv(archivo_csv)

# Eliminar el símbolo '%' de la columna '% var.' y convertir a tipo float
datos_csv['% var.'] = datos_csv['% var.'].str.strip('%').astype(float)