# -*- coding: utf-8 -*-

class QuickSort:

    def ordenar(self, elementos):
        self.quick_sort_aux(elementos, 0, len(elementos) - 1)

    def quick_sort_aux(self, elementos, low, high):
        if low < high:
            pi = self.partition(elementos, low, high)
            self.quick_sort_aux(elementos, low, pi - 1)
            self.quick_sort_aux(elementos, pi + 1, high)

    def partition(self, elementos, low, high):
        pivot = elementos[low]
        left = low + 1
        right = high

        done = False
        while not done:
            while left <= right and elementos[left] <= pivot:
                left = left + 1
            while elementos[right] >= pivot and right >= left:
                right = right - 1
            if right < left:
                done = True
            else:
                elementos[left], elementos[right] = elementos[right], elementos[left]

        elementos[low], elementos[right] = elementos[right], elementos[low]
        return right


# Ejemplo de uso:
lista = [30, 50, 12, 15, 45]
qs = QuickSort()
qs.ordenar(lista)
print("Lista ordenada:", lista)
