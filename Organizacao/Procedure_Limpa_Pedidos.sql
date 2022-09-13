CREATE DEFINER=`root`@`localhost` PROCEDURE `Limpa_Pedidos`()
BEGIN
	DELETE FROM Pratos_Pedidos;
	DELETE FROM Bebidas_Pedidos;
	DELETE FROM Pedidos;
END