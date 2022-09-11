import logica_negocio_recepcao

def main():
    # adm = test.Fornecedor("root", "160301@")
    # adm.Del_Fornecedor("Teste")
    # adm.Add_Fornecedor("Teste")
    # adm.Add_Telefone_Fornecedor("Teste", "999")
    # adm.Add_Email_Fornecedor("Teste", "emailteste@teste.com")

    caixa = logica_negocio_recepcao.Recepcao("root", "160301@")
    # caixa.Add_Cliente("Teste", "123") #Nao funciona, resultado correto
    # caixa.Add_Cliente("TesteA")
    # caixa.Add_Cliente("Teste2") #Nao funciona, resultado correto
    # caixa.Del_Cliente("TesteA")
    # caixa.Del_Cliente("123")
    # caixa.Aloca_Mesa(12,4)
    # caixa.Faz_Pedido(10.00, '67952834100', 12, [[1,2,3],[1,2,3]])
    # caixa.Limpa_Pedidos_Cliente('Brenda Barbosa Pinto')
    # caixa.Add_Cliente("Roberto Magalhães", "67952834100")
    # caixa.Limpa_Pedidos_Geral()
    # caixa.Limpa_Mesas()

if __name__ == "__main__":
    main()