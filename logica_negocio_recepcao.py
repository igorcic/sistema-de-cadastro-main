import mysql.connector
import re

class Recepcao:
    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd
        self.mydb = mysql.connector.connect(
            user=user, 
            password=passwd, 
            host='localhost',
            auth_plugin='mysql_native_password', 
            database='Restaurante_BD')
        self.cursor = self.mydb.cursor(buffered=True)
    
    def __del__(self):
        if self.mydb.is_connected():
            self.cursor.close()
            self.mydb.close()
            
    def Get_Cliente_ID(self, *args):
        # Padrao esperado args: Nome ou CPF
        if re.findall("\d", args[0]) == []:
            sql = "SELECT ID FROM Clientes WHERE Nome = %s"
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            return result[0]
        else:
            sql = "SELECT ID FROM Clientes WHERE CPF = %s"
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            return result[0]

    def Add_Cliente(self, *args):
        # Padrao esperado args: (Nome, CPF) ou Nome
        if re.findall("\d", args[0]) == []:
            if len(args) == 2:
                sql = "SELECT CPF From Clientes WHERE CPF = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result == None and len(args[1]) == 11:
                    sql = "INSERT INTO Clientes (Nome, CPF) VALUES (%s, %s)"
                    val = args
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
            elif len(args) == 1:
                sql = "INSERT INTO Clientes " "(Nome) " "VALUE (%s)"
                val = args
                self.cursor.execute(sql, val)
                self.mydb.commit()
    
    def Del_Cliente(self, *args):
        #Padrao esperado args: Nome ou CPF
        if re.findall("\d", args[0]) != []: # Testa se o argumento tem números
            sql = "DELETE FROM Clientes WHERE CPF = %s"
            val = args
            self.cursor.execute(sql, val)
            self.mydb.commit()
        else:
            sql = "DELETE FROM Clientes WHERE Nome = %s"
            val = args
            self.cursor.execute(sql, val)
            self.mydb.commit()

    def Aloca_Mesa(self,*args):
        # Padrao esperado args: (QTD_Lugares, ID_Cliente)
        sql = "SELECT ID FROM Mesa WHERE ID_Cliente = %s"
        tupla = (args[1], )
        self.cursor.execute(sql, tupla)
        result = self.cursor.fetchone()
        # Testa se o cliente já está alocado em uma mesa
        # Se nao, pode alocar uma mesa
        if len(result) == 0:
            sql = "SELECT ID, QTD_Lugares FROM Mesa WHERE ID_Cliente IS NULL"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            for i in range(len(result)):
                if result[i][1] >= args[0]:
                    sql = "UPDATE Mesa SET ID_Cliente = %s WHERE ID = %s"
                    val = (args[1], result[i][0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
                    break

    def Faz_Pedido(self, *args):
        # Padrao esperado args: (Total, ID_Func, ID_Mesa, [[ID_Pratos], [ID_Bebidas]])
        sql = "SELECT now()"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        # Insere o pedido na tabela Pedidos
        sql = "INSERT INTO Pedidos (Data_Pedido, Total, ID_Func, ID_Mesa) VALUES (%s, %s, %s, %s)"
        val = (result[0], args[0], args[1], args[2])
        self.cursor.execute(sql, val)
        self.mydb.commit()
        aux = args[3]
        # Obtem o ID do pedido
        sql = "SELECT last_insert_id() FROM Pedidos"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        # Insere os pratos e as bebidas pedidas nas tabelas Pratos_Pedidos e Bebidas_Pedidos
        while len(aux) > 0:
            a = aux.pop(0)
            for i in range(len(a)):
                sql = "INSERT INTO Pratos_Pedidos (ID_Pedido, ID_Prato) VALUES (%s, %s)"
                val = (result[0], a[i])
                self.cursor.execute(sql, val)
                self.mydb.commit()
            
            b = aux.pop(0)
            for i in range(len(a)):
                sql = "INSERT INTO Bebidas_Pedidos (ID_Pedido, ID_Bebida) VALUES (%s, %s)"
                val = (result[0], b[i])
                self.cursor.execute(sql, val)
                self.mydb.commit()
        
    def Limpa_Pedidos_Cliente(self, *args):
        # Padrao esperado args: CPF cadastrado ou Nome
        id = self.Get_Cliente_ID(args[0])
        val = (id, )
        sql = "SELECT ID FROM Mesa WHERE ID_Cliente = %s"
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        sql = "SELECT ID FROM Pedidos WHERE ID_Mesa = %s"
        self.cursor.execute(sql, result)
        result = self.cursor.fetchall()
        for i in range(len(result)):
            sql = "DELETE FROM Pratos_Pedidos WHERE ID_Pedido = %s"
            val = (result[i][0], )
            self.cursor.execute(sql, val)
            self.mydb.commit()
            sql = "DELETE FROM Bebidas_Pedidos WHERE ID_Pedido = %s"
            val = (result[i][0], )
            self.cursor.execute(sql, val)
            self.mydb.commit()
            sql = "DELETE FROM Pedidos WHERE ID = %s"
            val = (result[i][0], )
            self.cursor.execute(sql, val)
            self.mydb.commit()
    
    def Cardapio(self):
        sql = "SELECT * FROM Cardapio"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    # TODO  - Definir uma forma de obter o cardapio


class Gerencia:
    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = user,
            passwd = passwd,
            auth_plugin = 'mysql_native_password',
            database = "Restaurante_BD")
        self.cursor = self.mydb.cursor()

    def __del__(self):
        if self.mydb.is_connected():
            self.cursor.close()
            self.mydb.close()
    
    def Add_Fornecedor(self, Nome):
        sql = "INSERT INTO Fornecedores " "(Nome) " "VALUE (%s)"
        val = (Nome, )
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def Get_Fornecedor_ID(self, Nome):
        sql = "SELECT ID FROM Fornecedores WHERE Nome = %s"
        val = (Nome, )
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        return result[0]
    
    def Get_Fornecedor_Nome(self, ID):
        sql = "SELECT Nome FROM Fornecedores WHERE ID = %s"
        val = (ID, )
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        return result[0]
    
    def Del_Fornecedor(self, Nome):
        sql = "DELETE FROM Fornecedores WHERE Nome = %s"
        val = (Nome, )
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def Add_Telefone_Fornecedor(self, Nome, Telefone):
        sql = "INSERT INTO Telefone_Fornecedores " "(ID_Forn, Telefone) " "VALUE (%s, %s)"
        val = (self.Get_Fornecedor_ID(Nome), Telefone)
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def Add_Email_Fornecedor(self, Nome, Email):
        sql = "INSERT INTO Email_Fornecedores" "(ID_Forn, Email) " "VALUE (%s, %s)"
        val = (self.Get_Fornecedor_ID(Nome), Email)
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    def Add_Funcionario(self, Nome):
        sql = "INSERT INTO Funcionarios " "(Nome) " "VALUE (%s)"
        val = (Nome, )
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def Get_Funcionario_CPF(self, Nome):
        sql = "SELECT CPF FROM Funcionarios WHERE Nome = %s"
        val = (Nome, )
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        return result[0]
    
    def Get_Funcionario_Nome(self, CPF):
        sql = "SELECT Nome FROM Fornecedores WHERE CPF = %s"
        val = (ID, )
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        return result[0]
    
    def Del_Funcionario(self, Nome):
        sql = "DELETE FROM Funcionarios WHERE Nome = %s"
        val = (self.Get_Funcionario_Nome, )
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def Add_Telefone_Func(self, Nome, Telefone):
        sql = "INSERT INTO Telefone_Func " "(ID_Forn, Telefone) " "VALUE (%s, %s)"
        val = (self.Get_Fornecedor_ID(Nome), Telefone)
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def Add_Email_Fornecedor(self, Nome, Email):
        sql = "INSERT INTO Email_Fornecedores" "(ID_Forn, Email) " "VALUE (%s, %s)"
        val = (self.Get_Fornecedor_ID(Nome), Email)
        self.cursor.execute(sql, val)
        self.mydb.commit()