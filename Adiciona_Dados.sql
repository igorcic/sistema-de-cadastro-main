USE Restaurante_BD;

INSERT INTO Fornecedores(Nome)
VALUES
	('Cola Coca'),
    ('VEBAM'),
    ('Paonificadora do Art'),
    ('FreeVaca'),
    ('Distribuidora Hortifruti'),
    ('Linha Quente'),
    ('Atacarejo Sorvete'),
    ('Minas Queijo')
;

INSERT INTO Email_Fornecedores()
VALUES
	(1, 'fornece@coca.ina'),
    (2, 'bebidas@vebam.drink'),
    (3, 'paoquentinho@bom.dms'),
    (4, 'sempapelao@freevaca.br'),
    (5, 'natural@daterra.com'),
    (6, 'aquecimentoglobal@eletro.br'),
    (7, 'acabou@osproduto.caro')
;

INSERT INTO Telefone_Fornecedores()
VALUES
	(1, '0800-123-4567'),
    (2, '0800-456-7890'),
    (3, '0800-789-0123'),
    (4, '0800-000-4444'),
    (5, '10 3104-9898'),
    (6, '0800-481-3975'),
    (7, '80 4002-8922')
;

INSERT INTO Bebidas(Nome, Validade, Valor_Venda, Valor_Compra, Tipo, ID_Forn)
VALUES
	('Refrigerante de Limao 350ML', '2022-09-23', 4.50, 4.00, 'Nao_Alcoolica', 2),
    ('Chá Gelado de Pêssego 350ML', '2023-06-28', 4.00, 3.10, 'Nao_Alcoolica', 2),
    ('Cerveja Carona 355ML', '2023-07-05', 6.50, 4.88, 'Alcoolica', 2),
    ('Energético Alien 355ML', '2024-01-02', 6.00, 3.79, 'Nao_Alcoolica', 1),
    ('Refrigerante Cola-Coca 350ML', '2023-01-18', 5.00, 4.80, 'Nao_Alcoolica', 1),
    ('Bebida Láctea Sabor Chocolate com Menta 250ML', '2023-05-17', 3.75, 1.25, 'Nao_Alcoolica', 1),
	('Água da Pedra 600ML', '2024-01-02', 3.50, 2.10, 'Nao_Alcoolica', 1)
;

INSERT INTO Mesa(ID, Qtd_Lugares)
VALUES
	(1, 4),
	(2, 2),
	(3, 4),
	(4, 12),
	(5, 4),
	(6, 4),
	(7, 8),
	(8, 8),
	(9, 4),
	(10, 4),
	(11, 2),
	(12, 8),
	(13, 8),
	(14, 12),
	(15, 2),
	(16, 2),
	(17, 8),
	(18, 4),
	(19, 12),
	(20, 8)
;

INSERT INTO Ingredientes(Nome, Validade, Armazenamento, Valor_Compra, Tipo, ID_Forn)
VALUES
	('Alface 18 Pés', '2022-09-08', 'Frio', 15.00, 'Vegetal', 5),
    ('Tomate 20KG', '2022-09-28', 'Seco', 45.00, 'Vegetal', 5),
    ('Picles 440G', '2023-02-13', 'Seco', 11.75, 'Vegetal', 5),
    ('Pão Italiano 1KG', '2022-10-18', 'Seco', 29.90, 'Pao', 3),
    ('Pão com Gergelim 1KG', '2022-10-23', 'Seco', 17.65, 'Pao', 3),
    ('Filé de Peito de Frango 1KG', '2023-05-20', 'Frio', 22.80, 'Carne', 4),
    ('Hamburguer de Picanha 90G', '2023-01-10', 'Frio', 1.76, 'Carne', 4),
    ('Carne Moida sem Gordura 1KG', '2023-01-10', 'Frio', 34.99, 'Carne', 4),
    ('Bacon 1KG', '2023-01-12', 'Frio', 39.80, 'Carne', 4),
    ('Cebola 1KG', '2022-09-08', 'Seco', 4.80, 'Vegetal', 5),
    ('Farinha de Rosca 1KG', '2022-09-28', 'Seco', 9.50, 'Extra', 6),
    ('Farinha de Trigo 5KG', '2022-09-28', 'Seco', 19.89, 'Extra', 6),
    ('Ovo 30 Dúzias', '2022-10-15', 'Frio', 170.00, 'Extra', 7),
    ('Batata Frita Congelada 2KG', '2024-05-08', 'Frio', 24.90, 'Extra', 7),
    ('Queijo Cheddar 2.3KG', '2023-03-12', 'Frio', 493.12, 'Queijo', 8)
;
# Checa Disponibilidade se o produto estiver na validade
# TODO - Criar método de excluir a entrada se a validade < curdate()
-- SELECT * FROM Ingredientes WHERE Validade >= curdate();

INSERT INTO Funcionarios(CPF, Nome, Data_Contrato, Cargo)
VALUES
	('6795283410', 'Roberto Magalhães' , '2016-02-09', 'ADM')
;

