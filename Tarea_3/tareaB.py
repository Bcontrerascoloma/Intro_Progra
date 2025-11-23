class Especie:
    def __init__(self, nombreEspecie):
        self.__nombre = nombreEspecie
        self.__ids = []               # lista de ID de animales de esta especie
        self.__avistamientos = []     # lista de strings "PuestoX YYYY-MM-DD HH:MM"
    
    def agregarID(self, identificador):
        if identificador not in self.ids: #agegamos el id a la lista de self.ids si solo si este id no esta en la lista, pues es unico para cada animal entonces hay que agrgarlo solo una vez
            self.ids.append(identificador)
    
    def agregarAvistamiento(self, avist):
        self.avistamientos.append(avist)

    def getIDS(self):
        return self.__ids
    def getNombre(self):
        return self.__nombre
    def getAvistamientos(self):
        return self.__avistamientos

lista_especies = []

