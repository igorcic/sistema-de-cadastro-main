class Fornecedor():
    
    def __init__(self):
        self.__idFornecedor = None
        self.__nome = None
        self.__telefones = {}
        self.__emails = {}
        
    def setIdFornecedor(self, idFornecedor):
        self.__idFornecedor = idFornecedor

    def getIdFornecedor(self):
        return self.__idFornecedor

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def getTelefones(self):
        return self.__telefones

    def addTelefones(self,telefone):
        self.__telefones.add(telefone)

    def getEmails(self):
        return self.__emails

    def addEmails(self,email):
        self.__emails.add(email)

