from ejercicio1 import lee_variaciones_temperatura
import matplotlib.pyplot as plt
from datetime import datetime

def muestra_variaciones_temperatura(ruta_csv, fecha_inicial = None, fecha_final = None):
    # Leer las variaciones de temperatura
    variaciones = lee_variaciones_temperatura(ruta_csv)

    # Inicializar listas para las fechas y variaciones
    fechas = []
    variaciones_temp = []
    
    for fecha_str, variacion_temp in variaciones:
        fecha = datetime.strptime(fecha_str, '%d/%m/%Y')  # Cambiamos el formato a dd/mm/yyyy
        
        # Verificar si las fechas son válidas o None
        if (fecha_inicial is None or fecha >= datetime.strptime(fecha_inicial, '%d/%m/%Y')) and \
           (fecha_final is None or fecha <= datetime.strptime(fecha_final, '%d/%m/%Y')):
            fechas.append(fecha)
            variaciones_temp.append(variacion_temp)

    # Graficar
    plt.figure(figsize=(10, 5))
    plt.plot(fechas, variaciones_temp, marker='o')
    plt.title('Evolución de Variaciones de Temperatura (Filtrado)')
    plt.xlabel('Fecha')
    plt.ylabel('Variación de Temperatura')
    plt.grid()
    plt.show()

# Prueba de la función sin filtro (pasando None) y con fechasç

if __name__ == '__main__':
    ruta = 'TEO-Ejercicios-tema-2\data\monthly_csv.csv'  # Asegúrate de que la ruta sea correcta
    print("Gráfica sin filtro:")
    muestra_variaciones_temperatura(ruta)  # Sin restricciones de fechas
    print("Gráfica con filtro de fechas:")
    muestra_variaciones_temperatura(ruta, fecha_inicial='01/01/2016', fecha_final='31/12/2016')  # Con filtro de fechas

