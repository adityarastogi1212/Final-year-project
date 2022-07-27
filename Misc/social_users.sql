-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: social
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) DEFAULT NULL,
  `lname` varchar(80) DEFAULT NULL,
  `pwd` varchar(120) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `tele` varchar(12) DEFAULT NULL,
  `city` varchar(200) DEFAULT NULL,
  `zip` varchar(120) DEFAULT NULL,
  `gen` varchar(120) DEFAULT NULL,
  `addr` varchar(120) DEFAULT NULL,
  `profilepic` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (7,'Aditya','Rastogi','12345','adityarastogi1212@gmail.com','3545641516','Bengaluru','560060','Male','Uttrahalli-Kengri main road',NULL),(8,'amit','amit','123','amit@gmail.com','1234567890','amit','560060','Male','amit',NULL),(9,'bharadawaj','bharadawaj','123','bharadawaj@gmail.com','3545641516','bharadawaj','800013','Male','bharadawaj',NULL),(10,'jyothi','l','123','jyothi@gmail.com','1234567890','jyothi','123456','Female','jyothi',NULL),(11,'ddemo','demo','123','demo@gmail.com','1234567890','demo','123456','Female','demo',NULL),(12,'Arpit','Srivastava','123','arpit@gmail.com','1234567890','Varanasi','123456','Male','Varanasi',NULL),(13,'jayesh','kumar','123','jayesh@gmail.com','3545641516','goa','345678','Male','goa',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-27 14:40:24
