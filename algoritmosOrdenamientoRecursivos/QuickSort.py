# -*- coding: utf-8 -*-
"""
@author: guest
"""
from OrdenableRecursivo import OrdenableRecursivoAbstractClass
class QuickSort(OrdenableRecursivoAbstractClass):

    def ordenar(self, elementos):
        print(elementos)
        self.quick_sort_aux(elementos, 0, len(elementos) - 1)
    
    def quick_sort_aux(self, elementos, left, right):
        index = self.partition(elementos, left, right)
        if left < index - 1:
            print("Sublist izquierda")
            self.quick_sort_aux(elementos, left, index - 1)
        if right >= index:
            print("Sublist derecha")
            self.quick_sort_aux(elementos, index, right)
    
    def partition(self, elementos, left, right):
        i = left
        j = right
        pivote = elementos[int((left + right) / 2)]
        print('\nLeft: {} Right: {} Piv Índice: {} Pivote: {}'.format(left, right, int((left + right) / 2), pivote))
        
        while i <= j:
            i = self.encuentra_mayor(elementos, i, pivote)
            j = self.encuentra_menor(elementos, j, pivote)
            if i <= j:
                self.intercambiar(elementos, i, j)
                i += 1
                j -= 1
        print(elementos)
        return i
    
    def intercambiar(self, elementos, i, j):
        aux = elementos[i]
        elementos[i] = elementos[j]
        elementos[j] = aux

    def encuentra_mayor(self, elementos, i, pivote):
        while elementos[i] < pivote:
            i += 1
        return i
    
    def encuentra_menor(self, elementos, j, pivote):
        while elementos[j] > pivote:
            j -= 1
        return j



    
    
            