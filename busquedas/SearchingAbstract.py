# -*- coding: utf-8 -*-

"""
 Clase abstracta para implementar diferentes tipos de ordenamientos
 con números reales
 Los números se ordenarán de MENOR A MAYOR
 Objetivo: Analizar su implementación y complejidad.
 @author Jess
 @version 1.0
"""
from abc import ABC, abstractmethod

class SearchingAbstractClass:
    @abstractmethod
    def secuencial(elementos, item):
        """
        Búsqueda  de elementos de forma secuencial
        Parameters
        ----------
        elementos : []float -Recibe una lista de números reales
        Returns
        -------
        int - regresa el índice donde se localiza el itewm a buscar o -1 si no se encuentra
        """
        pass
    @abstractmethod
    def binaria_iterativa(elementos, item):
        """
        Búsqueda  de elementos de forma secuencial
        Parameters
        ----------
        elementos : []float -Recibe una lista de números reales
        Returns
        -------
        int - regresa el índice donde se localiza el itewm a buscar o -1 si no se encuentra
        """
        pass
    @abstractmethod
    def binaria_recursiva(elementos, item):
        """
        Búsqueda  de elementos de forma secuencial
        Parameters
        ----------
        elementos : []float -Recibe una lista de números reales
        Returns
        -------
        int - regresa el índice donde se localiza el itewm a buscar o -1 si no se encuentra
        """
        pass

