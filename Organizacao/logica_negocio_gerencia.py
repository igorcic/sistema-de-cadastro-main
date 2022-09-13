import mysql.connector
import re

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
        self.cursor = self.mydb.cursor(buffered=True)

    def __del__(self):
        if self.mydb.is_connected():
            self.cursor.close()
            self.mydb.close()
    
    def Get_Fornecedor(self):
        sql = "SELECT ID, Nome FROM Fornecedores order by ID"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def Add_Fornecedor(self, *args):
        # Padrao de dados: Nome do fornecedor
        sql = "SELECT ID FROM Fornecedores WHERE Nome = %s"
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        if result == None:
            sql = "INSERT INTO Fornecedores " "(Nome) " "VALUE (%s)"
            self.cursor.execute(sql, args)
            self.mydb.commit()

    def Get_Fornecedor_Data(self, *args):
        # Padrao de dados: Nome ou ID
        if re.findall("\d", args[0]) == []:
            sql = "SELECT ID FROM Fornecedores WHERE Nome = %s"
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            return result
        else:
            sql = "SELECT Nome FROM Fornecedores WHERE ID = %s"
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            return result
    
    def Del_Fornecedor(self, *args):
        # Padrao de dados: Nome ou ID
        if re.findall("\d", args[0]) == []:
            sql = "SELECT ID FROM Fornecedores WHERE Nome = %s"
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            if result != None:
                if re.findall("\d", args[0]) == []:
                    sql = "SELECT ID_Forn FROM Ingredientes WHERE ID_Forn = %s"
                    val = (self.Get_Fornecedor_Data(args[0]), )
                    self.cursor.execute(sql, val)
                    result = self.cursor.fetchone()
                    sql = "SELECT ID_Forn FROM Bebidas WHERE ID_Forn = %s"
                    val = (self.Get_Fornecedor_Data(args[0]), )
                    self.cursor.execute(sql, val)
                    result2 = self.cursor.fetchone()
                    if result == None and result2 == None:
                        sql = "DELETE FROM Fornecedores WHERE Nome = %s"
                        self.cursor.execute(sql, args)
                        self.mydb.commit()
                    else:
                        sql = "UPDATE Ingredientes SET ID_Forn = 1 WHERE ID_Forn = %s"
                        val = (self.Get_Fornecedor_Data(args[0]), )
                        self.cursor.execute(sql, val)
                        self.mydb.commit()
                        sql = "UPDATE Bebidas SET ID_Forn = 1 WHERE ID_Forn = %s"
                        val = (self.Get_Fornecedor_Data(args[0]), )
                        self.cursor.execute(sql, val)
                        self.mydb.commit()
                        sql = "DELETE FROM Fornecedores WHERE Nome = %s"
                        self.cursor.execute(sql, args)
                        self.mydb.commit()
                else:
                    sql = "SELECT ID_Forn FROM Ingredientes WHERE ID_Forn = %s"
                    val = (self.Get_Fornecedor_Data(args[0]), )
                    self.cursor.execute(sql, val)
                    result = self.cursor.fetchone()
                    sql = "SELECT ID_Forn FROM Bebidas WHERE ID_Forn = %s"
                    val = (self.Get_Fornecedor_Data(args[0]), )
                    self.cursor.execute(sql, val)
                    result2 = self.cursor.fetchall()
                    if result == None and result2 == None:
                        sql = "DELETE FROM Fornecedores WHERE ID = %s"
                        self.cursor.execute(sql, args)
                        self.mydb.commit()
                    else:
                        sql = "UPDATE Ingredientes SET ID_Forn = 1 WHERE ID_Forn = %s"
                        val = (self.Get_Fornecedor_Data(args[0]), )
                        self.cursor.execute(sql, val)
                        self.mydb.commit()
                        sql = "UPDATE Bebidas SET ID_Forn = 1 WHERE ID_Forn = %s"
                        val = (self.Get_Fornecedor_Data(args[0]), )
                        self.cursor.execute(sql, val)
                        self.mydb.commit()
                        sql = "DELETE FROM Fornecedores WHERE Nome = %s"
                        self.cursor.execute(sql, args)
                        self.mydb.commit()
        else:
            sql = "SELECT ID FROM Fornecedores WHERE ID = %s"
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            if result != None:
                if re.findall("\d", args[0]) == []:
                    sql = "SELECT ID_Forn FROM Ingredientes WHERE ID_Forn = %s"
                    val = (self.Get_Fornecedor_Data(args[0]), )
                    self.cursor.execute(sql, val)
                    result = self.cursor.fetchone()
                    sql = "SELECT ID_Forn FROM Bebidas WHERE ID_Forn = %s"
                    val = (self.Get_Fornecedor_Data(args[0]), )
                    self.cursor.execute(sql, val)
                    result2 = self.cursor.fetchone()
                    if result == None and result2 == None:
                        sql = "DELETE FROM Fornecedores WHERE Nome = %s"
                        self.cursor.execute(sql, args)
                        self.mydb.commit()
                    else:
                        sql = "UPDATE Ingredientes SET ID_Forn = 1 WHERE ID_Forn = %s"
                        val = (self.Get_Fornecedor_Data(args[0]), )
                        self.cursor.execute(sql, val)
                        self.mydb.commit()
                        sql = "UPDATE Bebidas SET ID_Forn = 1 WHERE ID_Forn = %s"
                        val = (self.Get_Fornecedor_Data(args[0]), )
                        self.cursor.execute(sql, val)
                        self.mydb.commit()
                        sql = "DELETE FROM Fornecedores WHERE Nome = %s"
                        self.cursor.execute(sql, args)
                        self.mydb.commit()
                else:
                    sql = "SELECT ID_Forn FROM Ingredientes WHERE ID_Forn = %s"
                    val = (self.Get_Fornecedor_Data(args[0]), )
                    self.cursor.execute(sql, val)
                    result = self.cursor.fetchone()
                    sql = "SELECT ID_Forn FROM Bebidas WHERE ID_Forn = %s"
                    val = (self.Get_Fornecedor_Data(args[0]), )
                    self.cursor.execute(sql, val)
                    result2 = self.cursor.fetchall()
                    if result == None and result2 == None:
                        sql = "DELETE FROM Fornecedores WHERE Nome = %s"
                        self.cursor.execute(sql, args)
                        self.mydb.commit()
                    else:
                        sql = "UPDATE Ingredientes SET ID_Forn = 1 WHERE ID_Forn = %s"
                        val = (self.Get_Fornecedor_Data(args[0]), )
                        self.cursor.execute(sql, val)
                        self.mydb.commit()
                        sql = "UPDATE Bebidas SET ID_Forn = 1 WHERE ID_Forn = %s"
                        val = (self.Get_Fornecedor_Data(args[0]), )
                        self.cursor.execute(sql, val)
                        self.mydb.commit()
                        sql = "DELETE FROM Fornecedores WHERE Nome = %s"
                        self.cursor.execute(sql, args)
                        self.mydb.commit()

    def Add_Telefone_Fornecedor(self, *args):
        # Padrao de dados: Nome do fornecedor, Telefone
        sql = "SELECT ID FROM Fornecedores WHERE Nome = %s"
        val = (args[0], )
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result != None:
            sql = "SELECT Telefone FROM Telefone_Fornecedores WHERE Telefone = %s"
            val = (args[1], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result == None:
                sql = "INSERT INTO Telefone_Fornecedores " "(ID_Forn, Telefone) " "VALUE (%s, %s)"
                val = (self.Get_Fornecedor_Data(args[0]), args[1])
                self.cursor.execute(sql, val)
                self.mydb.commit()

    def Add_Email_Fornecedor(self, *args):
        # Padrao de dados: Nome do fornecedor, Email
        sql = "SELECT ID FROM Fornecedores WHERE Nome = %s"
        val = (args[0], )
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result != None:
            sql = "SELECT Email FROM Email_Fornecedores WHERE Email = %s"
            val = (args[1], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result == None:
                sql = "INSERT INTO Email_Fornecedores" "(ID_Forn, Email) " "VALUE (%s, %s)"
                val = (self.Get_Fornecedor_Data(args[0]), args[1])
                self.cursor.execute(sql, val)
                self.mydb.commit()


    #   FIM FUNCIONARIOS


    def Add_Funcionario(self, *args):
        # Padrao de dados: (Nome, CPF, Cargo) ou (Nome, CPF, Data_Contrato, Cargo)
        sql = "SELECT CPF FROM Funcionarios WHERE Nome = %s"
        val = (args[0], )
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result == None and len(args[1]) == 11 and len(args) == 3:
            if args[2] == 'CHEF' or args[2] == 'RECEPCAO' or args[2] == 'ADMINISTRACAO':
                sql = "INSERT INTO Funcionarios  (Nome, CPF, Data_Contrato, Cargo) VALUE (%s, %s, curdate(),%s)"
                self.cursor.execute(sql, args)
                self.mydb.commit()
        elif result == None and len(args[1]) == 11 and len(args) == 4:
            if args[3] == 'CHEF' or args[3] == 'RECEPCAO' or args[3] == 'ADMINISTRACAO':
                sql = "INSERT INTO Funcionarios  (Nome, CPF, Data_Contrato, Cargo) VALUE (%s, %s, %s, %s)"
                self.cursor.execute(sql, args)
                self.mydb.commit()

    def Get_Funcionarios(self):
        sql = "SELECT Nome, Cargo FROM Funcionarios"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def Get_Funcionario_Data(self, *args):
        # Padrao de dados: Nome ou CPF
        if re.findall("\d", args[0]) == []:
            sql = "SELECT CPF FROM Funcionarios WHERE Nome = %s"
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            return result[0]
        else:
            sql = "SELECT Nome FROM Funcionarios WHERE CPF = %s"
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            return result[0]
    
    def Del_Funcionario(self, *args):
        # Padrao de dados: Nome ou CPF
        if re.findall("\d", args[0]) == []:
            sql = "SELECT Nome FROM Funcionarios WHERE Nome = %s"
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            if result != None:
                sql = "DELETE FROM Funcionarios WHERE Nome = %s"
                self.cursor.execute(sql, args)
                self.mydb.commit()
        else:
            sql = "SELECT CPF FROM Funcionarios WHERE CPF = %s"
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            if result != None:
                sql = "DELETE FROM Funcionarios WHERE CPF = %s"
                self.cursor.execute(sql, args)
                self.mydb.commit()

    def Add_Telefone_Func(self, *args):
        # Padrao de dados: Nome do funcionario ou CPF, Telefone
        if re.findall("\d", args[0]) == []: # Nome
            sql = "SELECT CPF FROM Funcionarios WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT Telefone FROM Telefone_Func WHERE Telefone = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result == None:
                    sql = "INSERT INTO Telefone_Func " "(CPF_Func, Telefone) " "VALUE (%s, %s)"
                    val = (self.Get_Funcionario_Data(args[0]), args[1])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        else: # CPF
            sql = "SELECT Telefone FROM Telefone_Func WHERE Telefone = %s"
            val = (args[1], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result == None:
                sql = "INSERT INTO Telefone_Func " "(CPF_Func, Telefone) " "VALUE (%s, %s)"
                val = (args[0], args[1])
                self.cursor.execute(sql, val)
                self.mydb.commit()

    def Add_Email_Func(self, *args):
        # Padrao de dados: Nome do funcionario ou CPF, Email
        if re.findall("\d", args[0]) == []: # Nome
            sql = "SELECT CPF FROM Funcionarios WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT Email FROM Email_Func WHERE Email = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result == None:
                    sql = "INSERT INTO Email_Func " "(CPF_Func, Email) " "VALUE (%s, %s)"
                    val = (self.Get_Funcionario_Data(args[0]), args[1])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        else: # CPF
            sql = "SELECT Email FROM Email_Func WHERE Email = %s"
            val = (args[1], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result == None:
                sql = "INSERT INTO Email_Func " "(CPF_Func, Email) " "VALUE (%s, %s)"
                val = (args[0], args[1])
                self.cursor.execute(sql, val)
                self.mydb.commit()
    
    def Add_Supervisor(self, *args):
        # Padrao de dados: Nome do funcionario ou CPF, Nome do supervisor ou CPF
        if re.findall("\d", args[0]) == [] and re.findall("\d", args[1]) == []: # Case Nome - Nome
            sql = "SELECT CPF FROM Funcionarios WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT CPF FROM Funcionarios WHERE Nome = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Funcionarios SET ID_Sup  = %s WHERE CPF = %s"
                    val = (self.Get_Funcionario_Data(args[1]), self.Get_Funcionario_Data(args[0]))
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        
        elif re.findall("\d", args[0]) == [] and re.findall("\d", args[1]) != []: # Case Nome - CPF
            sql = "SELECT CPF FROM Funcionarios WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "UPDATE Funcionarios SET ID_Sup  = %s WHERE CPF = %s"
                val = (args[1], self.Get_Funcionario_Data(args[0]))
                self.cursor.execute(sql, val)
                self.mydb.commit()
        
        elif re.findall("\d", args[0]) != [] and re.findall("\d", args[1]) == []: # Case CPF - Nome
            sql = "SELECT CPF FROM Funcionarios WHERE Nome = %s"
            val = (args[1], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "UPDATE Funcionarios SET ID_Sup  = %s WHERE CPF = %s"
                val = (self.Get_Funcionario_Data(args[1]), args[0])
                self.cursor.execute(sql, val)
                self.mydb.commit()

        else: ## Case CPF - CPF
            sql = "UPDATE Funcionarios SET ID_Sup  = %s WHERE CPF = %s"
            val = (args[1], args[0])
            self.cursor.execute(sql, val)
            self.mydb.commit()


    #   FIM FUNCIONARIOS

    def Add_Utensilio(self, *args):
        # Padrao de dados: Nome do utensilio, Preco, ID do Fornecedor
        sql = "SELECT Nome FROM Utensilios WHERE Nome = %s"
        val = (args[0], )
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result == None:
            sql = "SELECT ID FROM Fornecedores WHERE ID = %s"
            val = (args[2], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "INSERT INTO Utensilios " "(Nome, Valor_Compra, ID_Forn) " "VALUE (%s, %s, %s)"
                val = (args[0], args[1], args[2])
                self.cursor.execute(sql, val)
                self.mydb.commit()
    
    def Get_Utensilio(self):
        sql = "SELECT * FROM Utensilios"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
            
    def Del_Utensilio(self, *args):
        # Padrao de dados: Nome do utensilio ou ID
        if re.findall("\d", args[0]) == []: # Nome
            sql = "SELECT Nome FROM Utensilios WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "DELETE FROM Utensilios WHERE Nome = %s"
                val = (args[0], )
                self.cursor.execute(sql, val)
                self.mydb.commit()
        else: # ID
            sql = "SELECT ID FROM Utensilios WHERE ID = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "DELETE FROM Utensilios WHERE ID = %s"
                val = (args[0], )
                self.cursor.execute(sql, val)
                self.mydb.commit()
    
    def Get_Utensilio_Data(self, *args):
        # Padrao de dados: Nome do utensilio ou ID
        if re.findall("\d", args[0]) == []:
            sql = "SELECT ID FROM Utensilios WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                return result[0]
        else:
            sql = "SELECT Nome FROM Utensilios WHERE ID = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                return result[0]

#   FIM UTENSILIOS
    
    def Update_Fornecedor_Utensilio(self, *args):
        # Padrao de dados: Nome do ingrediente ou ID, ID do fornecedor ou Nome do fornecedor
        if re.findall("\d", args[0]) == [] and re.findall("\d", args[1]) == []: # Case Nome - Nome
            sql = "SELECT ID FROM Utensilios WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT ID FROM Fornecedores WHERE Nome = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Utensilios SET ID_Forn = %s WHERE Nome = %s"
                    val = (self.Get_Fornecedor_Data(args[1]), args[0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        
        elif re.findall("\d", args[0]) == [] and re.findall("\d", args[1]) != []: # Case Nome - ID
            sql = "SELECT ID FROM Utensilios WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT ID FROM Fornecedores WHERE ID = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Utensilios SET ID_Forn = %s WHERE Nome = %s"
                    val = (args[1], args[0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        
        elif re.findall("\d", args[0]) != [] and re.findall("\d", args[1]) == []: # Case ID - Nome
            sql = "SELECT ID FROM Utensilios WHERE ID = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT ID FROM Fornecedores WHERE Nome = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Utensilios SET ID_Forn = %s WHERE ID = %s"
                    val = (self.Get_Fornecedor_Data(args[1]), args[0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        
        else: # Case ID - ID
            sql = "SELECT ID FROM Utensilios WHERE ID = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT ID FROM Fornecedores WHERE ID = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Utensilios SET ID_Forn = %s WHERE ID = %s"
                    val = (args[1], args[0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()

    def Update_Fornecedor_Bebidas(self, *args):
        # Padrao de dados: Nome do ingrediente ou ID, ID do fornecedor ou Nome do fornecedor
        if re.findall("\d", args[0]) == [] and re.findall("\d", args[1]) == []: # Case Nome - Nome
            sql = "SELECT ID FROM Bebidas WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT ID FROM Fornecedores WHERE Nome = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Bebidas SET ID_Forn = %s WHERE Nome = %s"
                    val = (self.Get_Fornecedor_Data(args[1]), args[0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        
        elif re.findall("\d", args[0]) == [] and re.findall("\d", args[1]) != []: # Case Nome - ID
            sql = "SELECT ID FROM Bebidas WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT ID FROM Fornecedores WHERE ID = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Bebidas SET ID_Forn = %s WHERE Nome = %s"
                    val = (args[1], args[0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        
        elif re.findall("\d", args[0]) != [] and re.findall("\d", args[1]) == []: # Case ID - Nome
            sql = "SELECT ID FROM Bebidas WHERE ID = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT ID FROM Fornecedores WHERE Nome = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Bebidas SET ID_Forn = %s WHERE ID = %s"
                    val = (self.Get_Fornecedor_Data(args[1]), args[0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        
        else: # Case ID - ID
            sql = "SELECT ID FROM Bebidas WHERE ID = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT ID FROM Fornecedores WHERE ID = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Bebidas SET ID_Forn = %s WHERE ID = %s"
                    val = (args[1], args[0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()

    def Update_Fornecedor_Ingredientes(self, *args):
        # Padrao de dados: Nome do ingrediente ou ID, ID do fornecedor ou Nome do fornecedor
        if re.findall("\d", args[0]) == [] and re.findall("\d", args[1]) == []: # Case Nome - Nome
            sql = "SELECT ID FROM Ingredientes WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT ID FROM Fornecedores WHERE ID = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Ingredientes SET ID_Forn = %s WHERE Nome = %s"
                    val = (self.Get_Fornecedor_Data(args[1]), args[0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        
        elif re.findall("\d", args[0]) == [] and re.findall("\d", args[1]) != []: # Case Nome - ID
            sql = "SELECT ID FROM Ingredientes WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT ID FROM Fornecedores WHERE ID = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Ingredientes SET ID_Forn = %s WHERE Nome = %s"
                    val = (args[1], args[0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        
        elif re.findall("\d", args[0]) != [] and re.findall("\d", args[1]) == []: # Case ID - Nome
            sql = "SELECT ID FROM Ingredientes WHERE ID = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT ID FROM Fornecedores WHERE ID = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Ingredientes SET ID_Forn = %s WHERE ID = %s"
                    val = (self.Get_Fornecedor_Data(args[1]), args[0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        
        else: # Case ID - ID
            sql = "SELECT ID FROM Ingredientes WHERE ID = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            result = self.cursor.fetchone()
            if result != None:
                sql = "SELECT ID FROM Fornecedores WHERE ID = %s"
                val = (args[1], )
                self.cursor.execute(sql, val)
                result = self.cursor.fetchone()
                if result != None:
                    sql = "UPDATE Ingredientes SET ID_Forn = %s WHERE ID = %s"
                    val = (args[1], args[0])
                    self.cursor.execute(sql, val)
                    self.mydb.commit()


    def Get_Ingredientes(self):
        sql = "SELECT * FROM Ingredientes"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    
    def Add_Ingrediente(self, *args):
        # Padrao de dados: (Nome, Validade, Valor de Compra, Modo de Armazenamento(Seco ou Frio), ID_Forn ou Nome do Fornecedor) 
        if re.findall("\d", args[4]) == []:
            aux = self.Get_Fornecedor_Data(args[4])
            if aux != None:
                if args[3] == 1:
                    sql = "INSERT INTO Ingredientes (Nome, Validade, Valor_Compra, Armazenamento, ID_Forn) VALUES (%s, %s, %s, %s, %s)"
                    val = (args[0], args[1], args[2], 'Seco', aux)
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
                elif args[3] == 2:
                    sql = "INSERT INTO Ingredientes (Nome, Validade, Valor_Compra, Armazenamento, ID_Forn) VALUES (%s, %s, %s, %s, %s)"
                    val = (args[0], args[1], args[2], 'Frio', aux)
                    self.cursor.execute(sql, val)
                    self.mydb.commit()
        else:
            if args[3] == 1:
                sql = "INSERT INTO Ingredientes (Nome, Validade, Valor_Compra, Armazenamento, ID_Forn) VALUES (%s, %s, %s, %s, %s)"
                val = (args[0], args[1], args[2], 'Seco', args[4])
                self.cursor.execute(sql, val)
                self.mydb.commit()
            
            elif args[3] == 2:
                sql = "INSERT INTO Ingredientes (Nome, Validade, Valor_Compra, Armazenamento, ID_Forn) VALUES (%s, %s, %s, %s, %s)"
                val = (args[0], args[1], args[2], 'Frio', args[4])
                self.cursor.execute(sql, val)
                self.mydb.commit()
    
    def Del_Ingrediente(self, *args):
        # Padrao de dados: Nome do Ingrediente
        sql = "SELECT ID FROM Ingredientes WHERE Nome = %s"
        val = (args[0], )
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result != None:
            sql = "DELETE FROM Ingredientes WHERE Nome = %s"
            val = (args[0], )
            self.cursor.execute(sql, val)
            self.mydb.commit()
