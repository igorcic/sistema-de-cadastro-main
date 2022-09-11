class Prato():
    
    def __init__(self):
        self.__idPrato = None
        self.__nome = None
        self.__valorDeVenda = None

    def setIdPrato(self, prato):
        self.__idPrato = prato
    
    def getIdPrato(self):
        return self.__idPrato

    def setNome(self, nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome

    def setValorDeVenda(self, valorDeVenda):
        self.__valorDeVenda = valorDeVenda
    
    def getValorDeVenda(self):
        return self.__valorDeVenda  

    