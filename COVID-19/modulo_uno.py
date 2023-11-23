import requests
import matplotlib.pyplot as plt

# Función para obtener los datos de la API de casos
def obtener_datos_casos():
    url_casos = "https://disease.sh/v3/covid-19/all"
    response_casos = requests.get(url_casos)
    datos_casos = response_casos.json()
    return datos_casos

# Función para obtener los datos de la API de países
def obtener_datos_paises():
    url_paises = "https://disease.sh/v3/covid-19/countries"
    response_paises = requests.get(url_paises)
    datos_paises = response_paises.json()
    return datos_paises

# Funciones para calcular los valores según las fórmulas (sin cambios)
def calcular_casos_por_millon(datos_casos):
    cases = datos_casos["cases"]
    population = datos_casos["population"]
    casos_por_millon = (cases / population) * 1_000_000
    return casos_por_millon

def calcular_muertes_por_millon(datos_casos):
    deaths = datos_casos["deaths"]
    population = datos_casos["population"]
    muertes_por_millon = (deaths / population) * 1_000_000
    return muertes_por_millon

def calcular_pruebas_por_millon(datos_casos):
    tests = datos_casos["tests"]
    population = datos_casos["population"]
    pruebas_por_millon = (tests / population) * 1_000_000
    return pruebas_por_millon

# Función para mostrar el menú (con títulos y nombres corregidos)
def mostrar_menu():
    print("Selecciona la opción que deseas:")
    print("1. Gráfico de Pastel: Distribución de Muertes en 5 Países Principales")
    print("2. Gráfico de Barras: 5 Países con Mayor Cantidad de Casos")
    print("3. Gráfico de Pastel: 5 Países con Menor Cantidad de Casos")
    print("4. Gráfico de Barras: 5 Países con Mayor Cantidad de Vacunas")
    print("5. Gráfico de Líneas: Evolución de Casos Actuales en 5 Países Principales")
    print("6. Regresar")

# Función principal
def main():
    datos_casos = obtener_datos_casos()
    datos_paises = obtener_datos_paises()
    
    while True:
        mostrar_menu()
        opcion = input("Ingresa el número de la opción que deseas (1-6): ")
        
        if opcion == "1":
            # Gráfico de pastel: Distribución de Muertes en 5 Países Principales
            paises = sorted(datos_paises, key=lambda x: x["deaths"], reverse=True)[:5]
            labels = [pais["country"] for pais in paises]
            muertes_paises = [pais["deaths"] for pais in paises]
            plt.pie(muertes_paises, labels=labels, autopct='%1.1f%%')
            plt.title("Distribución de Muertes en 5 Países Principales")
            plt.show()
        
        elif opcion == "2":
            # Gráfico de barras: 5 Países con Mayor Cantidad de Casos
            paises = sorted(datos_paises, key=lambda x: x["cases"], reverse=True)[:5]
            nombres_paises = [pais["country"] for pais in paises]
            casos_paises = [pais["cases"] for pais in paises]
            plt.bar(nombres_paises, casos_paises)
            plt.xlabel("Países")
            plt.ylabel("Casos Confirmados")
            plt.title("5 Países con Mayor Cantidad de Casos")
            plt.xticks(rotation=45)
            plt.show()
        
        elif opcion == "3":
            # Gráfico de pastel: 5 Países con Menor Cantidad de Casos
            paises = sorted(datos_paises, key=lambda x: x["cases"])[:5]
            labels = [pais["country"] for pais in paises]
            sizes = [pais["cases"] for pais in paises]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%')
            plt.title("Distribución de Casos en 5 Países con Menor Cantidad")
            plt.show()
        
        elif opcion == "4":
            # Gráfico de barras: 5 Países con Mayor Cantidad de Vacunas
            paises = sorted(datos_paises, key=lambda x: x["tests"], reverse=True)[:5]
            nombres_paises = [pais["country"] for pais in paises]
            vacunas_paises = [pais["tests"] for pais in paises]
            plt.bar(nombres_paises, vacunas_paises)
            plt.xlabel("Países")
            plt.ylabel("Número de Vacunas")
            plt.title("5 Países con Mayor Cantidad de Vacunas")
            plt.xticks(rotation=45)
            plt.show()
        
        elif opcion == "5":
            # Gráfico de líneas: Evolución de Casos Actuales en 5 Países Principales
            paises = sorted(datos_paises, key=lambda x: x["active"], reverse=True)[:5]
            nombres_paises = [pais["country"] for pais in paises]
            casos_actuales_paises = [pais["active"] for pais in paises]
            plt.plot(nombres_paises, casos_actuales_paises, marker='o')
            plt.xlabel("Países")
            plt.ylabel("Casos Actuales")
            plt.title("Evolución de Casos Actuales en 5 Países Principales")
            plt.xticks(rotation=45)
            plt.show()
            
        elif opcion == "6":
            return
        
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()
