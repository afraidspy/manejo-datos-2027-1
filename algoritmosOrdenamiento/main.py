"""
Compara el tiempo de los cuatro ordenamientos sobre la misma entrada.
Ejecutar:  python main.py
"""
import random
import time

from ordenamientos import Burbuja, BurbujaMejorado, Seleccion, Insercion

TAMANIO = 1000

ALGORITMOS = [
    ("Burbuja", Burbuja()),
    ("Burbuja mejorado", BurbujaMejorado()),
    ("Seleccion", Seleccion()),
    ("Insercion", Insercion()),
]


def generar_aleatorios(cantidad):
    datos = []
    for i in range(cantidad):
        datos.append(random.randint(1, 10000000))
    return datos

#https://docs.python.org/es/3/library/time.html#time.perf_counter
def medir(algoritmo, datos):
    inicio = time.perf_counter()
    algoritmo.ordenar(datos.copy())
    fin = time.perf_counter()
    return fin - inicio


def main():
    datos = generar_aleatorios(TAMANIO)
    print("n =", TAMANIO)
    print()

    for nombre, algoritmo in ALGORITMOS:
        tiempo = medir(algoritmo, datos)
        print("Tiempo para", nombre, ":", round(tiempo, 4), "segundos")


if __name__ == "__main__":
    main()