CREATE DEFINER=`root`@`localhost` PROCEDURE `Limpa_Mesas`()
BEGIN
     UPDATE Mesa SET ID_Cliente = NULL;
END