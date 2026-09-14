"""
Clase abstracta para implementar diferentes tipos de ordenamientos.
Los elementos se ordenan de MENOR A MAYOR.
Objetivo: analizar su implementación y complejidad.
"""
from abc import ABC, abstractmethod


class OrdenableIterativo(ABC):

    @abstractmethod
    def ordenar(self, elementos):
        """Ordena la lista en sitio y la devuelve."""
        ...

    def intercambiar(self, elementos, i, j):
        """Intercambia el elemento de la posición i por el de j y viceversa."""
        elementos[i], elementos[j] = elementos[j], elementos[i]

