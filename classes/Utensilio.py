class Utensilios():
    
    def __init__(self):
        self.__idUtensilios = None
        self.__nome = None
        self.__valorDeCompra = None
        
    def setIdUtensilios(self, idUtensilios):
        self.__idUtensilios = idUtensilios

    def getIdUtensilios(self):
        return self.__idUtensilios

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setValorDeCompra(self, valorDeCompra):
        self.__valorDeCompra = valorDeCompra

    def getValorDeCompra(self):
        return self.__valorDeCompra