from logica_negocio_cozinha import Cozinha
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



sair = False
cozinha = Cozinha('gabriel','357159258456')
menu = 0
submenu = 0
while sair == False:
    clear()
    submenu = 0
    print(''' Menu de opções - Recepção:
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
            cozinha.Read_Pedidos()
        input('\nPressione qualquer tecla para retornar...')
        clear()
    elif menu == 2:
        print("""Você gostaria de ver os ingredientes necessarios?
                      (S/N)""")
        res2 = input()
        if res2 == "S":
            cozinha.Read_Ingredientes()
        input('\nPressione qualquer tecla para retornar...')
        clear()
    elif menu == 3:
        clear()
        print(''' Menu de opções - Receitas:
        1 - Você gostaria de ver as receitas?
        2 - Você gostaria de editar uma receita?
        3 - Você gostaria de deletar uma receita?
        4 - Sair''')
        submenu = int(input())
        if submenu == 1:
            cozinha.Read_Receitas()
            input('\nPressione qualquer tecla para retornar...')
            clear()
        elif submenu == 2:
            cozinha.Update_Receitas()
            input('\nPressione qualquer tecla para retornar...')
            clear()
        elif submenu == 3:
            cozinha.Delete_Receitas()
            input('\nPressione qualquer tecla para retornar...')
            clear()
        elif submenu == 4:
            input('\nPressione qualquer tecla para retornar...')
            clear()
    elif menu == 4:
        clear()
        sair = True