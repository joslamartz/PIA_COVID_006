import requests
import statistics

def obtener_datos(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.RequestException as e:
        print(f"Error al obtener datos: {e}")
        return None

def calcular_estadisticas_api2(datos):
    try:
        valores = [entry['timeline']['11/22/23'] for entry in datos]
        media = statistics.mean(valores)
        moda = statistics.mode(valores)
        maximo = max(valores)
        minimo = min(valores)
        mediana = statistics.median(valores)
        desviacion_estandar = statistics.stdev(valores)
        varianza = statistics.variance(valores)
        
        return media, moda, maximo, minimo, mediana, desviacion_estandar, varianza
    except statistics.StatisticsError:
        moda = "No hay moda única"
        return media, moda, maximo, minimo, mediana, desviacion_estandar, varianza

def main():
    datos_api2 = obtener_datos("https://disease.sh/v3/covid-19/vaccine/coverage/countries?lastdays=1")  # Reemplaza con la URL correcta

    if datos_api2:
        print("Datos de la API 2 obtenidos con éxito.")
    else:
        print("Error al obtener los datos de la API 2. Verifique su conexión a Internet o la URL.")

    while True:
        print("\nMenú de Estadísticas de Vacunación:")
        print("1. Media")
        print("2. Moda")
        print("3. Máximo")
        print("4. Mínimo")
        print("5. Mediana")
        print("6. Desviación Estándar")
        print("7. Varianza")
        print("8. Regresar")

        opcion = input("Seleccione una opción (1-8): ")

        if opcion == '1':
            resultado = calcular_estadisticas_api2(datos_api2)
            print(f"Media: {resultado[0]}")
        elif opcion == '2':
            resultado = calcular_estadisticas_api2(datos_api2)
            print(f"Moda: {resultado[1] if resultado[1] is not None else 'No hay moda única'}")
        elif opcion == '3':
            resultado = calcular_estadisticas_api2(datos_api2)
            print(f"Máximo: {resultado[2]}")
        elif opcion == '4':
            resultado = calcular_estadisticas_api2(datos_api2)
            print(f"Mínimo: {resultado[3]}")
        elif opcion == '5':
            resultado = calcular_estadisticas_api2(datos_api2)
            print(f"Mediana: {resultado[4]}")
        elif opcion == '6':
            resultado = calcular_estadisticas_api2(datos_api2)
            print(f"Desviación Estándar: {resultado[5]}")
        elif opcion == '7':
            resultado = calcular_estadisticas_api2(datos_api2)
            print(f"Varianza: {resultado[6]}")
        elif opcion == '8':
            return
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
