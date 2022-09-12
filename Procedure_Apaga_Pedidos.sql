CREATE DEFINER=`root`@`localhost` PROCEDURE `Apaga_Pedidos`(
	IN data_apagar DATE
)
BEGIN
	SELECT * FROM Pedidos WHERE DATE(Data_Pedido) <= data_apagar;
    
    IF data_apagar <= curdate() THEN
    
		DELETE FROM Pedidos Where Data_Pedido <= now();
        
	END IF;

END