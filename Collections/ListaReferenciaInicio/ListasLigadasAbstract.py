"""
 Clase abstracta para el TDA de una lista liga
 Objetivo: Analizar su implementación y complejidad de cada uno de sus métodos
 @author Jessica
 @version 1.0
"""
from abc import ABC, abstractmethod

class ListaLigadasAbstract:
    @abstractmethod
    def esta_vacia():
        pass
    @abstractmethod
    def vaciar():
        pass
    @abstractmethod
    def agregar(elemento):
        pass
    @abstractmethod
    def contiene(elemento):
        pass
    @abstractmethod
    def primer_elemento():
        pass
    @abstractmethod
    def eliminar(eliminar):
        pass
    @abstractmethod
    def sustituir(actual,nuevo):
        pass
    @abstractmethod
    def imprimir():
        pass
    @abstractmethod
    def iterador():
        pass
    

        