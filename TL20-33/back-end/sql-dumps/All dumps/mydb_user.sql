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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `User_id` int(11) NOT NULL,
  `Username` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Card_id` int(12) NOT NULL,
  `Wallet_id` varchar(15) NOT NULL,
  `Points` int(11) NOT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'George','molestie','eu.erat@sitametluctus.net',1,'100',123),(2,'Fay','bibendum','est@Proin.com',2,'101',80),(3,'Jane','elit,','lorem@velitCras.ca',3,'102',835),(4,'Nathaniel','facilisis','Aliquam.erat.volutpat@necanteblandit.net',4,'103',837),(5,'Branden','enim.','ut.nulla@pedenonummy.edu',5,'104',574),(6,'Renee','tincidunt','per@etnetus.net',6,'105',690),(7,'Quamar','a','dictum.placerat@nibhAliquam.edu',7,'106',669),(8,'Velma','ut,','convallis.dolor@Morbi.edu',8,'107',549),(9,'Damian','luctus','non.magna.Nam@massaSuspendisseeleifend.ca',9,'108',361),(10,'Mason','Sed','nibh.enim.gravida@convallisconvallis.ca',10,'109',755),(11,'Imani','Morbi','enim@Suspendissealiquet.net',11,'110',288),(12,'Otto','vehicula','gravida.molestie@cursusNunc.edu',12,'111',344),(13,'Erica','elit,','laoreet.lectus@morbitristique.org',13,'112',577),(14,'Dante','malesuada','ipsum@Fuscemollis.org',14,'113',660),(15,'Athena','Donec','ac.arcu@egestas.net',15,'114',257),(16,'Lester','dolor,','consectetuer.euismod.est@feliseget.co.uk',16,'115',695),(17,'Thomas','vestibulum,','cursus@dictumcursus.ca',17,'116',718),(18,'Robert','Nunc','blandit.at.nisi@nonmagna.net',18,'117',233),(19,'Harlan','quis','facilisis.non@egestasFusce.org',19,'118',184),(20,'Xyla','porttitor','Proin.ultrices.Duis@risus.org',20,'119',326),(21,'TaShya','arcu','egestas@arcueuodio.net',21,'120',395),(22,'Lee','sit','varius.orci.in@Duissit.net',22,'121',279),(23,'Harding','Nam','ipsum@diameu.edu',23,'122',612),(24,'Isadora','metus.','cubilia.Curae@vulputatenisi.org',24,'123',701),(25,'Hoyt','Nam','Pellentesque.habitant.morbi@aliquetmetus.ca',25,'124',156),(26,'Gay','est,','Suspendisse@faucibuslectus.edu',26,'125',832),(27,'Whoopi','Cras','eu.ligula.Aenean@aliquet.co.uk',27,'126',839),(28,'Gareth','mi','Nunc@ametlorem.co.uk',28,'127',663),(29,'Kimberley','nibh','rutrum.urna@ametmassaQuisque.co.uk',29,'128',733),(30,'Rhoda','nunc.','litora.torquent@malesuada.com',30,'129',828),(31,'Tana','tempor','a.purus.Duis@auctorvitae.ca',31,'130',589),(32,'Rhona','vel,','rhoncus.Nullam@Duissit.edu',32,'131',595),(33,'Gavin','sociis','cursus@erosnec.ca',33,'132',662),(34,'Judith','Cras','enim.Mauris@consequatenim.net',34,'133',115),(35,'Gisela','arcu.','sit@actellus.net',35,'134',658),(36,'Dai','orci','tempor@egetlacus.ca',36,'135',347),(37,'Kirestin','congue','vel.arcu.eu@Cumsociis.edu',37,'136',658),(38,'Sarah','in','id@sedfacilisisvitae.org',38,'137',613),(39,'Vera','tortor.','tincidunt.tempus@Duis.ca',39,'138',469),(40,'Arthur','ipsum.','luctus.sit.amet@loremut.com',40,'139',580),(41,'Stuart','sapien,','Quisque.libero@turpisAliquam.org',41,'140',277),(42,'Whitney','lectus','et.arcu@etlacinia.co.uk',42,'141',461),(43,'Neil','et','consectetuer.cursus.et@ametfaucibus.com',43,'142',606),(44,'Shad','aliquam,','Phasellus.ornare@malesuadaInteger.com',44,'143',818),(45,'Jerome','tempor','Morbi@adipiscingelitCurabitur.ca',45,'144',283),(46,'Tatyana','enim,','enim@atiaculisquis.com',46,'145',101),(47,'Natalie','velit.','neque.vitae.semper@egetodioAliquam.net',47,'146',793),(48,'Ali','fermentum','eget.dictum.placerat@nonummy.co.uk',48,'147',115),(49,'Anastasia','molestie','scelerisque@vestibulumloremsit.org',49,'148',384),(50,'Kylan','tristique','ipsum.ac@utmolestiein.edu',50,'149',365),(51,'Scott','eu','Nam@etmagnis.co.uk',51,'150',492),(52,'Lael','justo','tellus.non.magna@pharetrased.co.uk',52,'151',168),(53,'Berk','nulla.','eleifend.egestas.Sed@euismodin.org',53,'152',221),(54,'Natalie','dictum','fringilla.est@laciniamattis.com',54,'153',410),(55,'Rosalyn','ultricies','enim.Etiam.gravida@gravida.com',55,'154',167),(56,'Aaron','cubilia','adipiscing.elit@ligulaconsectetuerrhoncus.edu',56,'155',529),(57,'Hashim','feugiat','dignissim.Maecenas.ornare@Seddiam.co.uk',57,'156',542),(58,'Davis','dolor','sit.amet@est.ca',58,'157',337),(59,'Melodie','libero','malesuada@orci.org',59,'158',157),(60,'Cally','enim.','auctor.odio.a@malesuada.net',60,'159',675),(61,'Ursa','egestas.','sem.ut@estacfacilisis.co.uk',61,'160',810),(62,'Octavius','metus.','ligula.Nullam.enim@musAenean.com',62,'161',795),(63,'Maggie','Curae;','fermentum@elementumsem.com',63,'162',823),(64,'Guy','dictum','congue.turpis.In@nibhPhasellusnulla.org',64,'163',463),(65,'Dalton','Sed','imperdiet@tellusSuspendissesed.com',65,'164',106),(66,'Lydia','Proin','quis.accumsan@orcisemeget.co.uk',66,'165',266),(67,'Brent','ipsum','eu.turpis.Nulla@dolorFuscefeugiat.net',67,'166',289),(68,'Madeline','vitae,','erat.in.consectetuer@nasceturridiculusmus.net',68,'167',203),(69,'Margaret','Duis','Donec.consectetuer@mollisnec.com',69,'168',484),(70,'Micah','Donec','quis.tristique@egetmollislectus.edu',70,'169',455),(71,'Judah','at,','Sed@ametorci.co.uk',71,'170',362),(72,'Harriet','Sed','tincidunt.vehicula@odioa.org',72,'171',484),(73,'Carl','id','vitae.erat@fringilla.com',73,'172',293),(74,'Karina','mauris','egestas.Sed@tellusNunclectus.com',74,'173',103),(75,'Matthew','magna','aliquam.adipiscing@etrutrumeu.org',75,'174',629),(76,'Summer','risus.','ligula.Nullam.feugiat@ac.edu',76,'175',338),(77,'Benjamin','commodo','ac.tellus@rutrummagna.org',77,'176',123),(78,'Galena','justo.','semper.egestas.urna@dictummagnaUt.org',78,'177',366),(79,'Blaine','nec','sapien.Cras@euultricessit.com',79,'178',143),(80,'Allistair','at,','nisi@urnaetarcu.ca',80,'179',399),(81,'Rebekah','vitae','eget.laoreet@nectempusmauris.com',81,'180',168),(82,'Janna','tristique','nec@lacuspede.edu',82,'181',104),(83,'Amena','magnis','aliquet.libero@Nunc.com',83,'182',826),(84,'Nita','lorem,','ipsum@consequatauctor.com',84,'183',195),(85,'Uriel','nonummy','senectus.et.netus@orcilacus.co.uk',85,'184',81),(86,'Emmanuel','erat.','non.enim@velit.com',86,'185',318),(87,'Quail','non','ipsum@ipsum.net',87,'186',577),(88,'Idola','orci,','risus@antedictummi.net',88,'187',623),(89,'Tanner','mauris','quam.a@eget.net',89,'188',265),(90,'Harper','nec','eu.nulla.at@massaIntegervitae.com',90,'189',429),(91,'Hedley','eget','turpis.Nulla@pede.net',91,'190',709),(92,'Helen','semper','lorem.lorem.luctus@vulputatelacus.com',92,'191',782),(93,'Lareina','felis','Nulla.eu.neque@lorem.co.uk',93,'192',732),(94,'Quinn','dolor','pede.Cras@tellus.co.uk',94,'193',362),(95,'Inez','dictum.','quis.diam.Pellentesque@aodio.net',95,'194',618),(96,'Daquan','magnis','sodales.purus.in@metusfacilisis.ca',96,'195',617),(97,'Harrison','Ut','in@Sed.com',97,'196',178),(98,'Erica','conubia','Duis@sodaleselit.co.uk',98,'197',305),(99,'Cyrus','ut','odio.auctor.vitae@velit.co.uk',99,'198',231),(100,'Colt','a','ultrices.posuere@Phasellusat.com',100,'199',641);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
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
