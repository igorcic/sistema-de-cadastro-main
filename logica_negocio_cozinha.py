import mysql.connector

class Cozinha:
    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd
        self.mydb = mysql.connector.connect(
            host="localhost",
            user=user,
            passwd=passwd,
            auth_plugin='mysql_native_password',
            database="Restaurante_BD")
        self.cursor = self.mydb.cursor()

    def __del__(self):
        if self.mydb.is_connected():
            self.mydb.close()

    def Read_Pedidos(self):
        sql = "SELECT pedidos.ID_Mesa, pratos.Nome FROM Pedidos, pratos, pratos_pedidos WHERE Pedidos.ID = Pratos_Pedidos.ID_Pedido and Pratos.ID = Pratos_Pedidos.ID_Prato;"
        self.cursor.execute(sql)
        linhas = self.cursor.fetchall()
        print(linhas)
        for i in range(len(linhas)):
            count = 0
            for j in range(len(linhas)):
                if i == linhas[j][0]:
                    if count == 1:
                        print("\nPedido" + " " + str(linhas[j][0]))
                    print(linhas[j][1])
                    count +=1


    def Read_Receitas(self):
        sql = "SELECT pratos.Nome, modo_preparo.Manual FROM modo_preparo, pratos WHERE modo_preparo.ID = pratos.ID_preparo;"
        self.cursor.execute(sql)
        linhas = self.cursor.fetchall()
        for i in range(len(linhas)):
            print((str(linhas[i][1]).replace(r'\n', '\n').replace(r"b'", "")).replace("\n'", "\n"))
            print("\n\n")

    def Read_Ingredientes(self):
        sql = "SELECT DISTINCT pedidos.ID_Mesa, pratos.Nome, Ingredientes.Nome FROM Pedidos, Pratos_Pedidos, Pratos, ingredientes_receita, ingredientes, modo_preparo WHERE Pedidos.ID = Pratos_Pedidos.ID_Pedido and Pratos.ID = Pratos_Pedidos.ID_Prato and Pratos.ID_Preparo = modo_preparo.ID and ingredientes_receita.ID_preparo = modo_preparo.ID ORDER BY Pedidos.ID_Mesa, pratos.Nome;"
        self.cursor.execute(sql)
        linhas = self.cursor.fetchall()
        print(linhas)
        passa=[]
        for i in range(len(linhas)):
            count = 0
            for j in range(len(linhas)):
                if linhas[i][1] == linhas[j][1] and linhas[i][0] == linhas[j][0]:
                    if linhas[j][1] not in passa:
                        if(count ==0):
                            print("\n\n" + str(linhas[j][1]) + ":\n")
                        print(linhas[j][2])
                        count+=1
            passa.append(linhas[i][1])

    def Create_Receitas(self):
        print("Adicione o Modo de preparado:")
        print("(Digite fim para finalizar a operação)")
        texto = ""
        linha = ""
        while linha != "fim":
            linha = input()
            if linha == "fim":
                break
            texto += linha + r"\n"

        print("Digite todos o ID dos ingredientes necessarios")
        ingredientes = input().split()
        print("Digite todos o ID dos utensilios necessarios")
        utensilios = input().split()
        print("Digite o nome da nova receita")
        nome = input()
        print("Digite o preço da nova receita")
        Valor_Venda = input()

        sql = "INSERT INTO Modo_Preparo (ID, Manual) VALUES (NULL, %s);"
        self.cursor.execute(sql, (texto, ))
        self.mydb.commit()

        sql = "SELECT last_insert_id() FROM Modo_Preparo"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.cursor = self.mydb.cursor(buffered=True)

        for i in range(len(ingredientes)):
            sql = "INSERT INTO Ingredientes_Receita (ID_Ingr, ID_Preparo) VALUES (%s, %s);"
            val = (ingredientes[i], result[0][0])
            self.cursor.execute(sql, val)
            self.mydb.commit()

        for i in range(len(utensilios)):
            sql = "INSERT INTO Utensilios_Receita (ID_Util, ID_Preparo) VALUES (%s, %s);"
            val = (utensilios[i], result[0][0])
            self.cursor.execute(sql, val)
            self.mydb.commit()

        sql = "INSERT INTO Pratos (ID, Nome, Valor_Venda, ID_Preparo) VALUES (NULL, %s, %s, %s);"
        val = (nome, Valor_Venda, result[0][0])
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def Update_Receitas(self):
        print("Qual é o id da receita?")
        ID = input()
        print("Você gostaria de editar o modo de preparo?")
        print("S/N")
        res1 = input()
        if res1 == "S":
            print("Digite a receita?")
            print("(Digite fim para finalizar a operação)")
            texto = ""
            linha = ""
            while linha != "fim":
                linha = input()
                if linha == "fim":
                    break
                texto += linha + r"\n"

            sql = "UPDATE Modo_Preparo SET Manual = %s Where ID = %s;"
            val = (texto, ID)
            self.cursor.execute(sql, val)
            self.mydb.commit()


    def Delete_Receitas(self):
        print("Qual é o id da receita?")
        ID = input()
        sql = "DELETE FROM Modo_Preparo WHERE ID = %s"
        val = (ID, )
        self.cursor.execute(sql, val)
        self.mydb.commit()

