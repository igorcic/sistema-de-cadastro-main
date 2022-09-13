USE Restaurante_BD;

INSERT INTO Fornecedores(Nome)
VALUES
	('Estoque/Sem Fornecedor'),
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
	(2, 'fornece@coca.ina'),
    (3, 'bebidas@vebam.drink'),
    (4, 'paoquentinho@bom.dms'),
    (5, 'sempapelao@freevaca.br'),
    (6, 'natural@daterra.com'),
    (7, 'aquecimentoglobal@eletro.br'),
    (8, 'acabou@osproduto.caro')
;

INSERT INTO Telefone_Fornecedores()
VALUES
	(2, '0800-123-4567'),
    (3, '0800-456-7890'),
    (4, '0800-789-0123'),
    (5, '0800-000-4444'),
    (6, '10 3104-9898'),
    (7, '0800-481-3975'),
    (8, '80 4002-8922')
;

INSERT INTO Bebidas(Nome, Validade, Valor_Venda, Valor_Compra, Tipo, ID_Forn)
VALUES
	('Refrigerante de Limao', '2022-09-23', 4.50, 4.00, 'Nao_Alcoolica', 3),
    ('Cha Gelado de Pessego', '2023-06-28', 4.00, 3.10, 'Nao_Alcoolica', 3),
    ('Cerveja Carona', '2023-07-05', 6.50, 4.88, 'Alcoolica', 3),
    ('Energetico Alien', '2024-01-02', 6.00, 3.79, 'Nao_Alcoolica', 2),
    ('Refrigerante Cola-Coca', '2023-01-18', 5.00, 4.80, 'Nao_Alcoolica', 2),
    ('Bebida Lactea Sabor Chocolate com Menta', '2023-05-17', 3.75, 1.25, 'Nao_Alcoolica', 2),
	('Agua da Pedra', '2024-01-02', 3.50, 2.10, 'Nao_Alcoolica', 2)
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
	('Alface', '2022-09-08', 'Frio', 15.00, 'Vegetal', 5),
    ('Tomate', '2022-09-28', 'Seco', 45.00, 'Vegetal', 5),
    ('Picles', '2023-02-13', 'Seco', 11.75, 'Vegetal', 5),
    ('Pao Italiano', '2022-10-18', 'Seco', 29.90, 'Pao', 3),
    ('Pao com Gergelim', '2022-10-23', 'Seco', 17.65, 'Pao', 3),
    ('File de Peito de Frango', '2023-05-20', 'Frio', 22.80, 'Carne', 4),
    ('Hamburguer de Picanha', '2023-01-10', 'Frio', 1.76, 'Carne', 4),
    ('Carne Moida sem Gordura', '2023-01-10', 'Frio', 34.99, 'Carne', 4),
    ('Bacon', '2023-01-12', 'Frio', 39.80, 'Carne', 4),
    ('Cebola', '2022-09-08', 'Seco', 4.80, 'Vegetal', 5),
    ('Farinha de Rosca', '2022-09-28', 'Seco', 9.50, 'Extra', 6),
    ('Farinha de Trigo', '2022-09-28', 'Seco', 19.89, 'Extra', 6),
    ('Ovo', '2022-10-15', 'Frio', 170.00, 'Extra', 7),
    ('Batata Frita Congelada', '2024-05-08', 'Frio', 24.90, 'Extra', 7),
    ('Queijo Cheddar', '2023-03-12', 'Frio', 493.12, 'Queijo', 8)
;
# Checa Disponibilidade se o produto estiver na validade
# TODO - Criar método de excluir a entrada se a validade < curdate()
-- SELECT * FROM Ingredientes WHERE Validade >= curdate();

INSERT INTO Funcionarios(CPF, Nome, Data_Contrato, Cargo)
VALUES
	('67952834100', 'Roberto Magalhães' , '2016-02-09', 'ADM')
;

