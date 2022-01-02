-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `station`
--

DROP TABLE IF EXISTS `station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `station` (
  `Station_id` int(11) NOT NULL,
  `Country` varchar(45) NOT NULL,
  `City` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `Energy_Provider_id` int(11) NOT NULL,
  PRIMARY KEY (`Station_id`),
  KEY `fk_Station_Energy_Provider1_idx` (`Energy_Provider_id`),
  CONSTRAINT `fk_Station_Energy_Provider1` FOREIGN KEY (`Energy_Provider_id`) REFERENCES `energy_provider` (`Provider_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `station`
--

LOCK TABLES `station` WRITE;
/*!40000 ALTER TABLE `station` DISABLE KEYS */;
INSERT INTO `station` VALUES (1,'Greece','Argiroupoli','Ari Velouchioti 45',5),(2,'Greece','Elliniko','Stefanou Sarafi 19',5),(3,'Greece','Ilioupoli','Samarinioti 18',1),(4,'Greece','Ilioupoli','Sarantinou 96',1),(5,'Greece','Nea Smirni','Kostopoulea 69',1),(6,'Greece','Voula','Selas 35',5),(7,'Greece','','Panozevg 14',5),(8,'Greece','Nea Ionia','Lagou 47',2),(9,'Greece','Kifissos','Kiprou 12',4),(10,'Greece','','Argiroupolews 185',2),(11,'Greece','Glifada','Varkizas 99',2),(12,'Greece','Nea Ionia','Athanasiou Diakou 21',5),(13,'Greece','Argiroupoli','Katsantoni 14',1),(14,'Greece','Nea Ionia','Papaspyrou 1742',5),(15,'Greece','Nea Smirni','Veskouki 21',5),(16,'Greece','Alimos','Paleologou 1453',2),(17,'Greece','Patissia','Vladimirou 33',2),(18,'Greece','Nea Smirni','Wewinit 696',4),(19,'Greece','Vari','Sarantaporou 176',3),(20,'Greece','Kifissos','Smirnis 22',3);
/*!40000 ALTER TABLE `station` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-27 21:19:02
