import logica_negocio_recepcao

def main():
    # adm = test.Fornecedor("root", "160301@")
    # adm.Del_Fornecedor("Teste")
    # adm.Add_Fornecedor("Teste")
    # adm.Add_Telefone_Fornecedor("Teste", "999")
    # adm.Add_Email_Fornecedor("Teste", "emailteste@teste.com")

    caixa = logica_negocio_recepcao.Recepcao("root", "160301@")
    # caixa.Add_Cliente("Teste", "123")
    # caixa.Add_Cliente("TesteA")
    # caixa.Add_Cliente("Teste2")
    # caixa.Del_Cliente("TesteA")
    # caixa.Del_Cliente("123")
    # caixa.Aloca_Mesa(12,4)
    caixa.Faz_Pedido(10.00, '6795283410', 12, [[1,2,3],[1,2,3]])

if __name__ == "__main__":
    main()