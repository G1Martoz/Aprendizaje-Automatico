import pandas as pd
import numpy as np
import os

# Definimos la ruta base del script para encontrar los archivos en la misma carpeta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------
# 1. CARGA DE DATOS DE VENTAS (CSV)
# ---------------------------------------------------------
try:
    path_ventas = os.path.join(BASE_DIR, 'ventas.csv')
    ventas_df = pd.read_csv(path_ventas, encoding="ISO-8859-1")
    print("--- Punto 1: Vista previa de Ventas ---")
    print(ventas_df.head())
    print("\n")
except FileNotFoundError:
    print(f"Error: El archivo ventas.csv no se encuentra en {BASE_DIR}")

# ---------------------------------------------------------
# 2. CARGA DE DATOS DE CLIENTES (JSON)
# ---------------------------------------------------------
try:
    path_clientes = os.path.join(BASE_DIR, 'clientes.json')
    clientes_df = pd.read_json(path_clientes)
    print("--- Punto 2: Informacion de Clientes ---")
    print(f"Cantidad total de clientes registrados: {len(clientes_df)}")
    print("\n")
except FileNotFoundError:
    print(f"Error: El archivo clientes.json no se encuentra en {BASE_DIR}")

# ---------------------------------------------------------
# 3. CARGA DE INVENTARIO Y ANÁLISIS BÁSICO
# ---------------------------------------------------------
try:
    path_inventario = os.path.join(BASE_DIR, 'inventario.xlsx')
    # Usamos read_excel para archivos .xlsx
    inventario_df = pd.read_excel(path_inventario) 
    
    print("--- Punto 3: Analisis de Inventario ---")
    # Calculamos el promedio de la columna 'stock'
    promedio_stock = inventario_df['stock'].mean()
    print(f"El promedio de stock disponible es: {promedio_stock:.2f}")
    print("\n")
except FileNotFoundError:
    print(f"Error: El archivo inventario.xlsx no se encuentra en {BASE_DIR}")
except KeyError:
    print("Error: No se encontró la columna 'stock' en el archivo de inventario.")

# ---------------------------------------------------------
# INTRODUCCIÓN AL EDA (Análisis Exploratorio de Datos)
# ---------------------------------------------------------
print("--- Resumen Estadistico para el inicio del EDA (Ventas) ---")
if 'ventas_df' in locals():
    # describe() nos da media, desviación estándar, min, max y cuartiles
    print(ventas_df.describe())
    
    print("\n--- Estructura de los datos (Info) ---")
    print(ventas_df.info())
