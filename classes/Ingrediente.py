class Ingrediente():
    
    def __init__(self):
        self.__idIngrediente = None
        self.__nome = None
        self.__tipo = None
        self.__validade = None
        self.__valorDeCompra = None
        self.__localDeArmazenamento = None


    def setIdIngrediente(self, idIngrediente):
        self.__idIngrediente = idIngrediente
    
    def getIdIngrediente(self):
        return self.__idIngrediente

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

    def setLocalDeArmazenamento(self, localDeArmazenamento):
        self.__localDeArmazenamento = localDeArmazenamento
    
    def getLocalDeArmazenamento(self):
        return self.__localDeArmazenamento