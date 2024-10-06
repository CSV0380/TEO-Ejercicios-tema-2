# ejercicio2.py
import matplotlib.pyplot as plt
from ejercicio1 import lee_variaciones_temperatura  # Importar desde ejercicio1

def muestra_variaciones_temperatura(ruta_csv):
    # Obtener los datos del CSV usando la función del ejercicio 1
    variaciones = lee_variaciones_temperatura(ruta_csv)
    
    # Separar las fechas y las variaciones de temperatura
    fechas = [x[0] for x in variaciones]
    variaciones_temp = [x[1] for x in variaciones]
    
    # Generar la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(fechas, variaciones_temp)

    # Mostrar la gráfica
    plt.show()

# Prueba de la función
ruta = 'TEO-Ejercicios-tema-2\data\monthly_csv.csv'
muestra_variaciones_temperatura(ruta)

