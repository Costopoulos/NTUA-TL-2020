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
