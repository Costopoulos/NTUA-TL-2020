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
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car` (
  `Car_id` int(11) NOT NULL,
  `Brand` varchar(45) NOT NULL,
  `Battery_Size` int(11) NOT NULL,
  PRIMARY KEY (`Car_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,'Infiniti',119),(2,'Cadillac',94),(3,'Nissan',87),(4,'Volvo',114),(5,'Ferrari',87),(6,'Renault',87),(7,'Subaru',113),(8,'Vauxhall',119),(9,'Suzuki',111),(10,'Smart',102),(11,'Toyota',90),(12,'Seat',88),(13,'Isuzu',120),(14,'Nissan',117),(15,'Citroën',108),(16,'Porsche',108),(17,'Mazda',100),(18,'BMW',85),(19,'Kenworth',114),(20,'FAW',89),(21,'Suzuki',99),(22,'Toyota',115),(23,'Toyota',119),(24,'Jeep',102),(25,'Dacia',115),(26,'BMW',118),(27,'Acura',97),(28,'Skoda',106),(29,'Dongfeng Motor',119),(30,'Daihatsu',95),(31,'Mahindra and Mahindra',85),(32,'Daimler',110),(33,'Tata Motors',83),(34,'FAW',101),(35,'Mitsubishi Motors',97),(36,'Chevrolet',109),(37,'Mahindra and Mahindra',100),(38,'GMC',89),(39,'Daimler',104),(40,'Suzuki',86),(41,'Ford',116),(42,'Daimler',119),(43,'Infiniti',100),(44,'Infiniti',89),(45,'Peugeot',112),(46,'Skoda',103),(47,'Lincoln',100),(48,'Infiniti',105),(49,'Dodge',97),(50,'MINI',87),(51,'Kia Motors',103),(52,'Mahindra and Mahindra',113),(53,'GMC',83),(54,'BMW',118),(55,'Suzuki',81),(56,'Cadillac',94),(57,'General Motors',99),(58,'Chevrolet',84),(59,'Renault',119),(60,'Tata Motors',118),(61,'Honda',113),(62,'FAW',96),(63,'GMC',93),(64,'Chevrolet',116),(65,'Chevrolet',119),(66,'Smart',109),(67,'Infiniti',87),(68,'GMC',81),(69,'Jeep',114),(70,'Renault',103),(71,'Maruti Suzuki',96),(72,'RAM Trucks',96),(73,'Volvo',86),(74,'Acura',98),(75,'Ferrari',99),(76,'Mercedes-Benz',80),(77,'Dacia',92),(78,'Buick',100),(79,'Peugeot',111),(80,'Honda',81),(81,'Lexus',110),(82,'Volvo',114),(83,'Nissan',98),(84,'RAM Trucks',90),(85,'GMC',103),(86,'JLR',90),(87,'Chevrolet',82),(88,'Skoda',84),(89,'Honda',118),(90,'RAM Trucks',88),(91,'JLR',116),(92,'Smart',111),(93,'Lexus',87),(94,'Isuzu',87),(95,'Buick',111),(96,'Nissan',119),(97,'General Motors',119),(98,'Skoda',117),(99,'Porsche',117),(100,'Seat',106);
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
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
