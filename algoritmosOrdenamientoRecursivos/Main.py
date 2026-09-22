# -*- coding: utf-8 -*-
"""
@author: guest
"""
import time
from QuickSort import QuickSort
from mergesort import Mergesort


if __name__ == '__main__':
        #data = [9,6,4,3,2,1]
        #data = ["quicksort","burbuja","seleccion","inserción"]
        data = [30,50,12,15,45]
        print("QuickSort...")
        quick = QuickSort()
        tiempo_inicio = time.time()
        quick.ordenar(data);
        tiempo_fin = time.time()-tiempo_inicio
        print("Tiempo para quicksort: ", tiempo_fin)
       
        
        print("Mergesort...")
        data = [12,5,20,8,9]
        merge = Mergesort()
        tiempo_inicio = time.time()
        lista=merge.ordenar(data);
        tiempo_fin = time.time()-tiempo_inicio
        print("Tiempo para merget: ", tiempo_fin)
        print(lista)
    