INSERT INTO Funcionarios()
VALUES
	('10642593870', 'Julio Oliveira' , '2016-02-12', 'CHEF', '67952834100'),
    ('89642503710', 'Marcia Pereira' , '2017-01-18', 'RECEPCAO', '67952834100'),
    ('50268913740', 'Gorete da Fofoca' , '2017-04-16', 'ADMINISTRACAO', '67952834100'),
    ('20165798430', 'Juscelino do Domino' , '2018-09-25', 'CHEF', '10642593870'),
    ('60953247180', 'Michael Jordan' , '2019-08-30', 'ADMINISTRACAO', '67952834100'),
	('68549210730', 'Pedrinho do Baile' , '2021-09-12', 'ADMINISTRACAO', '60953247180'),
    ('43712068950', 'Daiane dos Santos' , '2018-10-05', 'RECEPCAO', '89642503710'),
    ('58610743290', 'Felipe Baiano' , '2018-07-21', 'CHEF', '10642593870'),
    ('16784230590', 'Margarete Lima', '2018-05-15', 'RECEPCAO', '43712068950')
;

INSERT INTO Email_Func()
VALUES
	('67952834100', 'rmagal@gmail.com' ),
    ('10642593870', 'seujulio@gmail.com'),
    ('89642503710', 'mpereira@gmail.com'),
    ('50268913740', 'senhorado71@gmail.com'),
    ('20165798430', 'domingo@domino.br'),
    ('68549210730', 'mcpedrinnn_do_baile@gmail.com'),
    ('60953247180', 'oneal@nba.na'),
    ('43712068950', 'santos@ginasta.br'),
    ('58610743290', 'felipepchef@estelar.com'),
    ('16784230590', 'donalima@gmail.com')
;

INSERT INTO Telefone_Func()
VALUES
	('67952834100', '21 84536694' ),
    ('10642593870', '16 31244813'),
    ('89642503710', '65 80452254'),
    ('50268913740', '41 50138403'),
    ('20165798430', '34 42314149'),
    ('68549210730', '21 63115282'),
    ('60953247180', '91 53078504'),
    ('43712068950', '11 98765865'),
    ('58610743290', '67 89998212'),
    ('16784230590', '11 41336478')
;

INSERT INTO Clientes(Nome)
VALUES
	('Brenda Barbosa Pinto'),
    ('Rafaela Ribeiro Castro'),
    ('Tania Castro Fernandes'),
    ('Isabela Cunha Correia'),
    ('Leonardo Gomes Silva')
;

INSERT INTO Clientes(Nome, CPF)
VALUES
	('Ryan Araujo Souza','28937461500')
;

INSERT INTO Utensilios(Nome, Valor_Compra, ID_Forn)
VALUES
	('Chapa Para Lanches', 8118.71, 6),
    ('Fritadeira Eletrica', 11522.38, 6),
    ('Forno Eletrico', 5874.85, 6),
    ('Conservador de Batatas Fritas', 2151.24, 6),
    ('Exaustor', 1286.99, 6),
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
    (1, 3),
    (2, 4),
    (1, 5),
    (6, 5)
    
;

INSERT INTO Pratos(ID, Nome, Valor_Venda, ID_Preparo)
VALUES
	(1, 'Porcao de Batata Frita', 17.00, 1),
    (2, 'Cheeseburguer', 19.50, 2),
    (3, 'X-Frango', 21.00, 3),
    (4, 'Porcao de Aneis de Cebola', 15.00, 4),
    (5, 'X-Picanha', 23.50, 5)
;

INSERT INTO Pedidos(Data_Pedido, Total, ID_Func, ID_Mesa)
VALUES
	('2022-07-08 18:50', 47.50, '89642503710', 2),
    ('2022-07-31 10:10', 167.00, '67952834100', 4),
    ('2022-08-05 19:46', 144.00, '67952834100', 1),
    ('2022-08-18 09:11', 200.50, '43712068950', 8),
    ('2022-08-27 12:30', 3.50, '89642503710', 5)
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