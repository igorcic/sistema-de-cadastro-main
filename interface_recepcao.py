from time import sleep
from logica_negocio_recepcao import Recepcao
import os
import re

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def interface_recepcao():

    sair = False
    recepcao = Recepcao('root','160301@')
    opcao = 0

    while sair == False:
        print(''' Menu de opções - Recepção:
        1 - Mesas
        2 - Clientes
        3 - Cardápio
        4 - Pedidos
        5 - Sair''')

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
                val = int(input('Insira a quantidade de lugares desejada: '))
                val2 = input('Insira o Nome ou CPF do cliente: ')
                try:
                    if val2 > 12 or val2 < 0:
                        raise ValueError
                    else:
                        val2 = recepcao.Get_Cliente_ID(val2)
                        if val2 != None:
                            recepcao.Aloca_Mesa(val, val2)
                            print('Mesa alocada com sucesso!')
                except:
                    print('Erro nos dados inseridos!')
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
                    try:
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
                    except:
                        print('Cliente não encontrado.')

                else:
                    print('CPF do Cliente: ', val)
                    try:
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
                    except:
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
                print(f'ID - {i[0]}, Item: {i[1]} - R$ {i[2]}')

            input('\nPressione qualquer tecla para retornar...')
            clear()


        elif opcao == 4:
            print ('''Espaço Atual - Pedidos
            1 - Adicionar Pedido
            2 - Remover Pedido
            3 - Consultar Pedido
            4 - Sair''')
            menu = int(input('Digite a opção desejada: '))
            clear()

            if menu == 1:
                print('''Espaço Atual - Adicionar Pedido
                ''')
                val = input('Insira o CPF do Funcionário: ')
                val2 = input('Insira o Número da mesa: ')
                pratos, bebidas = [], []

                print('Insira os pratos desejados: ')
                while True:
                    print('Insira 0 para sair.')
                    aux = int(input('Insira o ID do prato: '))
                    pratos.append(aux)
                    if aux == 0:
                        break

                
                print('Insira as bebidas desejadas: ')
                while True:
                    print('Insira 0 para sair.')
                    aux = int(input('Insira o ID da bebida: '))
                    bebidas.append(aux)
                    if aux == 0:
                        break


                total = 0
                for i in pratos:
                    a = recepcao.Get_Valor_Prato(i)
                    if a!= None:
                        total += a[0]
                for i in bebidas:
                    a = recepcao.Get_Valor_Bebida(i)
                    if a!= None:
                        total += a[0]
                try:
                    if pratos[0] == 0 and bebidas[0] == 0:
                        print('Pedido não adicionado.')
                    else:
                        recepcao.Faz_Pedido(total, val, val2, pratos, bebidas)
                        print('Pedido adicionado com sucesso!')
                except:
                    print('Erro ao adicionar pedido.')
                sleep(3)
                clear()

            elif menu == 2:
                print('''Espaço Atual - Remover Pedido
                ''')
                val = input('Insira o Nome ou CPF do Cliente: ')
                try:
                    recepcao.Limpa_Pedidos_Cliente(val)
                    print('Pedido removido com sucesso!')
                except:
                    print('Cliente não encontrado.')
                sleep(3)
                clear()

            elif menu == 3:
                print('''Espaço Atual - Consultar Pedido
                ''')
                val = input('Insira o Número da mesa: ')

                aux = recepcao.Get_Pedidos(val)
                if len(aux) > 0:
                    print('Número do Pedido: ')
                    for i in range(len(aux)):
                        print(aux[i][0])
                        a = recepcao.Get_Pratos_Pedido(aux[i][0])
                        for item in a:
                            print(f'ID: {item[0]} - Prato: {item[1]}')
                        b = recepcao.Get_Bebidas_Pedido(aux[i][0])
                        for item in b:
                            print(f'ID: {item[0]} - Bebida: {item[1]}')
                else:
                    print('Mesa não possui pedidos.')
                
                input('\nPressione qualquer tecla para retornar...')
                clear()

            elif menu == 4:
                clear()

        elif opcao == 5:
            recepcao.__del__()
            sair = True
        
        else:
            print('Opção inválida!')