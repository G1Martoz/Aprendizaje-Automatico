import pandas as pd
import numpy as np
import os

# Definimos la ruta base del script para encontrar los archivos en la misma carpeta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------
# 1. CARGA DE DATOS DE VENTAS (CSV)
# ---------------------------------------------------------
# Cargamos el archivo de ventas y mostramos una vista previa
try:
    path_ventas = os.path.join(BASE_DIR, 'ventas.csv')
    ventas_df = pd.read_csv(path_ventas, encoding="ISO-8859-1")
    print("--- Punto 1: Vista previa de Ventas ---")
    print(ventas_df.head())
    print("\n")
except FileNotFoundError:
    print(f"Error: El archivo {path_ventas} no se encuentra.")

# ---------------------------------------------------------
# 2. CARGA DE DATOS DE CLIENTES (JSON)
# ---------------------------------------------------------
# Usamos read_json para importar los datos de clientes
try:
    path_clientes = os.path.join(BASE_DIR, 'clientes.json')
    clientes_df = pd.read_json(path_clientes)
    print("--- Punto 2: Información de Clientes ---")
    print(f"Cantidad total de clientes: {len(clientes_df)}")
    print("\n")
except FileNotFoundError:
    print(f"Error: El archivo {path_clientes} no se encuentra.")

# ---------------------------------------------------------
# 3. CARGA DE INVENTARIO (EXCEL) Y ANÁLISIS BÁSICO
# ---------------------------------------------------------
# Importamos el inventario desde Excel y calculamos el promedio
try:
    path_inventario = os.path.join(BASE_DIR, 'inventario.xlsx')
    inventario_df = pd.read_excel(path_inventario)
    print("--- Punto 3: Análisis de Inventario ---")
    promedio_stock = inventario_df['stock'].mean()
    print(f"El promedio de stock disponible es: {promedio_stock:.2f}")
    print("\n")
except FileNotFoundError:
    print(f"Error: El archivo {path_inventario} no se encuentra.")

# ---------------------------------------------------------
# EXTRA: COMBINACIÓN DE DATOS (OPCIONAL SEGÚN LA CONSIGNA)
# ---------------------------------------------------------
# Intentamos combinar ventas con inventario por nombre de producto
# Nota: ventas_df tiene 'producto' e inventario_df tiene 'nombre'
try:
    # Realizamos un merge para ver la información combinada de ventas e inventario
    # combinados_df = pd.merge(ventas_df, inventario_df, left_on='producto', right_on='nombre')
    # print("--- Extra: Datos Combinados (Ventas + Inventario) ---")
    # print(combinados_df.head())
    pass
except NameError:
    pass

# ---------------------------------------------------------
# INTRODUCCIÓN AL EDA (Análisis Exploratorio de Datos)
# ---------------------------------------------------------
print("--- Resumen Estadistico para el inicio del EDA ---")
if 'ventas_df' in locals():
    print(ventas_df.describe())