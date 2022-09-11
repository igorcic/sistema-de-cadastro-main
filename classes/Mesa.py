class Mesa():
    
    def __init__(self):
        self.__idMesa = None
        self.__qtdLugares = None

    def setIdMesa(self, idMesa):
        self.__idMesa = idMesa

    def getIdMesa(self):
        return self.__idMesa

    def setQtdLugares(self, qtdLugares):
        self.__qtdLugares = qtdLugares

    def getQtdLugares(self):
        return self.__qtdLugares