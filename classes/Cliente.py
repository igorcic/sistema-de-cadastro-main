class Cliente():
    
    def __init__(self):
        self.__idCliente = None
        self.__nome = None
        self.__cpf = None
        
    def setIdCliente(self, idCliente):
        self.__idCliente = idCliente

    def getIdCliente(self):
        return self.__idCliente

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getCpf(self):
        return self.__cpf