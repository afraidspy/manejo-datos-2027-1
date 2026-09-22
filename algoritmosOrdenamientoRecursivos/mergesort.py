# -*- coding: utf-8 -*-
"""


@author: guest
"""
from OrdenableRecursivo import OrdenableRecursivoAbstractClass

class Mergesort(OrdenableRecursivoAbstractClass):

    def ordenar(self,elementos):
        print(elementos)
        if(len(elementos) <= 1):
            return elementos
        izq=[];
        der=[];
        indice_medio=len(elementos)//2
        for i in range(0,indice_medio):
            izq.append(elementos[i]);
            
        for i in range(indice_medio,len(elementos)):
            der.append(elementos[i]);
        izq=self.ordenar(izq)
        der=self.ordenar(der)
        return self.merge_aux(izq,der)
 
    def merge_aux(self,izq,der):
        lista =[];
        i=0;
        j=0;
        while(i < len(izq) and j < len(der)):
            if(izq[i] <= der[j]):
                lista.append(izq[i])
                i=i+1;
            else:
                lista.append(der[j])
                j=j+1;
                
        while(i < len(izq)):
            lista.append(izq[i])
            i=i+1;
        while(j < len(der)):
            lista.append(der[j])
            j=j+1;

        return lista