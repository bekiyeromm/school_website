-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: school_db
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `about_us`
--

DROP TABLE IF EXISTS `about_us`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `about_us` (
  `id` int NOT NULL AUTO_INCREMENT,
  `school_history` text,
  `mission` text,
  `vision` text,
  `administration_staff_profiles` text,
  `contact_info` text,
  `social_media_links` text,
  `privacy` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `about_us`
--

LOCK TABLES `about_us` WRITE;
/*!40000 ALTER TABLE `about_us` DISABLE KEYS */;
INSERT INTO `about_us` VALUES (1,'Understanding that members input is valued, irrespective of amount\r\nBeing welcoming, and approachable to parents\r\nValuing the skills and insights people bring from diverse backgrounds\r\nBringing out the best in others by supporting them, and setting an inspiring example by always doing our best\r\nEmbracing and welcoming potential members from our diverse community, for example Cypriot, Greek Cypriot, English Cypriot, English, etc\r\nEnsuring strong family and community partnerships\r\n','Understanding that members input is valued, irrespective of amount\r\nBeing welcoming, and approachable to parents\r\nValuing the skills and insights people bring from diverse backgrounds\r\nBringing out the best in others by supporting them, and setting an inspiring example by always doing our best\r\nEmbracing and welcoming potential members from our diverse community, for example Cypriot, Greek Cypriot, English Cypriot, English, etc\r\nEnsuring strong family and community partnerships\r\n','Understanding that members input is valued, irrespective of amount\r\nBeing welcoming, and approachable to parents\r\nValuing the skills and insights people bring from diverse backgrounds\r\nBringing out the best in others by supporting them, and setting an inspiring example by always doing our best\r\nEmbracing and welcoming potential members from our diverse community, for example Cypriot, Greek Cypriot, English Cypriot, English, etc\r\nEnsuring strong family and community partnerships\r\n','','+251918664539','The Greek School of the Holy Trinity Greek Orthodox Community was possibly founded at the same time the Greek community was established, circa 1915.','The Greek School of the Holy Trinity Greek Orthodox Community was possibly founded at the same time the Greek community was established, circa 1920.'),(5,'blablalbla','bla bla bla','bla bla bla','beki','5878945888','swdefslkjknjsdk','kfdsalfafa\r\na\r\nfkaslf\r\nafasfnaklf');
/*!40000 ALTER TABLE `about_us` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admissions`
--

DROP TABLE IF EXISTS `admissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `process` text,
  `requirements` text,
  `application_form_link` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admissions`
--

LOCK TABLES `admissions` WRITE;
/*!40000 ALTER TABLE `admissions` DISABLE KEYS */;
INSERT INTO `admissions` VALUES (1,'Online Application','High school diploma, ID card, Transcript','http://example.com/form1'),(2,'Interview Process','Completed application, Two recommendation letters','http://example.com/form2'),(4,'gindergarton','able to learn','https://ww.example.com');
/*!40000 ALTER TABLE `admissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `announcements`
--

DROP TABLE IF EXISTS `announcements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `announcements` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `category` enum('KG','Primary','Secondary','A-Level','AS-Level','All') DEFAULT NULL,
  `posted_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `expiry_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `announcements`
--

LOCK TABLES `announcements` WRITE;
/*!40000 ALTER TABLE `announcements` DISABLE KEYS */;
INSERT INTO `announcements` VALUES (1,'class start','clsss will be start on the 04/0502024\r\nthis is to inform you that first test will academic year 2024 will begin on october 07/2024. so be ready accordinglyy','Primary','2024-09-29 12:18:09','2024-09-29 13:17:00'),(3,'Test Week','this is to inform you that first test will academic year 2024 will begin on october 07/2024. so be ready accordinglyyyyyyyyyyyyyyyy','All','2024-09-29 12:28:49','2024-10-11 15:00:00'),(15,'Vaccancy','we need a qualified software developer with  a minumum experiance of 3 years and having strong codeing skils in python','All','2024-10-01 14:42:16','2024-10-02 17:45:00'),(23,'beki','<p>&nbsp;</p>\r\n<p><span style=\"color: #2dc26b;\"><strong><span style=\"background-color: #ffffff;\">Greatings for beki :</span><em>F1-Score: The harmonic mean of precision and recall, which balances both metrics.&nbsp;</em></strong></span></p>','All','2024-10-01 20:54:29','2024-10-02 23:42:00');
/*!40000 ALTER TABLE `announcements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) NOT NULL,
  `grade` varchar(10) NOT NULL,
  `section` varchar(10) NOT NULL,
  `absence_date` date NOT NULL,
  `homeroom_teacher` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
INSERT INTO `attendance` VALUES (7,'yohana','7','7C4','2024-10-03','mignot'),(10,'Arsema not aschelew','7','7C1','2024-10-14','Mr tewodros'),(11,'Elnathan wondwosen','9','9C1','2024-10-14','ms Misrak'),(12,'Adam solomon','9','9C1','2024-10-14','ms Misrak'),(14,'betel asmelash','9','9C3','2024-10-15','Mr yohanes'),(15,'Sophia argaw','7','7C3','2024-10-14','mr bereket'),(16,'Sophia argaw','7','7C3','2024-10-15','mr bereket'),(17,'Ruth','7','7C2','2024-10-15','MR Abreham'),(18,'Edna nurlign let','7','7C2','2024-10-15','MR Abreham'),(19,'niya let','7','7C2','2024-10-15','MR Abreham'),(20,'niana let','7','7C2','2024-10-15','MR Abreham'),(21,'adula let','7','7C2','2024-10-15','MR Abreham'),(22,'Adam solomon','9','9C1','2024-10-15','ms Misrak'),(23,'anna ','9','9C1','2024-10-15','ms Misrak'),(24,'chiristina beyen','7','7C4','2024-10-17','xxx'),(25,'jazel fitsum','7','7C4','2024-10-17','yyyyy'),(26,'lea negus','7','7C4','2024-10-17','xxx'),(27,'kebron','7','7C4','2024-10-17','xxx'),(28,'mathania zekarias','7','7C4','2024-10-17','xxx'),(29,'nathan ermias','7','7C4','2024-10-17','xxx'),(30,'noel mihretab','7','7C4','2024-10-17','xxx'),(31,'yohana','7','7C4','2024-10-23','mr xx'),(32,'jazeal fitsum','7','7C4','2024-10-23','mr xx'),(33,'nathan ermias','7','7C4','2024-10-23','mr xx'),(34,'noel mihretab','7','7C4','2024-10-23','mr xx'),(35,'thomas marvin','7','7C4','2024-10-23','mr xx'),(36,'Elham Fadil','7','7C4','2024-10-23','ms mignot'),(37,'ali khalid','9','9C1','2024-10-24','ms Misrak'),(38,'amen addisu','9','9C1','2024-10-24','ms Misrak'),(39,'samuel Awash','7','7C2','2024-10-24','MR Abreham'),(40,'ammar','7','7C1','2024-10-25','Mr tewodros'),(41,'thomas marvin','7','7C4','2024-10-25','mr xx'),(42,'nathan ermias','7','7C4','2024-10-25','mr xx'),(44,'Samuel Elyas','7','7C3','2024-10-29','mr bereket'),(45,'anna ','9','9C1','2024-10-29','ms Misrak'),(50,'Jazel','7','7C4','2024-10-30','Ms mighot'),(51,'nicolas harmanis','9','9C1','2024-10-31','ms Misrak'),(52,'metmeku','7','7C4','2024-10-31','ms mignot'),(53,'maranatha','9','9C2','2024-11-04','mr bereket'),(54,'ali kha','9','9C1','2024-11-04','Mr yohanes'),(56,'aklil  permission','9','9C3','2024-11-05','Mr yohanes'),(57,'niya','7','7C2','2024-11-05','Mr tewodros'),(58,'naomi','7','7C2','2024-11-05','Mr tewodros'),(59,'niana','7','7C2','2024-11-05','Mr tewodros'),(60,'alula','7','7C2','2024-11-05','Mr tewodros'),(61,'abel','7','7C2','2024-11-05','Mr tewodros'),(62,'robel tesfaye','7','7C2','2024-11-05','Mr tewodros'),(63,'arsema  let','7','7C1','2024-11-07','Mr tewodros'),(64,'kaira  let','7','7C1','2024-11-07','Mr tewodros'),(65,'sishu','7','7C3','2024-11-07','mr bereket'),(66,'thomas marvin','7','7C4','2024-11-07','MR Abreham'),(67,'nathan ermias','7','7C4','2024-11-07','MR Abreham'),(68,'Arsema','9','9C2','2024-11-08','ms Misrak'),(69,'Arsema','9','9C2','2024-11-06','ms Misrak'),(70,'jana','7','7C1','2024-11-08','Mr tewodros');
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_information`
--

DROP TABLE IF EXISTS `contact_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact_information` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_information`
--

LOCK TABLES `contact_information` WRITE;
/*!40000 ALTER TABLE `contact_information` DISABLE KEYS */;
INSERT INTO `contact_information` VALUES (1,'Addis ababa','0918664539','bekitena34@gmail.com');
/*!40000 ALTER TABLE `contact_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `description` varchar(400) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES (9,'Annual Science Fair','Join us for our Annual Science Fair where students will showcase their innovative projects and experiments. This event provides a platform for young scientists to demonstrate their creativity and understanding of scientific principles.','2024-10-08','Main Hall, School Campus'),(10,'Championship Football Match','Come and support our school team as they compete in the Championship Football Match against the rival school. Experience the excitement, teamwork, and sportsmanship as both teams battle it out on the field. There will be food stalls and fun activities for all ages!','2024-11-15','school Football Field');
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `extracurricular_activities`
--

DROP TABLE IF EXISTS `extracurricular_activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `extracurricular_activities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` text,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `extracurricular_activities`
--

LOCK TABLES `extracurricular_activities` WRITE;
/*!40000 ALTER TABLE `extracurricular_activities` DISABLE KEYS */;
/*!40000 ALTER TABLE `extracurricular_activities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculty` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `subject` varchar(255) DEFAULT NULL,
  `biography` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
/*!40000 ALTER TABLE `faculty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_profiles`
--

DROP TABLE IF EXISTS `staff_profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_profiles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `profile_photo` varchar(255) NOT NULL,
  `experience` text NOT NULL,
  `qualification` text NOT NULL,
  `expert_areas` text NOT NULL,
  `position` varchar(255) NOT NULL,
  `contact_info` varchar(255) DEFAULT NULL,
  `social_links` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_profiles`
--

LOCK TABLES `staff_profiles` WRITE;
/*!40000 ALTER TABLE `staff_profiles` DISABLE KEYS */;
INSERT INTO `staff_profiles` VALUES (6,'Bereket Tena','static/uploads/IMG_20230411_201936_955.jpg','7 year in Teaching, 2 Year in software development ','Msc in computer Enginering and full stack application developer certified','Computer science','Teacher',NULL,NULL,'2024-09-29 18:24:48'),(10,'getachew tesfaye','static/uploads/6.jpg','20','degree','sport and coaching','teacher',NULL,NULL,'2024-11-05 06:01:06'),(11,'Eyob Habtamu','static/uploads/MG_69801.jpg','7','BA','pe','Teacher',NULL,NULL,'2024-11-07 11:23:44');
/*!40000 ALTER TABLE `staff_profiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `class_assigned` varchar(50) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'tedy','bk3tena@gmail.com','scrypt:32768:8:1$4RrGt9JwNFlBxdXV$398a5cb31dfa85fb4af515feda1f6c7ed02cc655d551533734b5bcc975c43c24ee231b1cc02721936fb93364467640090541170958409e321fade5e2e4a82380','7c2','2024-10-02 17:12:54'),(14,'Bereket Temesgen','bk3tenaa@gmail.com','scrypt:32768:8:1$QEH7XyvLFuQEvceI$8c82f927e18e678e7cf1f9e0edea0ec1026a8758cdc70016a7a07656ee93bd1ab1d03591b2a1eb80fcc4c8f96ff8e302571c0d5fb7ea2d8b26e1d67363eb132a','7c3','2024-10-30 18:09:58'),(15,'Yabsira Negese','nege1234@gmail.com','scrypt:32768:8:1$vs40xnC0i3F64kD6$c6dd36c729783d228fa062cdafc5a5f5d41897ef9976aeea44ecc0b35bd3797c47b0e0cefbd8c4d6715708d3689ca568539aa73ba13e8756c433074c98d9cba0','7c3','2024-10-30 18:10:13');
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

-- Dump completed on 2024-11-12 18:40:13
