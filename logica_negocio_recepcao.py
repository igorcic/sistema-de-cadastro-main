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
        self.mydb.start_transaction(isolation_level='READ COMMITTED')
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
        result = self.Get_Cliente_ID(args[0])
        if result != None:
            sql = "UPDATE Mesa SET ID_Cliente = NULL WHERE ID_Cliente = %s"
            val = (result, )
            self.cursor.execute(sql, val)
            self.mydb.commit()
            sql = "DELETE FROM Clientes WHERE ID = %s"
            self.cursor.execute(sql, val)
            self.mydb.commit()
    
    def Mesas_Livres(self):
        sql = "SELECT ID, QTD_Lugares FROM Mesa WHERE ID_Cliente IS NULL"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def Aloca_Mesa(self,*args):
        # Padrao esperado args: (QTD_Lugares, ID_Cliente)
        sql = "SELECT ID FROM Mesa WHERE ID_Cliente = %s"
        tupla = (args[1], )
        self.cursor.execute(sql, tupla)
        result = self.cursor.fetchone()
        # Testa se o cliente já está alocado em uma mesa
        # Se nao, pode alocar uma mesa
        if result == None:
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
    
    def Get_Mesa(self, *args):
        # Padrao esperado args: ID_Cliente
        sql = "SELECT ID FROM Mesa WHERE ID_Cliente = %s"
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result
    
    def Get_Pedidos(self, *args):
        # Padrao esperado args: ID_Mesa
        sql = "SELECT ID FROM Pedidos WHERE ID_Mesa = %s"
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    def Get_Pratos_Pedido(self, *args):
        # Padrao esperado args: ID_Pedido
        sql = "SELECT ID_Prato FROM Pratos_Pedidos WHERE ID_Pedido = %s"
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        aux = []
        for i in result:
            sql = "SELECT ID,Nome FROM Pratos WHERE ID = %s"
            val = (i[0], )
            self.cursor.execute(sql, val)
            result2 = self.cursor.fetchone()
            aux.append(result2)
        return aux
        
    def Get_Bebidas_Pedido(self, *args):
        sql = "SELECT ID_Bebida FROM Bebidas_Pedidos WHERE ID_Pedido = %s"
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        aux = []
        for i in result:
            sql = "SELECT ID,Nome FROM Bebidas WHERE ID = %s"
            val = (i[0], )
            self.cursor.execute(sql, val)
            result2 = self.cursor.fetchone()
            aux.append(result2)
        return aux
            

    def Limpa_Mesa(self, *args):
        # Padrao esperado args: ID_Mesa
        sql = "SELECT ID FROM Pedidos WHERE ID_Mesa = %s"
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        if len(result) != 0:
            sql = "DELETE FROM Pedidos WHERE ID_Mesa = %s"
            self.cursor.execute(sql, args)
            self.mydb.commit()

        sql = "UPDATE Mesa SET ID_Cliente = NULL WHERE ID = %s"
        self.cursor.execute(sql, args)
        self.mydb.commit()

    def Get_Valor_Prato(self, *args):
        # Padrao esperado args: ID_Prato
        sql = "SELECT Valor_Venda FROM Pratos WHERE ID = %s"
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result
    
    def Get_Valor_Bebida(self, *args):
        # Padrao esperado args: ID_Bebida
        sql = "SELECT Valor_Venda FROM Bebidas WHERE ID = %s"
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

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
        aux2 = args[4]
        # Obtem o ID do pedido
        sql = "SELECT last_insert_id() FROM Pedidos"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        # Insere os pratos e as bebidas pedidas nas tabelas Pratos_Pedidos e Bebidas_Pedidos
        while len(aux) > 0:
            a = aux.pop(0)
            if a == 0:
                break
            sql = "INSERT INTO Pratos_Pedidos (ID_Pedido, ID_Prato) VALUES (%s, %s)"
            val = (result[0], a)
            self.cursor.execute(sql, val)
            self.mydb.commit()
        
        while len(aux2) > 0:
            b = aux2.pop(0)
            if b == 0:
                break
            sql = "INSERT INTO Bebidas_Pedidos (ID_Pedido, ID_Bebida) VALUES (%s, %s)"
            val = (result[0], b)
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

