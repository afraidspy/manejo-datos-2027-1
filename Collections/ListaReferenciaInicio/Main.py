# -*- coding: utf-8 -*-
from ListasClass  import ListaClass
estudiantes = ListaClass()

estudiantes.agregar("Diego")
estudiantes.agregar("Pedro")
estudiantes.agregar("Mariana")
estudiantes.agregar("Saul")

estudiantes.imprimir()
estudiantes.eliminar("Mariana")
estudiantes.imprimir()

estudiantes.eliminar("Saul")
estudiantes.imprimir()

estudiantes.sustituir("Diego","Lola")
estudiantes.imprimir()
estudiantes.vaciar()
estudiantes.imprimir()
try:
    print(estudiantes.primer_elemento())
except :
   pass
    