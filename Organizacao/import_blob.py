import os
import mysql.connector

path  = (r'Manual_Preparo')
user= input(f'Insira o usuário do banco de dados: ')
passwd= input(f'Insira a senha do banco de dados: ')

def txt2bin(arquivo):
    # Converte arquivo txt para formato binario
    with open(arquivo, 'rb') as a:
        binaryData = a.read()
    return binaryData


def insereBLOB(arquivo):
    print("Colocando BLOB na tabela Modo_Preparo")
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = user,
            passwd = passwd,
            auth_plugin = 'mysql_native_password',
            database = "Restaurante_BD")

        cursor = mydb.cursor()
        sql_insertBLOB = ("INSERT INTO Modo_Preparo " "(Manual) " "VALUE (%s)")

        file = txt2bin(arquivo)

        # Transforma arquivo em tupla
        tupla = (file,)
        result = cursor.execute(sql_insertBLOB, tupla)
        mydb.commit()
        print(f'Arquivo {arquivo} inserido na tabela Modo_Preparo como um BLOB')

    except mysql.connector.Error as error:
        print("Falha na inserção de arquivo BLOB na tabela{}".format(error))

    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("Conexão MySQL terminada")

# Percorre todos os arquivos .txt do diretorio e insere como BLOB no banco
# Apos isso, o arquivo .txt é movido para a pasta Inserido
for arquivo in os.listdir(path):
    if arquivo.endswith('.txt'):
            caminho_arquivo = rf'{path}/{arquivo}'
            insereBLOB(caminho_arquivo)
            # if not os.path.exists(r'Inserido'):
            #     os.makedirs(r'Inserido')
            # os.rename(caminho_arquivo,rf'Inserido/{arquivo}' )
            