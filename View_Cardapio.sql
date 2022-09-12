CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `Restaurante_BD`.`Cardapio` AS
    SELECT 
        `Bebidas`.`Nome` AS `Nome`,
        `Bebidas`.`Valor_Venda` AS `Valor_Venda`
    FROM
        (SELECT 
            `Restaurante_BD`.`Bebidas`.`ID` AS `ID`,
                `Restaurante_BD`.`Bebidas`.`Nome` AS `Nome`,
                `Restaurante_BD`.`Bebidas`.`Validade` AS `Validade`,
                `Restaurante_BD`.`Bebidas`.`Valor_Venda` AS `Valor_Venda`,
                `Restaurante_BD`.`Bebidas`.`Valor_Compra` AS `Valor_Compra`,
                `Restaurante_BD`.`Bebidas`.`Tipo` AS `Tipo`,
                `Restaurante_BD`.`Bebidas`.`ID_Forn` AS `ID_Forn`
        FROM
            `Restaurante_BD`.`Bebidas`
        WHERE
            (`Restaurante_BD`.`Bebidas`.`Validade` > CURDATE())) `Bebidas` 
    UNION SELECT 
        `Pratos`.`Nome` AS `Nome`,
        `Pratos`.`Valor_Venda` AS `Valor_Venda`
    FROM
        (SELECT 
            `Restaurante_BD`.`Pratos`.`ID` AS `ID`,
                `Restaurante_BD`.`Pratos`.`Nome` AS `Nome`,
                `Restaurante_BD`.`Pratos`.`Valor_Venda` AS `Valor_Venda`,
                `Restaurante_BD`.`Pratos`.`ID_Preparo` AS `ID_Preparo`
        FROM
            `Restaurante_BD`.`Pratos`
        WHERE
            `Restaurante_BD`.`Pratos`.`ID_Preparo` IN (SELECT 
                    `Restaurante_BD`.`Pratos`.`ID_Preparo`
                FROM
                    `Restaurante_BD`.`Pratos`
                WHERE
                    `Restaurante_BD`.`Pratos`.`ID_Preparo` IN (SELECT DISTINCT
                            `Restaurante_BD`.`Ingredientes_Receita`.`ID_Preparo`
                        FROM
                            ((SELECT 
                            `Restaurante_BD`.`Ingredientes`.`ID` AS `ID`,
                                `Restaurante_BD`.`Ingredientes`.`Nome` AS `Nome`,
                                `Restaurante_BD`.`Ingredientes`.`Validade` AS `Validade`,
                                `Restaurante_BD`.`Ingredientes`.`Armazenamento` AS `Armazenamento`,
                                `Restaurante_BD`.`Ingredientes`.`Valor_Compra` AS `Valor_Compra`,
                                `Restaurante_BD`.`Ingredientes`.`Tipo` AS `Tipo`,
                                `Restaurante_BD`.`Ingredientes`.`ID_Forn` AS `ID_Forn`
                        FROM
                            `Restaurante_BD`.`Ingredientes`
                        WHERE
                            (`Restaurante_BD`.`Ingredientes`.`Validade` < CURDATE())) `A`
                        JOIN `Restaurante_BD`.`Ingredientes_Receita`)
                        WHERE
                            (`A`.`ID` = `Restaurante_BD`.`Ingredientes_Receita`.`ID_Ingr`))
                        IS FALSE)) `Pratos`