# import logica_negocio_recepcao
import logica_negocio_gerencia

def main():
    # adm = test.Fornecedor("root", "160301@")
    # adm.Del_Fornecedor("Teste")
    # adm.Add_Fornecedor("Teste")
    # adm.Add_Telefone_Fornecedor("Teste", "999")
    # adm.Add_Email_Fornecedor("Teste", "emailteste@teste.com")

    # caixa = logica_negocio_recepcao.Recepcao("root", "160301@")
    # caixa.Add_Cliente("Teste", "123") #Nao funciona, resultado correto
    # caixa.Add_Cliente("TesteA")
    # caixa.Add_Cliente("Teste2") #Nao funciona, resultado correto
    # caixa.Del_Cliente("TesteA")
    # caixa.Del_Cliente("123")
    # caixa.Aloca_Mesa(12,4)
    # caixa.Faz_Pedido(10.00, '67952834100', 12, [[1,2,3],[1,2,3]])
    # caixa.Limpa_Pedidos_Cliente('Brenda Barbosa Pinto')
    # caixa.Add_Cliente("Roberto Magalhães", "67952834100")
    # caixa.Cardapio()

    adm = logica_negocio_gerencia.Gerencia("root", "root")
    adm.Add_Fornecedor("Teste")
    adm.Add_Telefone_Fornecedor("Teste", "999")
    adm.Add_Email_Fornecedor("Teste", "teste@testado.com")
    adm.Del_Fornecedor("Teste")
    adm.Add_Funcionario("TesteAbc", "22345678910", "Gerente")
    adm.Add_Telefone_Func("TesteAbc", "999")
    adm.Add_Telefone_Func("22345678910", "999")
    adm.Add_Email_Func("TesteAbc", "teste@testado.com.br")
    adm.Add_Email_Func("22345678910", "outroemail@teste.com")

    adm.Add_Funcionario("Outro", "33345678910", "Gerente")
    adm.Add_Funcionario("a", "44345678910", "Gerente")
    adm.Add_Funcionario("b", "55345678910", "Gerente")
    adm.Add_Funcionario("CC", "67345678910", "Gerente")
    adm.Add_Supervisor("Outro", "TesteAbc")
    adm.Add_Supervisor("44345678910", "TesteAbc")
    adm.Add_Supervisor("55345678910", "22345678910")
    adm.Add_Supervisor("CC", "22345678910")

    # adm.del_Funcionario("c")
    # adm.Del_Funcionario("a")
    # adm.Del_Funcionario("b")
    # adm.Del_Funcionario("CC")
    # adm.Del_Funcionario("TesteAbc")
    # adm.Del_Funcionario("22345678910")

    adm.Add_Utensilio("Batata", 10.00, 4)
    adm.Add_Utensilio("Batata", 10.00, 4)
    adm.Add_Utensilio("Cenoura", 10.00, 4)
    adm.Del_Utensilio("Batata")
    adm.Del_Utensilio("9")
    adm.Del_Utensilio("Cenoura")

    # adm.Del_Fornecedor("Cola Coca")
    # adm.Del_Fornecedor("Estoque/Sem Fornecedor")
    # adm.Add_Fornecedor("Cola Coca")
    # adm.Update_Fornecedor_Bebidas("Refrigerante Cola-Coca 350ML", "Cola Coca")
    adm.Update_Fornecedor_Bebidas("agua", "Cola Coca")
    adm.Update_Fornecedor_Bebidas("agua", "7")
    adm.Update_Fornecedor_Bebidas("9", "Estoque/Sem Fornecedor")
    adm.Update_Fornecedor_Bebidas("9", "3")
if __name__ == "__main__":
    main()