INSERT INTO Funcionarios()
VALUES
	('1064259387', 'Júlio Oliveira' , '2016-02-12', 'Cozinha', '6795283410'),
    ('8964250371', 'Marcia Pereira' , '2017-01-18', 'Atendimento', '6795283410'),
    ('5026891374', 'Gorete da Fofoca' , '2017-04-16', 'Limpeza', '6795283410'),
    ('2016579843', 'Juscelino do Dominó' , '2018-09-25', 'Cozinha', '1064259387'),
    ('6095324718', 'Michael Jordan' , '2019-08-30', 'TI', '6795283410'),
	('6854921073', 'Pedrinho do Baile' , '2021-09-12', 'Marketing', '6095324718'),
    ('4371206895', 'Daiane dos Santos' , '2018-10-05', 'Atendimento', '8964250371'),
    ('5861074329', 'Felipe Baiano' , '2018-07-21', 'Cozinha', '1064259387'),
    ('1678423059', 'Margarete Lima', '2018-05-15', 'Atendimento', '4371206895')
;

INSERT INTO Email_Func()
VALUES
	('6795283410', 'rmagal@gmail.com' ),
    ('1064259387', 'seujulio@gmail.com'),
    ('8964250371', 'mpereira@gmail.com'),
    ('5026891374', 'senhorado71@gmail.com'),
    ('2016579843', 'domingo@domino.br'),
    ('6854921073', 'mcpedrinnn_do_baile@gmail.com'),
    ('6095324718', 'oneal@nba.na'),
    ('4371206895', 'santos@ginasta.br'),
    ('5861074329', 'felipepchef@estelar.com'),
    ('1678423059', 'donalima@gmail.com')
;

INSERT INTO Telefone_Func()
VALUES
	('6795283410', '21 84536694' ),
    ('1064259387', '16 31244813'),
    ('8964250371', '65 80452254'),
    ('5026891374', '41 50138403'),
    ('2016579843', '34 42314149'),
    ('6854921073', '21 63115282'),
    ('6095324718', '91 53078504'),
    ('4371206895', '11 98765865'),
    ('5861074329', '67 89998212'),
    ('1678423059', '11 41336478')
;

INSERT INTO Clientes(Nome)
VALUES
	('Brenda Barbosa Pinto'),
    ('Rafaela Ribeiro Castro'),
    ('Tânia Castro Fernandes'),
    ('Isabela Cunha Correia'),
    ('Leonardo Gomes Silva')
;

INSERT INTO Clientes(Nome, CPF)
VALUES
	('Ryan Araujo Souza','2893746150')
;

INSERT INTO Utensilios(Nome, Valor_Compra, ID_Forn)
VALUES
	('Chapa Para Lanches', 8118.71, 6),
    ('Fritadeira Elétrica', 11522.38, 6),
    ('Forno Elétrico', 5874.85, 6),
    ('Conservador de Batatas Fritas', 2151.24, 6),
    ('Exaustor 30CM', 1286.99, 6),
    ('Cortador de Frios', 4054.00, 6)
;

INSERT INTO Ingredientes_Receita()
VALUES
	(14, 1),
    (4, 2),
    (8, 2),
    (2, 2),
    (10, 2),
    (1, 2),
    (15, 2),
    (5, 3),
    (6, 3),
    (15, 3),
    (2, 3),
    (1, 3),
    (10, 4),
    (11, 4),
    (13, 4),
    (12, 4),
    (5, 5),
    (7, 5),
    (10, 5),
    (9, 5),
    (13, 5),
    (15, 5),
    (1, 5),
    (2, 5)
;

INSERT INTO Utensilios_Receita()
VALUES
	(2, 1),
    (4, 1),
    (1, 2),
    (6, 2),
    (6, 3),
    (2, 4),
    (2, 5),
    (6, 5)
;

INSERT INTO Pratos(ID, Nome, Valor_Venda, ID_Preparo)
VALUES
	(1, 'Porção de Batata Frita', 17.00, 1),
    (2, 'Cheeseburguer', 19.50, 2),
    (3, 'X-Frango', 21.00, 3),
    (4, 'Porção de Anéis de Cebola', 15.00, 4),
    (5, 'X-Picanha', 23.50, 5)
;

INSERT INTO Pedidos(Data_Pedido, Total, ID_Func, ID_Mesa)
VALUES
	('2022-07-08', 47.50, '8964250371', 2),
    ('2022-07-31', 167.00, '6795283410', 4),
    ('2022-08-05', 144.00, '6795283410', 1),
    ('2022-08-18', 200.50, '4371206895', 8),
    ('2022-08-27', 3.50, '8964250371', 5)
;

INSERT INTO Pratos_Pedidos()
VALUES
	(2, 1),
    (4, 2),
    (3, 2),
    (1, 2),
    (5, 3),
    (3, 3),
    (1, 3),
    (1, 4),
    (4, 4),
    (5, 4),
    (2, 4)
;

INSERT INTO Bebidas_Pedidos()
VALUES
	(5, 7),
    (1, 2),
    (1, 4),
    (2, 1),
    (3, 1),
    (3, 7),
    (3, 2),
    (4, 5)
;

UPDATE Mesa SET ID_Cliente = 2 WHERE ID = 2;
UPDATE Mesa SET ID_Cliente = 1 WHERE ID = 4;
UPDATE Mesa SET ID_Cliente = 5 WHERE ID = 1;
UPDATE Mesa SET ID_Cliente = 3 WHERE ID = 8;
UPDATE Mesa SET ID_Cliente = 4 WHERE ID = 11;

SHOW WARNINGS;
SHOW ERRORS;