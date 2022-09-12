DROP SCHEMA IF EXISTS Restaurante_BD;
CREATE SCHEMA Restaurante_BD;
USE Restaurante_BD;

CREATE TABLE Funcionarios(
	CPF VARCHAR(11) PRIMARY KEY UNIQUE NOT NULL,
    Nome VARCHAR(70) NOT NULL,
    Data_Contrato DATE,
    Cargo VARCHAR(50) NOT NULL,
    ID_Sup VARCHAR(11),
    FOREIGN KEY(ID_Sup) references Funcionarios(CPF)
);

CREATE TABLE Telefone_Func(
	CPF_Func VARCHAR(11),
	Telefone VARCHAR(11) NOT NULL,
    PRIMARY KEY(CPF_Func, Telefone),
    FOREIGN KEY(CPF_Func) references Funcionarios(CPF)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Email_Func(
	CPF_Func VARCHAR(11),
    Email VARCHAR(100) NOT NULL,
    PRIMARY KEY(CPF_Func, Email),
    FOREIGN KEY(CPF_Func) references Funcionarios(CPF)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Fornecedores(
	ID INTEGER UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(70) NOT NULL UNIQUE
);

CREATE TABLE Telefone_Fornecedores(
	ID_Forn INTEGER UNSIGNED,
    Telefone VARCHAR(15) NOT NULL,
    PRIMARY KEY(ID_Forn, Telefone),
    FOREIGN KEY(ID_Forn) references Fornecedores(ID)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Email_Fornecedores(
	ID_Forn INTEGER UNSIGNED,
    Email VARCHAR(100) NOT NULL,
    PRIMARY KEY(ID_Forn, Email),
    FOREIGN KEY(ID_Forn) references Fornecedores(ID)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Clientes(
	ID INTEGER UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(70) NOT NULL,
    CPF VARCHAR(11)
);

CREATE TABLE Bebidas(
	ID INTEGER UNSIGNED AUTO_INCREMENT,
    Nome VARCHAR(70) NOT NULL,
    Validade DATE NOT NULL,
    Valor_Venda DECIMAL(10, 2) NOT NULL,
    Valor_Compra DECIMAL(10, 2),
    Tipo ENUM('Alcoolica', 'Nao_Alcoolica') NOT NULL,
    ID_Forn INTEGER UNSIGNED NOT NULL,
    PRIMARY KEY(ID, ID_Forn),
    FOREIGN KEY(ID_Forn)references Fornecedores(ID)
        ON UPDATE CASCADE
);

CREATE TABLE Mesa(
	ID INTEGER UNSIGNED NOT NULL PRIMARY KEY,
    Qtd_Lugares INT,
    ID_Cliente INTEGER UNSIGNED,
    FOREIGN KEY(ID_CLiente) references Clientes(ID)
        ON UPDATE CASCADE
);


CREATE TABLE Pedidos(
	ID INTEGER UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Data_Pedido DATETIME,
    Total DECIMAL(10, 2) NOT NULL,
    ID_Func VARCHAR(11) NOT NULL,
    ID_Mesa INTEGER UNSIGNED,
	FOREIGN KEY(ID_Func) references Funcionarios(CPF)
        ON UPDATE CASCADE,
	FOREIGN KEY(ID_Mesa) references Mesa(ID)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Bebidas_Pedidos(
	ID_Pedido INTEGER UNSIGNED NOT NULL,
    ID_Bebida INTEGER UNSIGNED NOT NULL,
    PRIMARY KEY(ID_Pedido, ID_Bebida),
    FOREIGN KEY(ID_Pedido) references Pedidos(ID)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
	FOREIGN KEY(ID_Bebida) references Bebidas(ID)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Ingredientes(
	ID INTEGER UNSIGNED AUTO_INCREMENT,
    Nome VARCHAR(70) NOT NULL,
    Validade DATE NOT NULL,
    Armazenamento ENUM('Seco', 'Frio') NOT NULL,
    Valor_Compra DECIMAL (10, 2),
    Tipo ENUM('Carne', 'Vegetal', 'Pao', 'Extra', 'Queijo') NOT NULL,
    ID_Forn INTEGER UNSIGNED NOT NULL,
    PRIMARY KEY(ID, ID_Forn),
    FOREIGN KEY (ID_Forn) references Fornecedores(ID)
        ON UPDATE CASCADE
);

CREATE TABLE Utensilios(
	ID INTEGER UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(70) NOT NULL,
    Valor_Compra DECIMAL(10, 2),
    ID_Forn INTEGER UNSIGNED NOT NULL references Fornecedores(ID)
);

CREATE TABLE Modo_Preparo(
	ID INTEGER UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Manual BLOB
);

CREATE TABLE Utensilios_Receita(
	ID_Util INTEGER UNSIGNED NOT NULL,
    ID_Preparo INTEGER UNSIGNED NOT NULL,
    PRIMARY KEY(ID_Util, ID_Preparo),
    FOREIGN KEY(ID_Util) references Utensilios(ID)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
	FOREIGN KEY(ID_Preparo) references Modo_Preparo(ID)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Ingredientes_Receita(
	ID_Ingr INTEGER UNSIGNED NOT NULL,
    ID_Preparo INTEGER UNSIGNED NOT NULL,
    PRIMARY KEY(ID_Ingr, ID_Preparo),
    FOREIGN KEY(ID_Ingr) references Ingredientes(ID)		
		ON DELETE CASCADE
        ON UPDATE CASCADE,
	FOREIGN KEY(ID_Preparo) references Modo_Preparo(ID)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Pratos(
	ID INTEGER UNSIGNED PRIMARY KEY,
    Nome VARCHAR(70) NOT NULL,
    Valor_Venda DECIMAL(10, 2) NOT NULL,
    ID_Preparo INTEGER UNSIGNED NOT NULL, 
    FOREIGN KEY(ID_Preparo) references Modo_Preparo(ID)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Pratos_Pedidos(
    ID_Pedido INTEGER UNSIGNED NOT NULL,
	ID_Prato INTEGER UNSIGNED NOT NULL,
    PRIMARY KEY(ID_Pedido, ID_Prato),
    FOREIGN KEY(ID_Pedido) references Pedidos(ID)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
	FOREIGN KEY(ID_Prato) references Pratos(ID)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

