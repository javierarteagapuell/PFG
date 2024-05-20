# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:27:21 2023

@author: javie
"""

import sqlite3
import csv

conn = sqlite3.connect('switrs.sqlite')
cursor = conn.cursor()

# Ejemplo: Obtener las primeras 10,000 filas de distintas tablas
consulta_tabla1 = 'SELECT * FROM case_ids LIMIT 10000'
cursor.execute(consulta_tabla1)
resultados_tabla1 = cursor.fetchall()

consulta_tabla2 = 'SELECT * FROM collisions LIMIT 10000'
cursor.execute(consulta_tabla2)
resultados_tabla2 = cursor.fetchall()

consulta_tabla3 = 'SELECT * FROM collisions LIMIT 10000'
cursor.execute(consulta_tabla3)
resultados_tabla3 = cursor.fetchall()

consulta_tabla4 = 'SELECT * FROM collisions LIMIT 10000'
cursor.execute(consulta_tabla4)
resultados_tabla4 = cursor.fetchall()

print("Resultados de tabla1:")
print("RS1  \n\n\n\n\n\n\n\n",resultados_tabla1)

print("Resultados de tabla2:")
print("RS2  \n\n\n\n\n\n\n\n",resultados_tabla2)

print("Resultados de tabla3:")
print("RS3  \n\n\n\n\n\n\n\n",resultados_tabla3)

print("Resultados de tabla4:")
print("RS4  \n\n\n\n\n\n\n\n",resultados_tabla4)

nombre_archivo_csv = 'tablafinal.csv'
with open(nombre_archivo_csv, 'w', newline='') as archivo_csv:
    # Crear el escritor CSV
    escritor_csv = csv.writer(archivo_csv)
    # Escribir los datos
    escritor_csv.writerows(resultados_tabla1)

print(f"Datos exportados a {nombre_archivo_csv}")

# Cerrar la conexión
conn.close()