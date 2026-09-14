"""
Inserción: toma el elemento i y lo hace descender hasta su lugar
dentro del prefijo que ya está ordenado.
"""
from .ordenable import OrdenableIterativo


class Insercion(OrdenableIterativo):

    def ordenar(self, elementos):
        for i in range(1, len(elementos)):
            for j in range(i - 1, -1, -1):
                if elementos[j] <= elementos[j + 1]:
                    break       # el prefijo ya está ordenado: no hay más que bajar
                self.intercambiar(elementos, j, j + 1)
        return elementos
