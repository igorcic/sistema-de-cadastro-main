class Funcionario():

    def __init__(self):
        self.__cpf = None
        self.__nome = None
        self.__supervisor = None
        self.__cargo = None
        self.__telefones = {}
        self.__emails = {}
        self.__data_de_contrato = None

    def getCpf(self):
        return self.__cpf

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getSupervisor(self):
        return self.__supervisor

    def setSupervisor(self, supervisor):
        self.__supervisor = supervisor

    def getCargo(self):
        return self.__cargo

    def setCargo(self, cargo):
        self.__cargo = cargo

    def getTelefones(self):
        return self.__telefones

    def addTelefones(self,telefone):
        self.__telefones.add(telefone)

    def getEmails(self):
        return self.__emails

    def addEmails(self,email):
        self.__emails.add(email)

    def getData_de_contrato(self):
        return self.__data_de_contrato

    def setData_de_contrato(self, data_de_contrato):
        self.__data_de_contrato = data_de_contrato