from logica_negocio_cozinha import Cozinha
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def interface_cozinha():

    sair = False
    cozinha = Cozinha('gabriel','357159258456')
    menu = 0
    submenu = 0
    while sair == False:
        clear()
        submenu = 0
        print(''' Menu de opções - Cozinha:
        1 - Pedidos
        2 - Ingredientes
        3 - Receitas
        4 - Sair''')
        menu = int(input())
        if menu == 1:
            print("""Você gostaria de ver os pedidos?
                (S/N)""")
            res1 = input()
            if res1 == "S":
                linhas = cozinha.Read_Pedidos()
                for i in range(len(linhas)):
                    count = 0
                    for j in range(len(linhas)):
                        if i == linhas[j][0]:
                            if count == 1:
                                print("\nPedido" + " " + str(linhas[j][0]))
                            print(linhas[j][1])
                            count += 1
            input('\nPressione qualquer tecla para retornar...')
            clear()
        elif menu == 2:
            print("""Você gostaria de ver os ingredientes necessarios?
                        (S/N)""")
            res2 = input()
            if res2 == "S":
                linhas = cozinha.Read_Ingredientes()
                passa = []
                for i in range(len(linhas)):
                    count = 0
                    for j in range(len(linhas)):
                        if linhas[i][1] == linhas[j][1] and linhas[i][0] == linhas[j][0]:
                            if linhas[j][1] not in passa:
                                if (count == 0):
                                    print("\n\n" + str(linhas[j][1]) + ":\n")
                                print(linhas[j][2])
                                count += 1
                    passa.append(linhas[i][1])
            input('\nPressione qualquer tecla para retornar...')
            clear()
        elif menu == 3:
            clear()
            print(''' Menu de opções - Receitas:
        1 - Você gostaria de ver as receitas?
        2 - Você gostaria de editar uma receita?
        3 - Você gostaria de deletar uma receita?
        4 - Você gostaria de criar uma receita?
        5 - Sair''')
            submenu = int(input())

            if submenu == 1:
                linhas = cozinha.Read_Receitas()
                for i in range(len(linhas)):
                    print(((str(linhas[i][1]).replace(r'\n', '\n').replace(r"b'", "")).replace("\n'", "\n")).replace(
                        "'\n", "\n"))
                    print("\n\n")
                input('\nPressione qualquer tecla para retornar...')
                clear()

            elif submenu == 2:
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
                    cozinha.Update_Receitas(ID, texto)
                input('\nPressione qualquer tecla para retornar...')
                clear()

            elif submenu == 3:
                print("Qual é o id da receita?")
                ID = input()
                cozinha.Delete_Receitas(ID)
                input('\nPressione qualquer tecla para retornar...')
                clear()

            elif submenu == 4:
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
                cozinha.Create_Receitas(texto, ingredientes, utensilios, nome, Valor_Venda)
                input('\nPressione qualquer tecla para retornar...')

            elif submenu == 5:
                input('\nPressione qualquer tecla para retornar...')
                clear()

        elif menu == 4:
            clear()
            sair = True