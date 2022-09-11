class Bebida():
    
    def __init__(self):
        self.__idBebida = None
        self.__nome = None
        self.__tipo = None
        self.__validade = None
        self.__valorDeCompra = None
        self.__valorDeVenda = None


    def setIdBebida(self, idBebida):
        self.__idBebida = idBebida
    
    def getIdBebida(self):
        return self.__idBebida

    def setNome(self, nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome

    def setTipo(self, tipo):
        self.__tipo = tipo
    
    def getTipo(self):
        return self.__tipo

    def setValidade(self, validade):
        self.__validade = validade
    
    def getValidade(self):
        return self.__validade

    def setValorDeCompra(self, valorDeCompra):
        self.__valorDeCompra = valorDeCompra
    
    def getValorDeCompra(self):
        return self.__valorDeCompra

    def setValorDeVenda(self, valorDeVenda):
        self.__valorDeVenda = valorDeVenda
    
    def getValorDeVenda(self):
        return self.__valorDeVenda