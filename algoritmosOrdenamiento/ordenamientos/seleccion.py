"""
Selección: en cada pasada busca el mínimo del tramo no ordenado
y lo coloca en su posición final.
"""
from .ordenable import OrdenableIterativo


class Seleccion(OrdenableIterativo):

    def ordenar(self, elementos):
        n = len(elementos)
        for i in range(n):
            minimo = i
            for j in range(i + 1, n):
                if elementos[j] < elementos[minimo]:
                    minimo = j
            if minimo != i:
                self.intercambiar(elementos, i, minimo)
        return elementos
