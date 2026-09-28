from SearchingAbstract import SearchingAbstractClass
class Searching(SearchingAbstractClass):
    
    
    def secuencial(self, elementos, item): 
        for index in range(len(elementos)):
            if elementos[index] == item:
                return index
        return -1
    #[4,4,4,4,4,4,4] 
    def binaria_iterativa(self,elementos, item):    
        inicio = 0
        fin = len(elementos) -1
        indice_encontrado = -1

        while inicio<=fin:
            print("inicio: {} fin_{}".format(inicio,fin))
            indice_medio = (fin+inicio) // 2
            print("Medio: ", indice_medio)
            if (elementos[indice_medio] == item):
                indice_encontrado = indice_medio
                return indice_encontrado
            else:
                if item < elementos[indice_medio]:
                    #[0,indice_medio-1]
                    fin = indice_medio -1 
                else:
                    #[indice_medio+1,fin]
                    inicio = indice_medio+1
            
        return -1
     
    def binaria_recursiva(self,elementos, item):
       return self.divide(elementos, item, 0, len(elementos)-1)
   
    def divide(self,elementos, item, inicio, fin):
        #[90,100,110,130,150]  (2+4)//2
        indice_medio = (inicio + fin) // 2
        print("inicio: {} fin: {} ".format(inicio,fin))
        print("Indice_medio: ", indice_medio)
        
        if elementos[indice_medio] == item:
            
            return indice_medio
        
        if inicio > fin:
            return -1
        
        if item < elementos[indice_medio]:
            
            return self.divide(elementos, item, inicio, indice_medio-1)
        else:
            return self.divide(elementos, item, indice_medio+1,fin)
   