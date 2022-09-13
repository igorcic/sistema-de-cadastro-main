from logica_negocio_gerencia import Gerencia
from time import sleep
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def interface_gerencia():
    sair = False
    gerencia = Gerencia('root','160301@')
    opcao = 0

    while sair == False:
        print(''' Menu de opções - Gerencia:
        1 - Funcionários
        2 - Fornecedores
        3 - Ingredientes
        4 - Utensilios
        5 - Sair''')

        opcao = int(input('Digite a opção desejada: '))
        clear()

        if opcao == 1:
            print(''' Espaço Atual -  Funcionários:
            1 - Ver funcionários
            2 - Adicionar funcionário
            3 - Remover funcionário
            4 - Adicionar Contatos
            5 - Voltar''')

            menu = int(input('Digite a opção desejada: '))
            clear()

            if menu == 1:
                print('Espaço Atual - Ver funcionários')
                aux = gerencia.Get_Funcionarios()
                print('Funcionários: \n')
                for i in range(len(aux)):
                    print(f'Nome: {aux[i][0]} - Cargo: {aux[i][1]}')
                input('\nPressione qualquer tecla para retornar...')
                clear()

            elif menu == 2:
                print('Espaço Atual - Adicionar funcionário')
                val = input('Insira o nome do funcionário: ')
                val2 = input('Insira o CPF do funcionário: ')
                val3 = input('Insira o cargo do funcionário: ')
                menu = int(input('''Deseja adicionar uma data de contrato do funcionário? 
                1 - Sim
                2 - Nao\n'''))
                try:

                    if len(val2) < 11:
                        raise ValueError

                    elif val3 != 'CHEF' and val3 != 'RECEPCAO' and val3 != 'ADMINISTRACAO':
                        raise ValueError

                    if menu == 1:
                        val4 = input('Insira a data de contrato do funcionário: ')
                        gerencia.Add_Funcionario(val, val2, val4, val3)

                    else:
                        gerencia.Add_Funcionario(val, val2, val3)

                    print('Funcionário adicionado com sucesso!')
                except:
                    print('Erro nos dados inseridos!')
                sleep(3)
                clear()

            elif menu == 3:
                print('Espaço Atual - Remover funcionário')
                val = input('Insira o nome ou CPF do funcionário: ')
                gerencia.Del_Funcionario(val)
                print('Funcionário removido com sucesso!')
                sleep(3)
                clear()
            
            elif menu == 4:
                print('Espaço Atual - Adicionar Contatos')
                val = input('Insira o nome ou CPF do funcionário: ')
                aux = int(input('''
                Deseja adicionar Email ou Telefone?
                1 - Email
                2 - Telefone\n'''))
                if aux == 1:
                        adiciona = True
                        while adiciona == True:
                            try:
                                val2 = input('Insira o email do funcionário: ')
                                gerencia.Add_Email_Func(val, val2)
                                aux = int(input('''
                                Deseja adicionar outro email?
                                1 - Sim
                                2 - Nao\n'''))
                                if aux == 2:
                                    adiciona = False
                            except:
                                print('Erro nos dados inseridos!')
                                sleep(3)
                                clear()
                else:
                    adiciona = True
                    while adiciona == True:
                        try:
                            val2 = input('Insira o telefone do funcionário: ')
                            gerencia.Add_Telefone_Func(val, val2)
                            aux = int(input('''Deseja adicionar outro telefone?\n
                            1 - Sim
                            2 - Nao\n'''))
                            if aux == 2:
                                adiciona = False
                        except:
                            print('Erro nos dados inseridos!')
                            sleep(3)
                            clear()
                print('Contato adicionado com sucesso!')
                sleep(3)
                clear()

            elif menu == 5:
                clear()
    
        elif opcao == 2:
            print(''' Espaço Atual -  Fornecedores:
            1 - Ver fornecedores
            2 - Adicionar fornecedor
            3 - Remover fornecedor
            4 - Adicionar Contatos
            5 - Voltar''')

            menu = int(input('Digite a opção desejada: '))
            clear()

            if menu == 1:
                print('Espaço Atual - Ver fornecedores')
                aux = gerencia.Get_Fornecedor()
                print('Fornecedores: \n')
                for i in range(len(aux)):
                    print(f'ID - {aux[i][0]} -  Nome: {aux[i][1]}')
                input('\nPressione qualquer tecla para retornar...')
                clear()

            elif menu == 2:
                print('Espaço Atual - Adicionar fornecedor')
                val = input('Insira o nome do fornecedor: ')
                try:
                    gerencia.Add_Fornecedor(val)
                    print('Fornecedor adicionado com sucesso!')
                except:
                    print('Erro nos dados inseridos!')
                sleep(3)
                clear()

            elif menu == 3:
                print('Espaço Atual - Remover fornecedor')
                val = input('Insira o nome ou ID do fornecedor: ')
                gerencia.Del_Fornecedor(val)
                print('Fornecedor removido com sucesso!')
                sleep(3)
                clear()
            
            elif menu == 4:
                print('Espaço Atual - Adicionar Contatos')
                val = input('Insira o Nome do Fornecedor: ')
                aux = int(input('''Deseja adicionar Email ou Telefone?
                1 - Email
                2 - Telefone\n'''))
                clear()
                if aux == 1:
                        adiciona = True
                        while adiciona == True:
                            try:
                                val2 = input('Insira o email do fornecedor: ')
                                gerencia.Add_Email_Fornecedor(val, val2)
                                aux = int(input('''Deseja adicionar outro email?
                                1 - Sim
                                2 - Nao\n'''))
                                if aux == 2:
                                    adiciona = False
                            except:
                                print('Erro nos dados inseridos!')
                                sleep(3)
                                clear()
                else:
                    adiciona = True
                    while adiciona == True:
                        try:
                            val2 = input('Insira o telefone do funcionário: ')
                            gerencia.Add_Telefone_Fornecedor(val, val2)
                            aux = int(input('''Deseja adicionar outro telefone?\n
                            1 - Sim
                            2 - Nao\n'''))
                            if aux == 2:
                                adiciona = False
                        except:
                            print('Erro nos dados inseridos!')
                            sleep(3)
                            clear()
                print('Contato adicionado com sucesso!')
                sleep(3)
                clear()

            elif menu == 5:
                clear()
    
        elif opcao == 3:
            print(''' Espaço Atual -  Ingredientes:
            1 - Ver Ingredientes
            2 - Adicionar Ingredientes
            3 - Remover Ingredientes
            4 - Voltar''')

            menu = int(input('Digite a opção desejada: '))
            clear()

            if menu == 1:
                print('Espaço Atual - Ver Ingredientes')
                aux = gerencia.Get_Ingredientes()
                print('Produtos: \n')
                for i in range(len(aux)):
                    print(f'ID - {aux[i][0]} -  Nome: {aux[i][1]}, Validade: {aux[i][2]}, Armazenamento: {aux[i][3]}, Preco de Compra: {aux[i][4]}, Tipo: {aux[i][5]}, ID do Fornecedor: {aux[i][6]}')
                input('\nPressione qualquer tecla para retornar...')
                clear()

            elif menu == 2:
                print('Espaço Atual - Adicionar Ingrediente')
                val = input('Insira o nome do ingrediente: ')
                val2 = str(input('Insira a validade do ingrediente: '))
                val3 = int(input('Insira a forma de armazenamento do ingrediente: 1 - Seco, 2 - Frio '))
                val4 = input('Insira o preco de compra do ingrediente: ')
                val5 = input('Insira o ID ou Nome do fornecedor: ')
                try:
                    gerencia.Add_Ingrediente(val, val2, val4, val3, val5)
                    print('Produto adicionado com sucesso!')
                except:
                    print('Erro nos dados inseridos!')  
                sleep(3)
                clear()

            elif menu == 3:
                print('Espaço Atual - Remover Ingrediente')
                val = input('Insira o nome do ingrediente: ')
                gerencia.Del_Ingrediente(val)
                print('Produto removido com sucesso!')
                sleep(3)
                clear()
            
            elif menu == 4:
                clear()

        elif opcao == 4:
            print(''' Espaço Atual -  Utensilios:
            1 - Ver Utensilios
            2 - Adicionar Utensilios
            3 - Remover Utensilios
            4 - Voltar''')

            menu = int(input('Digite a opção desejada: '))
            clear()

            if menu == 1:
                print('Espaço Atual - Ver Utensilios')
                aux = gerencia.Get_Utensilio()
                print('Produtos: \n')
                for i in range(len(aux)):
                    print(f'ID - {aux[i][0]} -  Nome: {aux[i][1]}, Preco de Compra: {aux[i][2]}, ID do Fornecedor: {aux[i][3]}')
                input('\nPressione qualquer tecla para retornar...')
                clear()

            elif menu == 2:
                print('Espaço Atual - Adicionar Utensilio')
                val = input('Insira o nome do Utensilio: ')
                val2 = input('Insira o preco de compra do ingrediente: ')
                val3 = input('Insira o ID ou Nome do fornecedor: ')
                try:
                    gerencia.Add_Utensilio(val, val2, val3)
                    print('Produto adicionado com sucesso!')
                except:
                    print('Erro nos dados inseridos!')  
                sleep(3)
                clear()

            elif menu == 3:
                print('Espaço Atual - Remover Utensilio')
                val = input('Insira o nome do utensilio: ')
                gerencia.Del_Utensilio(val)
                print('Produto removido com sucesso!')
                sleep(3)
                clear()
            
            elif menu == 4:
                clear()

        elif opcao == 5:
            gerencia.__del__()
            sair = True
        
        else:
            print('Opção inválida!')
