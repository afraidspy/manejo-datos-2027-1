
"""
 Clase abstracta para implementar ordenamientos usando recursion
 Los elementos se ordenarán de MENOR A MAYOR
 Objetivo: Analizar su implementación y complejidad.
 @author 
 @version 1.0
"""
from abc import ABC, abstractmethod

class OrdenableRecursivoAbstractClass(ABC):
   @abstractmethod
   def ordenar(elementos):
       pass
