# -*- coding: utf-8 -*-
"""
REPASO DE HERENCIA EN PYTHON
Basado en los conceptos vistos en clase:
- Herencia simple  y mútliple 
- Sobreescritura de métodos 
- __init__ y uso de super()
- Encapsulamiento (getters/setters, atributos "privados")
- Polimorfismo--> Override
- Herencia múltiple

Completa cada ejercicio. Al final de cada ejercicio
hay una pequeña sección de pruebas para que verifiques tu solución.

Autor: Grupo de manejo de datos
"""

"""
Crea una clase base `Empleado` con atributos `nombre` y `salario_base`,
y un método `calcular_pago()` que regrese `salario_base`.

Luego crea dos clases hijas:
  - `Vendedor`: además tiene `comision` (monto extra). Sobreescribe
    `calcular_pago()` para regresar salario_base + comision.
  - `Gerente`: además tiene `bono` (monto extra). Sobreescribe
    `calcular_pago()` para regresar salario_base + bono.

Ambas clases hijas deben reutilizar el __init__ del padre con super().
"""


class Empleado:

    def __init__(self, nombre, salario_base):
        """ Constructor"""
        self.__nombre = nombre
        self.__salario_base = salario_base

    #empleado = Empleado("Pedro Picapiedra", 80000)
    def calcular_pago(self):
        return self.__salario_base

    def describeme(self):
        print(f"Soy {self.nombre}, un {type(self).__name__} y gano ${self.calcular_pago()}")


class Vendedor(Empleado):
    def __init__(self,nombre, salario_base, comision): 
        super().__init__(nombre, salario_base)
        self._comision = comision

    def calcular_pago(self):
        return super.__salario_base + self._comision
    

class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self._bono = bono

    def calcular_pago(self):
        return self().calcular_pago() + self._bono


def prueba_ejercicio_1():
    print("\n Prueba")
    v = Vendedor("Ana", 8000, 1500)
    g = Gerente("Luis", 15000, 3000)
    v.describeme()
    g.describeme()
    print("Pago esperado del vendedor: 9500 | obtenido:", v.calcular_pago())
    print("Pago esperado del gerente: 18000 | obtenido:", g.calcular_pago())

"""
Crea una clase base `Figura` con un método `area()` que regrese 0
(o lance NotImplementedError, para forzar a las hijas a implementarlo).

Crea las clases hijas `Rectangulo` (base, altura) y `Circulo` (radio),
cada una sobreescribiendo `area()` con su fórmula correspondiente.

Después, completa la función `area_total(figuras)` que reciba una
lista de figuras (de cualquier tipo) y regrese la suma de sus áreas,
SIN checar el tipo de cada una (esto es polimorfismo).
"""

import math

class Figura:
    def area(self):
        raise NotImplementedError("Las subclases deben implementar area()")


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base;
        self.altura = altura;

    def area(self):
        return self.base * self.altura;


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio;

    def area(self):
        return self.radio * self.radio * math.pi;

def area_total(figuras):
    total = 0;
    for fig in figuras:
        total += fig.area()
    return total;
    

def prueba_ejercicio_2():
    print("\n Ejercicio 2")
    figuras = [Rectangulo(4, 5), Circulo(3)]
    total = area_total(figuras)

    print("Total de área es: " , total)


"""
Crea una clase `CuentaBancaria` con un atributo "privado" __saldo
(inicializado en el constructor). Debe tener:
  - getSaldo(): regresa el saldo actual
  - depositar(monto): incrementa el saldo (monto debe ser > 0)
  - retirar(monto): decrementa el saldo, solo si hay saldo suficiente
    y monto > 0; si no, imprime un mensaje de error y no modifica el saldo
"""


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def getSaldo(self):
        #Completar
        pass

    def depositar(self, monto):
        #Completar
        pass

    def retirar(self, monto):
        #Completar
        pass


def prueba_ejercicio_3():
    print("\nPrueba Ejercicio 3-")
    cuenta = CuentaBancaria("Karla", 1000)
    cuenta.depositar(500)
    cuenta.retirar(300)
    print("Saldo esperado: 1200  obtenido:", cuenta.getSaldo())
    cuenta.retirar(999999) 
    print("Saldo esperado tras retiro inválido (no debe cambiar): 1200  obtenido:", cuenta.getSaldo())

 

"""
 dAgrega una nueva clase `Pez(Animal)` que:
  - sobreescriba hablar() para imprimir "Blub!"
  - sobreescriba moverse() para imprimir "Nadando"
  - defina un nuevo método `es_venenoso()` que regrese False por
    default, y que en una clase `PezGloboArgentino(Pez)` regrese True.

Esto refuerza: sobreescritura de métodos + un segundo nivel de
herencia (herencia en cadena).
"""


class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)


class Pez(Animal):
    def hablar(self):
        #Completar
        pass

    def moverse(self):
        #Completar
        pass

    def es_venenoso(self):
        #Completar
        pass


class PezGloboArgentino(Pez):
    def es_venenoso(self):
        #Completar
        pass


def prueba_ejercicio_4():
    print("\n Prueba Ejercicio 4")
    pez = Pez("acuático", 2)
    globo = PezGloboArgentino("acuático", 1)
    pez.hablar()
    pez.moverse()
    print("¿Pez normal es venenoso? esperado: False | obtenido:", pez.es_venenoso())
    print("¿Pez globo es venenoso? esperado: True | obtenido:", globo.es_venenoso())




if __name__ == "__main__":
    print("Herencia\n")
    try:
        prueba_ejercicio_1()
    except Exception as e:
        print(f"Ejercicio 1 {e}")
    try:
        prueba_ejercicio_2()
    except Exception as e:
        print(f"Ejercicio 2{e}")
    try:
        prueba_ejercicio_3()
    except Exception as e:
        print(f"Ejercicio  {e}")
    try:
        prueba_ejercicio_4()
    except Exception as e:
        print(f"Ejercicio 4 {e}")
