import interface_recepcao

sair = False

while sair == False:
    print(''' 
    Menu de opções
    1 - Recepção
    2 - Cozinha
    3 - Gerencia
    4 - Sair
    ''')
    opcao = int(input('Digite o número da opção desejada: '))
    if opcao == 1:
        interface_recepcao.clear()
        interface_recepcao.interface_recepcao()
    
    # elif opcao == 2:

    # elif opcao == 3:

    elif opcao == 4:
        interface_recepcao.clear()
        sair = True

    else:
        interface_recepcao.clear()
        print('''
        Opção inválida.
        Por favor, tente novamente:
        ''')

