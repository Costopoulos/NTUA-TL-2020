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
