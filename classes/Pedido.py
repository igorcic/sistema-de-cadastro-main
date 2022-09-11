class Pedido():
    
    def __init__(self):
        self.__idPedido = None
        self.__valorTotal = None
        self.__data = None
        
    def setIdPedido(self, idPedido):
        self.__idPedido = idPedido

    def getIdPedido(self):
        return self.__idPedido

    def setValorTotal(self, valorTotal):
        self.__valorTotal = valorTotal

    def getValorTotal(self):
        return self.__valorTotal

    def setData(self, data):
        self.__data = data

    def getData(self):
        return self.__data