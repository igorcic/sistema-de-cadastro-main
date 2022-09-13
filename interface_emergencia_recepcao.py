from time import sleep
from logica_negocio_recepcao import Recepcao
import os
import re

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

sair = False
recepcao = Recepcao('root','160301@')
opcao = 0

while sair == False:
    print(''' Menu de opções - Recepção:
    1 - Mesas
    2 - Clientes
    3 - Cardápio
    4 - Sair''')

    opcao = int(input('Digite a opção desejada: '))
    clear()

    if opcao == 1:
        print(''' Espaço Atual -  Mesas:
        1 - Ver mesas disponíveis
        2 - Alocar mesa
        3 - Desalocar mesa
        4 - Voltar''')

        menu = int(input('Digite a opção desejada: '))
        clear()

        if menu == 1:
            print('Espaço Atual - Ver mesas disponíveis')
            aux = recepcao.Mesas_Livres()
            print('Mesas disponíveis: \n')
            for i in range(len(aux)):
                print(f'Mesa {aux[i][0]} - {aux[i][1]} Lugares')
            input('\nPressione qualquer tecla para retornar...')
            clear()

        elif menu == 2:
            print('Espaço Atual - Alocar mesa')
            val = input('Insira a quantidade de lugares desejada: ')
            val2 = input('Insira o Nome ou CPF do cliente: ')
            try:
                val2 = recepcao.Get_Cliente_ID(val2)
                if val2 != None:
                    print(val, val2,len(val2))
                    recepcao.Aloca_Mesa(val, val2)
                    print('Mesa alocada com sucesso!')
            except:
                print('Cliente não encontrado ou Mesa já alocada!')
            sleep(3)
            clear()

        elif menu == 3:
            print('Espaço Atual - Desalocar mesa')
            val = input('Insira o Número da mesa: ')
            recepcao.Limpa_Mesa(val)
            print('Mesa desalocada com sucesso!')
            sleep(3)
            clear()

        elif menu == 4:
            clear()

    elif opcao == 2:
        print(''' Espaço Atual -  Clientes:
        1 - Registrar Cliente
        2 - Consultar Cliente
        3 - Remover Cliente
        4 - Sair''')
        menu = int(input('Digite a opção desejada: '))
        clear()

        if menu == 1:
            print('''Espaço Atual - Registro Cliente
            ''')
            nome = input('Digite o nome do cliente: ')
            print('''Deseja Adicionar CPF?
            1 - Sim
            2 - Não''')
            menu = int(input('Digite a opção desejada: '))
            clear()

            if menu == 1:
                print(f'Nome do Cliente: {nome}')
                cpf = input('Digite o CPF do cliente: ')
                recepcao.Add_Cliente(nome, cpf)

            else:
                recepcao.Add_Cliente(nome)
                print('Cliente adicionado: ', nome) 
                sleep(3)
                clear()  
                
        elif menu == 2:
            print('''Espaço Atual - Consultar Cliente
            ''')
            val = str(input('Digite o Nome ou CPF do cliente: '))
            if re.findall("\d", val) == []:
                print('Nome do Cliente: ', val)
                aux = recepcao.Get_Cliente_ID(val)

                if aux != None:
                    a = recepcao.Get_Mesa(aux)

                    if a != None:
                        print('Mesa Alocada: ', a[0])
                        aux = recepcao.Get_Pedidos(a[0])

                        if aux != None:
                            print('Número do Pedido: ')
                            for i in aux:
                                print(i[0])
                
                    else:
                        print('Cliente não possui mesa alocada.')
                else:
                    print('Cliente não encontrado.')
                
                sleep(3)
                clear()
                
        elif menu == 3:
            print('''Espaço Atual - Remover Cliente
            ''')
            val = input('Digite o Nome ou CPF: ')
            try:
                aux = recepcao.Del_Cliente(val)
                print('''Cliente Removido com Sucesso.''')
            except:
                print('Cliente não encontrado.')
            sleep(3)
            clear()
        
        elif menu == 4:
            clear()
    
    elif opcao == 3:
        aux = recepcao.Cardapio()
        print('Espaço Atual - Cardápio\n')
        for i in aux:
            print(f'Item: {i[0]} - R$ {i[1]}')

        input('\nPressione qualquer tecla para retornar...')


    elif opcao == 4:
        recepcao.__del__()
        sair = True
    
    else:
        print('Opção inválida!')