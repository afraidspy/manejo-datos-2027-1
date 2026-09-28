class Nodo:
    def __init__(self, elemento=None,
                 siguiente=None):
        self.elemento = elemento
        self.siguiente = siguiente
        
    def __str__(self):
        return str(self.elemento)