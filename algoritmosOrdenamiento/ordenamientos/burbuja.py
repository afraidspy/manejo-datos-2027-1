"""Burbuja en su versión básica: siempre recorre n pasadas completas."""
from .ordenable import OrdenableIterativo


class Burbuja(OrdenableIterativo):
    #[1,2,3]
    def ordenar(self, elementos):
        n = len(elementos)
        for i in range(n):           #O(N)                   
            for j in range(n - 1):  #O(N)                 
                if elementos[j] > elementos[j + 1]:     
                    self.intercambiar(elementos, j, j + 1)
        return elementos
