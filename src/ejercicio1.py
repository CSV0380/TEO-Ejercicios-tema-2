import csv


def lee_variaciones_temperatura(ruta_csv):
    variaciones = []
    
    # Abrimos el archivo CSV para lectura
    with open(ruta_csv, newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)
        next(lector)
        # Iteramos sobre las filas del CSV
        for fila in lector:
            fecha = fila[0]  # Primera columna: fecha
            variacion_temp = fila[1]  # Segunda columna: variación de temperatura
            variaciones.append((fecha, variacion_temp))  # Añadimos la tupla (fecha, variación) a la lista
    
    return variaciones

# Prueba de la función
if __name__ == "__main__":
    ruta = "TEO-Ejercicios-tema-2\data\monthly_csv.csv"

    datos_temperatura = lee_variaciones_temperatura(ruta)

    # Mostrar las 5 primeras tuplas
    print(datos_temperatura[:5])
