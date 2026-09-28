# -*- coding: utf-8 -*-}


from SearchingClass import Searching


busqueda = Searching()

data = [20,30,40,50,60,70,80,90,100]
#[0,8]
#[5,8]

#data.secuencial(data,20)
#print(busqueda.secuencial(data,60))


print("Bsuqueda binaria iterativa")
print(busqueda.binaria_iterativa(data,90))

print("Bsuqueda binaria recursiva")
print(busqueda.binaria_recursiva(data,0))

