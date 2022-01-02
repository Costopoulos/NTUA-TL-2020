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
-- Table structure for table `charging`
--

DROP TABLE IF EXISTS `charging`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `charging` (
  `Charging_id` int(11) NOT NULL,
  `Start` datetime NOT NULL,
  `Finish` datetime NOT NULL,
  `Type` varchar(45) NOT NULL,
  `User_id` int(11) NOT NULL,
  `Station_id` int(11) NOT NULL,
  `Car_id` int(11) NOT NULL,
  `Payment_id` int(11) NOT NULL,
  `Point_id` int(11) NOT NULL,
  PRIMARY KEY (`Charging_id`),
  KEY `fk_Charging_User1_idx` (`User_id`),
  KEY `fk_Charging_Station1_idx` (`Station_id`),
  KEY `fk_Charging_Car1_idx` (`Car_id`),
  KEY `fk_Charging_Payment1_idx` (`Payment_id`),
  KEY `fk_Charging_Point1_idx` (`Point_id`),
  CONSTRAINT `fk_Charging_Car1` FOREIGN KEY (`Car_id`) REFERENCES `car` (`Car_id`),
  CONSTRAINT `fk_Charging_Payment1` FOREIGN KEY (`Payment_id`) REFERENCES `payment` (`Payment_id`),
  CONSTRAINT `fk_Charging_Point1` FOREIGN KEY (`Point_id`) REFERENCES `point` (`Point_id`),
  CONSTRAINT `fk_Charging_Station1` FOREIGN KEY (`Station_id`) REFERENCES `station` (`Station_id`),
  CONSTRAINT `fk_Charging_User1` FOREIGN KEY (`User_id`) REFERENCES `pleasework_user` (`User_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `charging`
--

LOCK TABLES `charging` WRITE;
/*!40000 ALTER TABLE `charging` DISABLE KEYS */;
INSERT INTO `charging` VALUES (1,'2021-01-24 14:10:41','2021-01-24 14:25:41','fast',1,13,1,1,96),(2,'2021-01-26 11:59:44','2021-01-26 12:14:44','fast',2,12,2,2,76),(3,'2021-02-12 21:44:52','2021-02-12 21:59:52','fast',3,1,3,3,47),(4,'2021-01-22 01:13:48','2021-01-22 01:28:48','fast',4,10,4,4,52),(5,'2021-01-13 02:28:26','2021-01-13 02:43:26','fast',5,17,5,5,37),(6,'2021-01-08 01:34:30','2021-01-08 01:49:30','fast',6,4,6,6,5),(7,'2021-02-05 22:20:50','2021-02-05 22:35:50','fast',7,11,7,7,81),(8,'2021-01-01 00:52:51','2021-01-01 01:07:51','fast',8,20,8,8,87),(9,'2021-01-20 11:20:34','2021-01-20 11:35:34','fast',9,9,9,9,93),(10,'2021-01-23 08:31:27','2021-01-23 08:46:27','fast',10,10,10,10,86),(11,'2021-01-17 18:31:49','2021-01-17 18:46:49','fast',11,2,11,11,13),(12,'2021-01-15 22:11:35','2021-01-15 22:26:35','fast',12,4,12,12,5),(13,'2021-02-02 18:20:57','2021-02-02 18:35:57','fast',13,1,13,13,19),(14,'2021-01-08 15:23:13','2021-01-08 15:38:13','fast',14,6,14,14,84),(15,'2021-01-31 11:48:33','2021-01-31 12:03:33','fast',15,12,15,15,75),(16,'2021-01-24 16:49:24','2021-01-24 17:04:24','fast',16,2,16,16,13),(17,'2021-02-01 02:41:45','2021-02-01 02:56:45','fast',17,6,17,17,1),(18,'2021-01-03 10:37:05','2021-01-03 10:52:05','fast',18,7,18,18,2),(19,'2021-01-12 03:34:05','2021-01-12 03:49:05','fast',19,16,19,19,100),(20,'2021-02-10 06:30:10','2021-02-10 06:45:10','fast',20,13,20,20,50),(21,'2021-01-13 05:16:31','2021-01-13 05:31:31','fast',21,16,21,21,16),(22,'2021-01-08 20:41:16','2021-01-08 20:56:16','fast',22,17,22,22,46),(23,'2021-01-11 16:02:25','2021-01-11 16:17:25','fast',23,13,23,23,42),(24,'2021-01-13 22:10:00','2021-01-13 22:25:00','fast',24,7,24,24,8),(25,'2021-02-03 14:27:11','2021-02-03 14:42:11','fast',25,20,25,25,3),(26,'2021-01-14 07:28:45','2021-01-14 07:58:45','medium',26,13,26,26,92),(27,'2021-02-06 15:03:15','2021-02-06 15:33:15','medium',27,10,27,27,39),(28,'2021-02-11 18:38:31','2021-02-11 19:08:31','medium',28,12,28,28,11),(29,'2021-02-03 19:01:32','2021-02-03 19:31:32','medium',29,3,29,29,49),(30,'2021-02-02 05:53:32','2021-02-02 06:23:32','medium',30,20,30,30,20),(31,'2021-01-05 23:13:03','2021-01-05 23:43:03','medium',31,14,31,31,22),(32,'2021-01-31 06:06:24','2021-01-31 06:36:24','medium',32,13,32,32,92),(33,'2021-02-02 18:59:57','2021-02-02 19:29:57','medium',33,7,33,33,8),(34,'2021-01-17 04:19:00','2021-01-17 04:49:00','medium',34,15,34,34,28),(35,'2021-02-09 08:45:40','2021-02-09 09:15:40','medium',35,9,35,35,93),(36,'2021-01-04 02:05:55','2021-01-04 02:35:55','medium',36,8,36,36,9),(37,'2021-01-28 09:34:48','2021-01-28 10:04:48','medium',37,18,37,37,36),(38,'2021-01-28 11:15:53','2021-01-28 11:45:53','medium',38,14,38,38,94),(39,'2021-02-11 11:55:55','2021-02-11 12:25:55','medium',39,14,39,39,56),(40,'2021-01-17 14:58:44','2021-01-17 15:28:44','medium',40,9,40,40,93),(41,'2021-01-31 09:21:10','2021-01-31 09:51:10','medium',41,10,41,41,69),(42,'2021-01-14 05:48:58','2021-01-14 06:18:58','medium',42,7,42,42,29),(43,'2021-01-08 10:18:02','2021-01-08 10:48:02','medium',43,19,43,43,25),(44,'2021-02-01 09:44:16','2021-02-01 10:14:16','medium',44,10,44,44,41),(45,'2021-01-16 13:42:18','2021-01-16 14:12:18','medium',45,5,45,45,44),(46,'2021-02-03 22:26:54','2021-02-03 22:56:54','medium',46,15,46,46,70),(47,'2021-01-29 05:43:43','2021-01-29 06:13:43','medium',47,7,47,47,2),(48,'2021-02-07 00:40:33','2021-02-07 01:10:33','medium',48,4,48,48,57),(49,'2021-01-24 09:27:12','2021-01-24 09:57:12','medium',49,6,49,49,1),(50,'2021-01-01 10:18:50','2021-01-01 10:48:50','medium',50,18,50,50,79),(51,'2021-01-08 20:26:42','2021-01-08 21:26:42','slow',51,4,51,51,38),(52,'2021-01-31 07:31:20','2021-01-31 08:31:20','slow',52,5,52,52,17),(53,'2021-01-18 01:28:30','2021-01-18 02:28:30','slow',53,5,53,53,44),(54,'2021-01-20 00:12:42','2021-01-20 01:12:42','slow',54,9,54,54,12),(55,'2021-01-26 13:56:29','2021-01-26 14:56:29','slow',55,5,55,55,44),(56,'2021-01-26 18:59:09','2021-01-26 19:59:09','slow',56,9,56,56,12),(57,'2021-01-15 03:04:20','2021-01-15 04:04:20','slow',57,2,57,57,43),(58,'2021-01-10 02:47:38','2021-01-10 03:47:38','slow',58,18,58,58,36),(59,'2021-01-06 17:18:56','2021-01-06 18:18:56','slow',59,1,59,59,58),(60,'2021-02-11 23:03:24','2021-02-12 00:03:24','slow',60,16,60,60,16),(61,'2021-01-18 05:03:56','2021-01-18 06:03:56','slow',61,6,61,61,73),(62,'2021-01-29 11:44:40','2021-01-29 12:44:40','slow',62,8,62,62,33),(63,'2021-01-20 21:20:19','2021-01-20 22:20:19','slow',63,18,63,63,36),(64,'2021-01-19 18:41:25','2021-01-19 19:41:25','slow',64,17,64,64,48),(65,'2021-02-12 21:27:33','2021-02-12 22:27:33','slow',65,11,65,65,82),(66,'2021-02-04 10:48:56','2021-02-04 11:48:56','slow',66,16,66,66,21),(67,'2021-01-18 13:31:40','2021-01-18 14:31:40','slow',67,16,67,67,23),(68,'2021-01-16 10:59:35','2021-01-16 11:59:35','slow',68,12,68,68,76),(69,'2021-01-12 05:28:36','2021-01-12 06:28:36','slow',69,17,69,69,37),(70,'2021-01-17 00:52:50','2021-01-17 01:52:50','slow',70,10,70,70,35),(71,'2021-01-08 21:58:06','2021-01-08 22:58:06','slow',71,10,71,71,69),(72,'2021-01-22 02:24:25','2021-01-22 03:24:25','slow',72,20,72,72,3),(73,'2021-01-21 23:45:10','2021-01-22 00:45:10','slow',73,17,73,73,34),(74,'2021-01-16 09:51:11','2021-01-16 10:51:11','slow',74,10,74,74,35),(75,'2021-01-18 17:45:03','2021-01-18 18:45:03','slow',75,4,75,75,7),(76,'2021-01-21 00:44:11','2021-01-21 00:59:11','fast',76,11,76,76,81),(77,'2021-02-01 02:31:20','2021-02-01 02:46:20','fast',77,4,77,77,57),(78,'2021-02-09 00:44:20','2021-02-09 00:59:20','fast',78,12,78,78,59),(79,'2021-01-20 10:48:18','2021-01-20 11:03:18','fast',79,5,79,79,17),(80,'2021-01-02 09:23:48','2021-01-02 09:38:48','fast',80,16,80,80,16),(81,'2021-02-06 12:24:36','2021-02-06 12:39:36','fast',81,6,81,81,73),(82,'2021-01-31 11:28:19','2021-01-31 11:43:19','fast',82,9,82,82,12),(83,'2021-01-29 17:36:55','2021-01-29 17:51:55','fast',83,19,83,83,25),(84,'2021-02-04 18:19:54','2021-02-04 18:34:54','fast',84,2,84,84,13),(85,'2021-02-05 18:47:09','2021-02-05 19:02:09','fast',85,13,85,85,54),(86,'2021-01-04 20:50:32','2021-01-04 21:05:32','fast',86,19,86,86,25),(87,'2021-01-30 08:22:58','2021-01-30 08:37:58','fast',87,18,87,87,79),(88,'2021-02-02 05:57:05','2021-02-02 06:12:05','fast',88,3,88,88,55),(89,'2021-01-01 23:27:05','2021-01-01 23:42:05','fast',89,16,89,89,23),(90,'2021-01-25 04:43:15','2021-01-25 04:58:15','fast',90,14,90,90,22),(91,'2021-01-01 15:50:57','2021-01-01 16:05:57','fast',91,2,91,91,43),(92,'2021-02-04 13:00:34','2021-02-04 13:15:34','fast',92,19,92,92,27),(93,'2021-01-22 16:06:55','2021-01-22 16:21:55','fast',93,8,93,93,33),(94,'2021-01-26 08:52:26','2021-01-26 09:07:26','fast',94,4,94,94,85),(95,'2021-02-08 20:32:08','2021-02-08 20:47:08','fast',95,18,95,95,36),(96,'2021-01-20 18:58:48','2021-01-20 19:13:48','fast',96,20,96,96,53),(97,'2021-01-13 06:00:15','2021-01-13 06:15:15','fast',97,6,97,97,1),(98,'2021-01-01 06:39:52','2021-01-01 06:54:52','fast',98,19,98,98,25),(99,'2021-01-02 05:35:28','2021-01-02 05:50:28','fast',99,17,99,99,37),(100,'2021-01-29 13:20:46','2021-01-29 13:20:46','fast',100,16,100,100,16);
/*!40000 ALTER TABLE `charging` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-27 21:19:03
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
-- Table structure for table `energy_provider`
--

DROP TABLE IF EXISTS `energy_provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `energy_provider` (
  `Provider_id` int(11) NOT NULL,
  `Name` varchar(45) NOT NULL,
  PRIMARY KEY (`Provider_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `energy_provider`
--

LOCK TABLES `energy_provider` WRITE;
/*!40000 ALTER TABLE `energy_provider` DISABLE KEYS */;
INSERT INTO `energy_provider` VALUES (1,'DEI'),(2,'Voltron'),(3,'ShellEN'),(4,'Electro'),(5,'Vesenrgy');
/*!40000 ALTER TABLE `energy_provider` ENABLE KEYS */;
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
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `Payment_id` int(11) NOT NULL,
  `DateTime` datetime NOT NULL,
  `Amount` double NOT NULL,
  `Method` varchar(45) NOT NULL,
  `Bank` varchar(45) NOT NULL,
  PRIMARY KEY (`Payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (1,'2021-01-24 14:25:41',30.65,'wallet','Alphabank'),(2,'2021-01-26 12:14:44',35.65,'card','Ethniki'),(3,'2021-02-12 21:59:52',65.18,'wallet','Alphabank'),(4,'2021-01-22 01:28:48',94.14,'wallet','Piraeus'),(5,'2021-01-13 02:43:26',98.09,'card','Veskibank'),(6,'2021-01-08 01:49:30',70.55,'wallet','Piraeus'),(7,'2021-02-05 22:35:50',40.15,'wallet','Ethniki'),(8,'2021-01-01 01:07:51',50.95,'card','Ethniki'),(9,'2021-01-20 11:35:34',62.37,'wallet','Ethniki'),(10,'2021-01-23 08:46:27',77.6,'wallet','Piraeus'),(11,'2021-01-17 18:46:49',11.14,'wallet','Ethniki'),(12,'2021-01-15 22:26:35',5.48,'card','Piraeus'),(13,'2021-02-02 18:35:57',77.3,'card','Ethniki'),(14,'2021-01-08 15:38:13',73.43,'card','Veskibank'),(15,'2021-01-31 12:03:33',25.88,'card','Ethniki'),(16,'2021-01-24 17:04:24',47.81,'wallet','Eurobank'),(17,'2021-02-01 02:56:45',52.45,'wallet','Alphabank'),(18,'2021-01-03 10:52:05',69.03,'wallet','Veskibank'),(19,'2021-01-12 03:49:05',9.43,'wallet','Ethniki'),(20,'2021-02-10 06:45:10',97.05,'wallet','Eurobank'),(21,'2021-01-13 05:31:31',14.07,'wallet','Ethniki'),(22,'2021-01-08 20:56:16',9,'wallet','Ethniki'),(23,'2021-01-11 16:17:25',90.51,'wallet','Ethniki'),(24,'2021-01-13 22:25:00',9.42,'card','Alphabank'),(25,'2021-02-03 14:42:11',58.4,'card','Veskibank'),(26,'2021-01-14 07:58:45',9.89,'wallet','Ethniki'),(27,'2021-02-06 15:33:15',16.92,'card','Alphabank'),(28,'2021-02-11 19:08:31',46.14,'wallet','Alphabank'),(29,'2021-02-03 19:31:32',72.69,'wallet','Veskibank'),(30,'2021-02-02 06:23:32',77.29,'card','Eurobank'),(31,'2021-01-05 23:43:03',11.31,'card','Eurobank'),(32,'2021-01-31 06:36:24',33.9,'wallet','Alphabank'),(33,'2021-02-02 19:29:57',30.46,'wallet','Eurobank'),(34,'2021-01-17 04:49:00',41.84,'card','Piraeus'),(35,'2021-02-09 09:15:40',52.59,'wallet','Eurobank'),(36,'2021-01-04 02:35:55',77.63,'wallet','Ethniki'),(37,'2021-01-28 10:04:48',11.77,'card','Piraeus'),(38,'2021-01-28 11:45:53',86.91,'wallet','Eurobank'),(39,'2021-02-11 12:25:55',79.54,'card','Piraeus'),(40,'2021-01-17 15:28:44',33.5,'card','Veskibank'),(41,'2021-01-31 09:51:10',5.47,'wallet','Piraeus'),(42,'2021-01-14 06:18:58',33.24,'card','Veskibank'),(43,'2021-01-08 10:48:02',98.11,'wallet','Piraeus'),(44,'2021-02-01 10:14:16',82.49,'wallet','Ethniki'),(45,'2021-01-16 14:12:18',54.33,'card','Ethniki'),(46,'2021-02-03 22:56:54',60.37,'card','Ethniki'),(47,'2021-01-29 06:13:43',43.11,'card','Eurobank'),(48,'2021-02-07 01:10:33',42.57,'wallet','Ethniki'),(49,'2021-01-24 09:57:12',40.11,'card','Ethniki'),(50,'2021-01-01 10:48:50',35.94,'card','Eurobank'),(51,'2021-01-08 21:26:42',49.62,'wallet','Eurobank'),(52,'2021-01-31 08:31:20',73.55,'wallet','Piraeus'),(53,'2021-01-18 02:28:30',21.42,'card','Alphabank'),(54,'2021-01-20 01:12:42',37.49,'card','Piraeus'),(55,'2021-01-26 14:56:29',30.23,'card','Piraeus'),(56,'2021-01-26 19:59:09',19.97,'card','Veskibank'),(57,'2021-01-15 04:04:20',76.52,'wallet','Piraeus'),(58,'2021-01-10 03:47:38',65.81,'wallet','Veskibank'),(59,'2021-01-06 18:18:56',76.61,'wallet','Piraeus'),(60,'2021-02-12 00:03:24',49.96,'wallet','Piraeus'),(61,'2021-01-18 06:03:56',56.68,'wallet','Eurobank'),(62,'2021-01-29 12:44:40',82.55,'card','Ethniki'),(63,'2021-01-20 22:20:19',41.63,'wallet','Ethniki'),(64,'2021-01-19 19:41:25',47.94,'wallet','Veskibank'),(65,'2021-02-12 22:27:33',69.62,'wallet','Eurobank'),(66,'2021-02-04 11:48:56',10.06,'wallet','Eurobank'),(67,'2021-01-18 14:31:40',90.48,'card','Veskibank'),(68,'2021-01-16 11:59:35',65.47,'wallet','Alphabank'),(69,'2021-01-12 06:28:36',21.2,'wallet','Ethniki'),(70,'2021-01-17 01:52:50',98.19,'wallet','Ethniki'),(71,'2021-01-08 22:58:06',54.15,'wallet','Eurobank'),(72,'2021-01-22 03:24:25',95.66,'card','Veskibank'),(73,'2021-01-22 00:45:10',17.02,'card','Eurobank'),(74,'2021-01-16 10:51:11',55.95,'wallet','Piraeus'),(75,'2021-01-18 18:45:03',93.9,'card','Eurobank'),(76,'2021-01-21 00:59:11',8.48,'wallet','Veskibank'),(77,'2021-02-01 02:46:20',6.42,'card','Eurobank'),(78,'2021-02-09 00:59:20',43.1,'card','Veskibank'),(79,'2021-01-20 11:03:18',6.59,'wallet','Alphabank'),(80,'2021-01-02 09:38:48',87.2,'card','Eurobank'),(81,'2021-02-06 12:39:36',80.17,'card','Veskibank'),(82,'2021-01-31 11:43:19',64.21,'wallet','Eurobank'),(83,'2021-01-29 17:51:55',50.42,'card','Alphabank'),(84,'2021-02-04 18:34:54',24.52,'card','Eurobank'),(85,'2021-02-05 19:02:09',6.87,'wallet','Eurobank'),(86,'2021-01-04 21:05:32',90.98,'wallet','Piraeus'),(87,'2021-01-30 08:37:58',54.52,'wallet','Piraeus'),(88,'2021-02-02 06:12:05',52.82,'card','Eurobank'),(89,'2021-01-01 23:42:05',46.9,'card','Piraeus'),(90,'2021-01-25 04:58:15',84.25,'card','Eurobank'),(91,'2021-01-01 16:05:57',40.39,'wallet','Ethniki'),(92,'2021-02-04 13:15:34',45.31,'wallet','Piraeus'),(93,'2021-01-22 16:21:55',89.99,'card','Eurobank'),(94,'2021-01-26 09:07:26',59.14,'wallet','Piraeus'),(95,'2021-02-08 20:47:08',32,'card','Piraeus'),(96,'2021-01-20 19:13:48',72.7,'wallet','Ethniki'),(97,'2021-01-13 06:15:15',35.04,'wallet','Ethniki'),(98,'2021-01-01 06:54:52',88.37,'card','Veskibank'),(99,'2021-01-02 05:50:28',63.39,'wallet','Ethniki'),(100,'2021-01-29 13:20:46',82.12,'wallet','Veskibank');
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
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
-- Table structure for table `point`
--

DROP TABLE IF EXISTS `point`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `point` (
  `Station_id` int(11) NOT NULL,
  `Point_id` int(11) NOT NULL,
  `Operator` varchar(45) NOT NULL,
  PRIMARY KEY (`Point_id`),
  KEY `fk_Point_Station1_idx` (`Station_id`),
  CONSTRAINT `fk_Point_Station1` FOREIGN KEY (`Station_id`) REFERENCES `station` (`Station_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `point`
--

LOCK TABLES `point` WRITE;
/*!40000 ALTER TABLE `point` DISABLE KEYS */;
INSERT INTO `point` VALUES (6,1,'Azalia Gonzalez'),(7,2,'Hope Rowland'),(20,3,'Steel Foley'),(7,4,'Nyssa Navarro'),(4,5,'Victoria William'),(8,6,'Hiroko Middleton'),(4,7,'Joshua Fisher'),(7,8,'Iola Newton'),(8,9,'Bruce Carroll'),(11,10,'Ishmael Garrison'),(12,11,'Carla Vasquez'),(9,12,'Bethany Rice'),(2,13,'Ifeoma Browning'),(15,14,'Lamar Mcguire'),(18,15,'Melvin Harris'),(16,16,'Zane Howell'),(5,17,'Ashely Love'),(3,18,'Rooney Whitfield'),(1,19,'Jordan Bolton'),(20,20,'Sylvia Kline'),(16,21,'Kenyon Woodard'),(14,22,'Lawrence Montgomery'),(16,23,'Devin Fletcher'),(15,24,'Carla Foley'),(19,25,'Vivien Callahan'),(9,26,'Carter Melendez'),(19,27,'Octavius Burgess'),(15,28,'Casey Mason'),(7,29,'Leonard Greene'),(17,30,'Casey Snyder'),(17,31,'Kato Carter'),(12,32,'Ursula Dominguez'),(8,33,'Geoffrey Barlow'),(17,34,'Lars Greene'),(10,35,'Myles Moses'),(18,36,'Iona Shields'),(17,37,'Theodore Morrow'),(4,38,'Sloane Sloan'),(10,39,'Illana Wise'),(4,40,'Owen Solis'),(10,41,'Levi Noel'),(13,42,'Camden Obrien'),(2,43,'Lamar Frank'),(5,44,'Juliet Kim'),(10,45,'Cameran Giles'),(17,46,'Hunter Wade'),(1,47,'Zorita Farley'),(17,48,'Bryar Velazquez'),(3,49,'Rooney Reed'),(13,50,'Avram Ashley'),(15,51,'Francesca Baldwin'),(10,52,'Morgan Randolph'),(20,53,'Harding Decker'),(13,54,'Brenda Sullivan'),(3,55,'Venus Flynn'),(14,56,'September Joyner'),(4,57,'Sybil Hood'),(1,58,'Nevada Dejesus'),(12,59,'Dominic Melendez'),(13,60,'Ronan Walls'),(7,61,'Evan Rojas'),(1,62,'Sara Juarez'),(15,63,'Ocean Shannon'),(7,64,'Victoria Chase'),(8,65,'Dale Walker'),(8,66,'Rhiannon Bond'),(20,67,'Abdul Davis'),(3,68,'Kenyon Gallegos'),(10,69,'Chancellor Buchanan'),(15,70,'Kenyon Stanley'),(1,71,'Jamalia Pope'),(20,72,'Elizabeth Cardenas'),(6,73,'Sasha Kirby'),(1,74,'Mariam Hendricks'),(12,75,'Nathan Sloan'),(12,76,'Fay Cooper'),(18,77,'Rahim Mcconnell'),(8,78,'Honorato Duncan'),(18,79,'Kirsten Bentley'),(8,80,'Scarlet Holman'),(11,81,'Chandler Hopper'),(11,82,'Darryl Parrish'),(11,83,'Yvonne Hughes'),(6,84,'Brielle Welch'),(4,85,'Nero Guy'),(10,86,'Kendall Le'),(20,87,'Brynne Ferrell'),(12,88,'Jeanette Mills'),(5,89,'Luke Maddox'),(1,90,'John Farrell'),(1,91,'Rebecca Christian'),(13,92,'Frances Rios'),(9,93,'Anastasia Monroe'),(14,94,'Roth Berg'),(11,95,'Kyra Brennan'),(13,96,'Cullen Stone'),(3,97,'Raja Waters'),(7,98,'Ashely Guerrero'),(12,99,'Cleo Velasquez'),(16,100,'Guy Cox');
/*!40000 ALTER TABLE `point` ENABLE KEYS */;
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
-- Table structure for table `station_phones`
--

DROP TABLE IF EXISTS `station_phones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `station_phones` (
  `Station_id` int(11) NOT NULL,
  `Phone_no` varchar(15) NOT NULL,
  KEY `fk_Station_Phones_Station1_idx` (`Station_id`),
  CONSTRAINT `fk_Station_Phones_Station1` FOREIGN KEY (`Station_id`) REFERENCES `station` (`Station_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `station_phones`
--

LOCK TABLES `station_phones` WRITE;
/*!40000 ALTER TABLE `station_phones` DISABLE KEYS */;
INSERT INTO `station_phones` VALUES (1,'0800 1111'),(2,'07145 014254'),(3,'056 3569 2906'),(4,'07624 456775'),(5,'0800 557888'),(6,'0800 509 0763'),(7,'0808 855 4191'),(8,'(0116) 829 9917'),(9,'0500 296072'),(10,'0800 840 0845'),(11,'0500 455002'),(12,'0800 290 0121'),(13,'0800 003262'),(14,'(018046) 85641'),(15,'(016977) 8817'),(16,'(016977) 3893'),(17,'07624 745843'),(18,'07624 643156'),(19,'056 5148 6743'),(20,'076 0022 9521');
/*!40000 ALTER TABLE `station_phones` ENABLE KEYS */;
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
-- Table structure for table `user_has_car`
--

DROP TABLE IF EXISTS `user_has_car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_has_car` (
  `User_id` int(11) NOT NULL,
  `Car_id` int(11) NOT NULL,
  KEY `fk_User_has_Car_Car1_idx` (`Car_id`),
  KEY `fk_User_has_Car_User_idx` (`User_id`),
  CONSTRAINT `fk_User_has_Car_Car1` FOREIGN KEY (`Car_id`) REFERENCES `car` (`Car_id`),
  CONSTRAINT `fk_User_has_Car_User` FOREIGN KEY (`User_id`) REFERENCES `pleasework_user` (`User_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_has_car`
--

LOCK TABLES `user_has_car` WRITE;
/*!40000 ALTER TABLE `user_has_car` DISABLE KEYS */;
INSERT INTO `user_has_car` VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20),(21,21),(22,22),(23,23),(24,24),(25,25),(26,26),(27,27),(28,28),(29,29),(30,30),(31,31),(32,32),(33,33),(34,34),(35,35),(36,36),(37,37),(38,38),(39,39),(40,40),(41,41),(42,42),(43,43),(44,44),(45,45),(46,46),(47,47),(48,48),(49,49),(50,50),(51,51),(52,52),(53,53),(54,54),(55,55),(56,56),(57,57),(58,58),(59,59),(60,60),(61,61),(62,62),(63,63),(64,64),(65,65),(66,66),(67,67),(68,68),(69,69),(70,70),(71,71),(72,72),(73,73),(74,74),(75,75),(76,76),(77,77),(78,78),(79,79),(80,80),(81,81),(82,82),(83,83),(84,84),(85,85),(86,86),(87,87),(88,88),(89,89),(90,90),(91,91),(92,92),(93,93),(94,94),(95,95),(96,96),(97,97),(98,98),(99,99),(100,100);
/*!40000 ALTER TABLE `user_has_car` ENABLE KEYS */;
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
-- Table structure for table `user_phones`
--

DROP TABLE IF EXISTS `user_phones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_phones` (
  `User_id` int(11) NOT NULL,
  `Phone_no` varchar(15) NOT NULL,
  KEY `fk_User_Phones_User1` (`User_id`),
  CONSTRAINT `fk_User_Phones_User1` FOREIGN KEY (`User_id`) REFERENCES `pleasework_user` (`User_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_phones`
--

LOCK TABLES `user_phones` WRITE;
/*!40000 ALTER TABLE `user_phones` DISABLE KEYS */;
INSERT INTO `user_phones` VALUES (1,'0500 367911'),(2,'0845 46 41'),(3,'(016977) 9860'),(4,'0834 061 5776'),(5,'0845 46 43'),(6,'056 7598 0875'),(7,'0500 713509'),(8,'(022) 8109 1643'),(9,'0851 114 6742'),(10,'0800 575 2801'),(11,'(022) 9377 9125'),(12,'(0110) 534 5194'),(13,'(01830) 157917'),(14,'(0141) 321 8862'),(15,'0800 904 3711'),(16,'0800 509685'),(17,'0800 1111'),(18,'0800 708 0396'),(19,'0800 1111'),(20,'0923 482 0330'),(21,'(023) 7096 2044'),(22,'07624 075118'),(23,'(0117) 875 4377'),(24,'0500 959814'),(25,'(024) 2767 6126'),(26,'07624 525996'),(27,'055 4466 0777'),(28,'0845 46 44'),(29,'0314 925 8945'),(30,'0959 044 7298'),(31,'07332 260687'),(32,'070 3106 3188'),(33,'0800 617829'),(34,'076 1241 8769'),(35,'(01734) 847466'),(36,'07393 140520'),(37,'(015056) 82183'),(38,'055 0322 9495'),(39,'(016977) 3542'),(40,'0975 445 3678'),(41,'0800 487 8501'),(42,'(018047) 72347'),(43,'0381 304 9663'),(44,'(011079) 62560'),(45,'(0141) 048 0239'),(46,'(0141) 990 4012'),(47,'0800 847438'),(48,'(0181) 284 0717'),(49,'055 5856 4625'),(50,'0500 498670'),(51,'(01010) 56903'),(52,'0500 658619'),(53,'07624 871285'),(54,'0308 401 3516'),(55,'056 8336 7521'),(56,'0845 46 41'),(57,'056 7517 2240'),(58,'(016977) 9365'),(59,'0800 040 3987'),(60,'(016747) 67901'),(61,'0800 303772'),(62,'(01426) 693073'),(63,'(015351) 98548'),(64,'0500 797608'),(65,'0349 048 1102'),(66,'(0116) 801 1190'),(67,'(0117) 500 4909'),(68,'0800 1111'),(69,'(015046) 44413'),(70,'0845 46 49'),(71,'(017639) 60089'),(72,'(0115) 285 1710'),(73,'(0117) 360 8486'),(74,'0966 819 3010'),(75,'(016977) 8846'),(76,'0930 754 7447'),(77,'(01006) 64913'),(78,'(026) 7050 9841'),(79,'07426 542229'),(80,'055 4851 3288'),(81,'(025) 6749 1572'),(82,'055 8443 4185'),(83,'07624 194501'),(84,'0500 525775'),(85,'0856 798 7049'),(86,'(01836) 53475'),(87,'0500 827421'),(88,'0845 46 46'),(89,'0800 742135'),(90,'076 9570 5484'),(91,'0336 435 6566'),(92,'(012932) 62799'),(93,'(016977) 3929'),(94,'(0114) 909 2521'),(95,'076 7229 0695'),(96,'0500 402195'),(97,'056 8587 1884'),(98,'0845 46 43'),(99,'0929 691 1603'),(100,'(016977) 4297');
/*!40000 ALTER TABLE `user_phones` ENABLE KEYS */;
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

