"""
Burbuja con dos mejoras:
  1. La cola ya ordenada no se vuelve a recorrer (n - i - 1).
  2. Si una pasada no hace intercambios, la lista ya está ordenada y se corta.
"""
from .ordenable import OrdenableIterativo


class BurbujaMejorado(OrdenableIterativo):

    def ordenar(self, elementos):
        n = len(elementos) #[1,2,3] #[1,2,3,4,6,5]
        for i in range(n):
            hubo_intercambio = False
            for j in range(n - i - 1):
                if elementos[j] > elementos[j + 1]:
                    self.intercambiar(elementos, j, j + 1)
                    hubo_intercambio = True
            if not hubo_intercambio:
                break
        return elementos
