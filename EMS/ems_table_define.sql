-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: ems
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `adm_class`
--

DROP TABLE IF EXISTS `adm_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `adm_class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `major_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `adm_class_major_id_edbaa41c_fk_major_plan_id` (`major_id`),
  CONSTRAINT `adm_class_major_id_edbaa41c_fk_major_plan_id` FOREIGN KEY (`major_id`) REFERENCES `major_plan` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adm_class`
--

LOCK TABLES `adm_class` WRITE;
/*!40000 ALTER TABLE `adm_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `adm_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `announcement`
--

DROP TABLE IF EXISTS `announcement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `announcement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` longtext NOT NULL,
  `messages` longtext NOT NULL,
  `author` varchar(128) NOT NULL,
  `receiver` varchar(32) NOT NULL,
  `year` varchar(32) NOT NULL,
  `visible` tinyint(1) NOT NULL,
  `time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `announcement`
--

LOCK TABLES `announcement` WRITE;
/*!40000 ALTER TABLE `announcement` DISABLE KEYS */;
/*!40000 ALTER TABLE `announcement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add adm class',7,'add_admclass'),(26,'Can change adm class',7,'change_admclass'),(27,'Can delete adm class',7,'delete_admclass'),(28,'Can view adm class',7,'view_admclass'),(29,'Can add announcement',8,'add_announcement'),(30,'Can change announcement',8,'change_announcement'),(31,'Can delete announcement',8,'delete_announcement'),(32,'Can view announcement',8,'view_announcement'),(33,'Can add class room',9,'add_classroom'),(34,'Can change class room',9,'change_classroom'),(35,'Can delete class room',9,'delete_classroom'),(36,'Can view class room',9,'view_classroom'),(37,'Can add college',10,'add_college'),(38,'Can change college',10,'change_college'),(39,'Can delete college',10,'delete_college'),(40,'Can view college',10,'view_college'),(41,'Can add major',11,'add_major'),(42,'Can change major',11,'change_major'),(43,'Can delete major',11,'delete_major'),(44,'Can view major',11,'view_major'),(45,'Can add major plan',12,'add_majorplan'),(46,'Can change major plan',12,'change_majorplan'),(47,'Can delete major plan',12,'delete_majorplan'),(48,'Can view major plan',12,'view_majorplan'),(49,'Can add student',13,'add_student'),(50,'Can change student',13,'change_student'),(51,'Can delete student',13,'delete_student'),(52,'Can view student',13,'view_student'),(53,'Can add teacher',14,'add_teacher'),(54,'Can change teacher',14,'change_teacher'),(55,'Can delete teacher',14,'delete_teacher'),(56,'Can view teacher',14,'view_teacher'),(57,'Can add classroom_other_schedule',15,'add_classroom_other_schedule'),(58,'Can change classroom_other_schedule',15,'change_classroom_other_schedule'),(59,'Can delete classroom_other_schedule',15,'delete_classroom_other_schedule'),(60,'Can view classroom_other_schedule',15,'view_classroom_other_schedule'),(61,'Can add course',16,'add_course'),(62,'Can change course',16,'change_course'),(63,'Can delete course',16,'delete_course'),(64,'Can view course',16,'view_course'),(65,'Can add exam_ schedule',17,'add_exam_schedule'),(66,'Can change exam_ schedule',17,'change_exam_schedule'),(67,'Can delete exam_ schedule',17,'delete_exam_schedule'),(68,'Can view exam_ schedule',17,'view_exam_schedule'),(69,'Can add major courses',18,'add_majorcourses'),(70,'Can change major courses',18,'change_majorcourses'),(71,'Can delete major courses',18,'delete_majorcourses'),(72,'Can view major courses',18,'view_majorcourses'),(73,'Can add schedule_result',19,'add_schedule_result'),(74,'Can change schedule_result',19,'change_schedule_result'),(75,'Can delete schedule_result',19,'delete_schedule_result'),(76,'Can view schedule_result',19,'view_schedule_result'),(77,'Can add teacher_ schedule_result',20,'add_teacher_schedule_result'),(78,'Can change teacher_ schedule_result',20,'change_teacher_schedule_result'),(79,'Can delete teacher_ schedule_result',20,'delete_teacher_schedule_result'),(80,'Can view teacher_ schedule_result',20,'view_teacher_schedule_result'),(81,'Can add teaching',21,'add_teaching'),(82,'Can change teaching',21,'change_teaching'),(83,'Can delete teaching',21,'delete_teaching'),(84,'Can view teaching',21,'view_teaching'),(85,'Can add course selected',22,'add_courseselected'),(86,'Can change course selected',22,'change_courseselected'),(87,'Can delete course selected',22,'delete_courseselected'),(88,'Can view course selected',22,'view_courseselected'),(89,'Can add graduation project',23,'add_graduationproject'),(90,'Can change graduation project',23,'change_graduationproject'),(91,'Can delete graduation project',23,'delete_graduationproject'),(92,'Can view graduation project',23,'view_graduationproject'),(93,'Can add project document',24,'add_projectdocument'),(94,'Can change project document',24,'change_projectdocument'),(95,'Can delete project document',24,'delete_projectdocument'),(96,'Can view project document',24,'view_projectdocument'),(97,'Can add project score',25,'add_projectscore'),(98,'Can change project score',25,'change_projectscore'),(99,'Can delete project score',25,'delete_projectscore'),(100,'Can view project score',25,'view_projectscore'),(101,'Can add stu choice',26,'add_stuchoice'),(102,'Can change stu choice',26,'change_stuchoice'),(103,'Can delete stu choice',26,'delete_stuchoice'),(104,'Can view stu choice',26,'view_stuchoice'),(105,'Can add course score',27,'add_coursescore'),(106,'Can change course score',27,'change_coursescore'),(107,'Can delete course score',27,'delete_coursescore'),(108,'Can view course score',27,'view_coursescore'),(109,'Can add evaluation form',28,'add_evaluationform'),(110,'Can change evaluation form',28,'change_evaluationform'),(111,'Can delete evaluation form',28,'delete_evaluationform'),(112,'Can view evaluation form',28,'view_evaluationform'),(113,'Can add captcha store',29,'add_captchastore'),(114,'Can change captcha store',29,'change_captchastore'),(115,'Can delete captcha store',29,'delete_captchastore'),(116,'Can view captcha store',29,'view_captchastore');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `captcha_captchastore`
--

DROP TABLE IF EXISTS `captcha_captchastore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `captcha_captchastore`
--

LOCK TABLES `captcha_captchastore` WRITE;
/*!40000 ALTER TABLE `captcha_captchastore` DISABLE KEYS */;
/*!40000 ALTER TABLE `captcha_captchastore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class_room`
--

DROP TABLE IF EXISTS `class_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `class_room` (
  `crno` varchar(128) NOT NULL,
  `crtype` varchar(10) NOT NULL,
  `contain_num` int(11) NOT NULL,
  PRIMARY KEY (`crno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_room`
--

LOCK TABLES `class_room` WRITE;
/*!40000 ALTER TABLE `class_room` DISABLE KEYS */;
/*!40000 ALTER TABLE `class_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classroom_other_schedule`
--

DROP TABLE IF EXISTS `classroom_other_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `classroom_other_schedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(128) NOT NULL,
  `statement` varchar(128) NOT NULL,
  `crno_id` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Classroom_other_schedule_crno_id_c9f83eba_fk_class_room_crno` (`crno_id`),
  CONSTRAINT `Classroom_other_schedule_crno_id_c9f83eba_fk_class_room_crno` FOREIGN KEY (`crno_id`) REFERENCES `class_room` (`crno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classroom_other_schedule`
--

LOCK TABLES `classroom_other_schedule` WRITE;
/*!40000 ALTER TABLE `classroom_other_schedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `classroom_other_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `college`
--

DROP TABLE IF EXISTS `college`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `college` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `short_name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `short_name` (`short_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college`
--

LOCK TABLES `college` WRITE;
/*!40000 ALTER TABLE `college` DISABLE KEYS */;
/*!40000 ALTER TABLE `college` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cno` varchar(9) NOT NULL,
  `cname` varchar(128) NOT NULL,
  `course_type` varchar(128) DEFAULT NULL,
  `score` double NOT NULL,
  `college_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `course_cno_cname_course_type_1b785ce8_uniq` (`cno`,`cname`,`course_type`),
  KEY `course_college_id_601395bf_fk_college_id` (`college_id`),
  CONSTRAINT `course_college_id_601395bf_fk_college_id` FOREIGN KEY (`college_id`) REFERENCES `college` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course_score`
--

DROP TABLE IF EXISTS `course_score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `course_score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score` double NOT NULL,
  `commen_score` double NOT NULL,
  `final_score` double NOT NULL,
  `sno_id` int(11) NOT NULL,
  `teaching_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `course_score_teaching_id_sno_id_e656212a_uniq` (`teaching_id`,`sno_id`),
  KEY `course_score_sno_id_b4ea0ca3_fk_student_user_ptr_id` (`sno_id`),
  CONSTRAINT `course_score_sno_id_b4ea0ca3_fk_student_user_ptr_id` FOREIGN KEY (`sno_id`) REFERENCES `student` (`user_ptr_id`),
  CONSTRAINT `course_score_teaching_id_be7d1cf5_fk_teaching_table_id` FOREIGN KEY (`teaching_id`) REFERENCES `teaching_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_score`
--

LOCK TABLES `course_score` WRITE;
/*!40000 ALTER TABLE `course_score` DISABLE KEYS */;
/*!40000 ALTER TABLE `course_score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course_selected`
--

DROP TABLE IF EXISTS `course_selected`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `course_selected` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score` double NOT NULL,
  `common_score` double NOT NULL,
  `final_score` double NOT NULL,
  `is_finish` tinyint(1) NOT NULL,
  `cno_id` int(11) NOT NULL,
  `sno_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `course_selected_cno_id_3a56b2cc_fk_Teacher_Schedule_result_id` (`cno_id`),
  KEY `course_selected_sno_id_22468d70_fk_student_user_ptr_id` (`sno_id`),
  CONSTRAINT `course_selected_cno_id_3a56b2cc_fk_Teacher_Schedule_result_id` FOREIGN KEY (`cno_id`) REFERENCES `teacher_schedule_result` (`id`),
  CONSTRAINT `course_selected_sno_id_22468d70_fk_student_user_ptr_id` FOREIGN KEY (`sno_id`) REFERENCES `student` (`user_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_selected`
--

LOCK TABLES `course_selected` WRITE;
/*!40000 ALTER TABLE `course_selected` DISABLE KEYS */;
/*!40000 ALTER TABLE `course_selected` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'backstage','admclass'),(8,'backstage','announcement'),(9,'backstage','classroom'),(10,'backstage','college'),(11,'backstage','major'),(12,'backstage','majorplan'),(13,'backstage','student'),(14,'backstage','teacher'),(29,'captcha','captchastore'),(5,'contenttypes','contenttype'),(15,'courseScheduling','classroom_other_schedule'),(16,'courseScheduling','course'),(17,'courseScheduling','exam_schedule'),(18,'courseScheduling','majorcourses'),(19,'courseScheduling','schedule_result'),(20,'courseScheduling','teacher_schedule_result'),(21,'courseScheduling','teaching'),(22,'courseSelection','courseselected'),(23,'graduationManagement','graduationproject'),(24,'graduationManagement','projectdocument'),(25,'graduationManagement','projectscore'),(26,'graduationManagement','stuchoice'),(27,'scoreManagement','coursescore'),(28,'scoreManagement','evaluationform'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-05-15 03:19:28.004740'),(2,'auth','0001_initial','2019-05-15 03:19:29.809738'),(3,'admin','0001_initial','2019-05-15 03:19:30.197738'),(4,'admin','0002_logentry_remove_auto_add','2019-05-15 03:19:30.224740'),(5,'admin','0003_logentry_add_action_flag_choices','2019-05-15 03:19:30.248744'),(6,'contenttypes','0002_remove_content_type_name','2019-05-15 03:19:30.495738'),(7,'auth','0002_alter_permission_name_max_length','2019-05-15 03:19:30.749743'),(8,'auth','0003_alter_user_email_max_length','2019-05-15 03:19:30.817739'),(9,'auth','0004_alter_user_username_opts','2019-05-15 03:19:30.833749'),(10,'auth','0005_alter_user_last_login_null','2019-05-15 03:19:30.984738'),(11,'auth','0006_require_contenttypes_0002','2019-05-15 03:19:30.992740'),(12,'auth','0007_alter_validators_add_error_messages','2019-05-15 03:19:31.010748'),(13,'auth','0008_alter_user_username_max_length','2019-05-15 03:19:31.177749'),(14,'auth','0009_alter_user_last_name_max_length','2019-05-15 03:19:31.356746'),(15,'backstage','0001_initial','2019-05-15 03:19:33.304738'),(16,'captcha','0001_initial','2019-05-15 03:19:33.386745'),(17,'courseScheduling','0001_initial','2019-05-15 03:19:36.958738'),(18,'courseSelection','0001_initial','2019-05-15 03:19:37.331743'),(19,'graduationManagement','0001_initial','2019-05-15 03:19:38.865746'),(20,'scoreManagement','0001_initial','2019-05-15 03:19:40.012738'),(21,'sessions','0001_initial','2019-05-15 03:19:40.122738');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evaluation_form`
--

DROP TABLE IF EXISTS `evaluation_form`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `evaluation_form` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item1` int(11) NOT NULL,
  `item2` int(11) NOT NULL,
  `item3` int(11) NOT NULL,
  `item4` int(11) NOT NULL,
  `item5` int(11) NOT NULL,
  `item6` int(11) NOT NULL,
  `item7` int(11) NOT NULL,
  `item8` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `sum` double NOT NULL,
  `is_finish` tinyint(1) NOT NULL,
  `course_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `evaluation_form_course_id_2924b908_fk_major_courses_id` (`course_id`),
  KEY `evaluation_form_student_id_84e2b028_fk_student_user_ptr_id` (`student_id`),
  KEY `evaluation_form_teacher_id_0bcdf7c3_fk_teacher_user_ptr_id` (`teacher_id`),
  CONSTRAINT `evaluation_form_course_id_2924b908_fk_major_courses_id` FOREIGN KEY (`course_id`) REFERENCES `major_courses` (`id`),
  CONSTRAINT `evaluation_form_student_id_84e2b028_fk_student_user_ptr_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`user_ptr_id`),
  CONSTRAINT `evaluation_form_teacher_id_0bcdf7c3_fk_teacher_user_ptr_id` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`user_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_form`
--

LOCK TABLES `evaluation_form` WRITE;
/*!40000 ALTER TABLE `evaluation_form` DISABLE KEYS */;
/*!40000 ALTER TABLE `evaluation_form` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_schedule`
--

DROP TABLE IF EXISTS `exam_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `exam_schedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(128) NOT NULL,
  `sno_id` int(11) NOT NULL,
  `tno_mno_course_id` int(11) NOT NULL,
  `where_id` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Exam_Schedule_sno_id_tno_mno_course_id_e62e1c36_uniq` (`sno_id`,`tno_mno_course_id`),
  KEY `Exam_Schedule_tno_mno_course_id_1126f1c1_fk_Teacher_S` (`tno_mno_course_id`),
  KEY `Exam_Schedule_where_id_e5c447ba_fk_class_room_crno` (`where_id`),
  CONSTRAINT `Exam_Schedule_sno_id_4a55f0ee_fk_student_user_ptr_id` FOREIGN KEY (`sno_id`) REFERENCES `student` (`user_ptr_id`),
  CONSTRAINT `Exam_Schedule_tno_mno_course_id_1126f1c1_fk_Teacher_S` FOREIGN KEY (`tno_mno_course_id`) REFERENCES `teacher_schedule_result` (`id`),
  CONSTRAINT `Exam_Schedule_where_id_e5c447ba_fk_class_room_crno` FOREIGN KEY (`where_id`) REFERENCES `class_room` (`crno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_schedule`
--

LOCK TABLES `exam_schedule` WRITE;
/*!40000 ALTER TABLE `exam_schedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `exam_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `graduationproject`
--

DROP TABLE IF EXISTS `graduationproject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `graduationproject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pname` varchar(30) NOT NULL,
  `pdirection` varchar(10) NOT NULL,
  `pdifficulty` varchar(10) NOT NULL,
  `pkeywords` longtext NOT NULL,
  `pdescription` longtext NOT NULL,
  `pstu` longtext NOT NULL,
  `pstatus` int(11) NOT NULL,
  `tno_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GraduationProject_tno_id_4bb133f1_fk_teacher_user_ptr_id` (`tno_id`),
  CONSTRAINT `GraduationProject_tno_id_4bb133f1_fk_teacher_user_ptr_id` FOREIGN KEY (`tno_id`) REFERENCES `teacher` (`user_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `graduationproject`
--

LOCK TABLES `graduationproject` WRITE;
/*!40000 ALTER TABLE `graduationproject` DISABLE KEYS */;
/*!40000 ALTER TABLE `graduationproject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `major`
--

DROP TABLE IF EXISTS `major`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `major` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mno` varchar(20) NOT NULL,
  `mname` varchar(128) NOT NULL,
  `short_name` varchar(20) NOT NULL,
  `in_college_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mno` (`mno`),
  UNIQUE KEY `major_mno_mname_b42cdb8b_uniq` (`mno`,`mname`),
  KEY `major_in_college_id_19d3b0b6_fk_college_id` (`in_college_id`),
  CONSTRAINT `major_in_college_id_19d3b0b6_fk_college_id` FOREIGN KEY (`in_college_id`) REFERENCES `college` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `major`
--

LOCK TABLES `major` WRITE;
/*!40000 ALTER TABLE `major` DISABLE KEYS */;
/*!40000 ALTER TABLE `major` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `major_courses`
--

DROP TABLE IF EXISTS `major_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `major_courses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hour_total` int(11) NOT NULL,
  `hour_class` int(11) NOT NULL,
  `hour_other` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `exam_method` tinyint(1) NOT NULL,
  `cno_id` int(11) NOT NULL,
  `mno_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `major_courses_cno_id_mno_id_year_semester_18efc207_uniq` (`cno_id`,`mno_id`,`year`,`semester`),
  KEY `major_courses_mno_id_007f817c_fk_major_plan_id` (`mno_id`),
  CONSTRAINT `major_courses_cno_id_13964770_fk_course_id` FOREIGN KEY (`cno_id`) REFERENCES `course` (`id`),
  CONSTRAINT `major_courses_mno_id_007f817c_fk_major_plan_id` FOREIGN KEY (`mno_id`) REFERENCES `major_plan` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `major_courses`
--

LOCK TABLES `major_courses` WRITE;
/*!40000 ALTER TABLE `major_courses` DISABLE KEYS */;
/*!40000 ALTER TABLE `major_courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `major_plan`
--

DROP TABLE IF EXISTS `major_plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `major_plan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `cls_num` int(11) NOT NULL,
  `people_num` int(11) NOT NULL,
  `score_grad` int(11) NOT NULL,
  `stu_years` int(11) NOT NULL,
  `course_num` int(11) NOT NULL,
  `major_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `major_plan_year_major_id_e699703f_uniq` (`year`,`major_id`),
  KEY `major_plan_major_id_43ad8c43_fk_major_id` (`major_id`),
  CONSTRAINT `major_plan_major_id_43ad8c43_fk_major_id` FOREIGN KEY (`major_id`) REFERENCES `major` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `major_plan`
--

LOCK TABLES `major_plan` WRITE;
/*!40000 ALTER TABLE `major_plan` DISABLE KEYS */;
/*!40000 ALTER TABLE `major_plan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projectdocument`
--

DROP TABLE IF EXISTS `projectdocument`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `projectdocument` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schoic_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ProjectDocument_schoic_id_d715e807_fk_StuChoice_id` (`schoic_id`),
  CONSTRAINT `ProjectDocument_schoic_id_d715e807_fk_StuChoice_id` FOREIGN KEY (`schoic_id`) REFERENCES `stuchoice` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projectdocument`
--

LOCK TABLES `projectdocument` WRITE;
/*!40000 ALTER TABLE `projectdocument` DISABLE KEYS */;
/*!40000 ALTER TABLE `projectdocument` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projectscore`
--

DROP TABLE IF EXISTS `projectscore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `projectscore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grade` varchar(2) NOT NULL,
  `comments` longtext NOT NULL,
  `schoic_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ProjectScore_schoic_id_aa70fab1_fk_StuChoice_id` (`schoic_id`),
  CONSTRAINT `ProjectScore_schoic_id_aa70fab1_fk_StuChoice_id` FOREIGN KEY (`schoic_id`) REFERENCES `stuchoice` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projectscore`
--

LOCK TABLES `projectscore` WRITE;
/*!40000 ALTER TABLE `projectscore` DISABLE KEYS */;
/*!40000 ALTER TABLE `projectscore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule_result`
--

DROP TABLE IF EXISTS `schedule_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `schedule_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(128) NOT NULL,
  `sno_id` int(11) NOT NULL,
  `tno_id` int(11) NOT NULL,
  `where_id` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Schedule_result_sno_id_tno_id_where_id_time_f5fa0f13_uniq` (`sno_id`,`tno_id`,`where_id`,`time`),
  KEY `Schedule_result_tno_id_1a3d5af5_fk_teaching_table_id` (`tno_id`),
  KEY `Schedule_result_where_id_a3c1acf2_fk_class_room_crno` (`where_id`),
  CONSTRAINT `Schedule_result_sno_id_83953802_fk_student_user_ptr_id` FOREIGN KEY (`sno_id`) REFERENCES `student` (`user_ptr_id`),
  CONSTRAINT `Schedule_result_tno_id_1a3d5af5_fk_teaching_table_id` FOREIGN KEY (`tno_id`) REFERENCES `teaching_table` (`id`),
  CONSTRAINT `Schedule_result_where_id_a3c1acf2_fk_class_room_crno` FOREIGN KEY (`where_id`) REFERENCES `class_room` (`crno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule_result`
--

LOCK TABLES `schedule_result` WRITE;
/*!40000 ALTER TABLE `schedule_result` DISABLE KEYS */;
/*!40000 ALTER TABLE `schedule_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stuchoice`
--

DROP TABLE IF EXISTS `stuchoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stuchoice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) NOT NULL,
  `pno_id` int(11) NOT NULL,
  `sno_id` int(11) NOT NULL,
  `tno_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `StuChoice_sno_id_tno_id_pno_id_8444c033_uniq` (`sno_id`,`tno_id`,`pno_id`),
  KEY `StuChoice_pno_id_e77115b8_fk_GraduationProject_id` (`pno_id`),
  KEY `StuChoice_tno_id_38bacb5c_fk_teacher_user_ptr_id` (`tno_id`),
  CONSTRAINT `StuChoice_pno_id_e77115b8_fk_GraduationProject_id` FOREIGN KEY (`pno_id`) REFERENCES `graduationproject` (`id`),
  CONSTRAINT `StuChoice_sno_id_55c5d2f1_fk_student_user_ptr_id` FOREIGN KEY (`sno_id`) REFERENCES `student` (`user_ptr_id`),
  CONSTRAINT `StuChoice_tno_id_38bacb5c_fk_teacher_user_ptr_id` FOREIGN KEY (`tno_id`) REFERENCES `teacher` (`user_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stuchoice`
--

LOCK TABLES `stuchoice` WRITE;
/*!40000 ALTER TABLE `stuchoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `stuchoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `student` (
  `user_ptr_id` int(11) NOT NULL,
  `name` varchar(128) NOT NULL,
  `sex` tinyint(1) NOT NULL,
  `score_got` int(11) NOT NULL,
  `in_year` int(11) NOT NULL,
  `in_cls_id` int(11) NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  KEY `student_in_cls_id_eddc80d3_fk_adm_class_id` (`in_cls_id`),
  CONSTRAINT `student_in_cls_id_eddc80d3_fk_adm_class_id` FOREIGN KEY (`in_cls_id`) REFERENCES `adm_class` (`id`),
  CONSTRAINT `student_user_ptr_id_44865c21_fk_auth_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `teacher` (
  `user_ptr_id` int(11) NOT NULL,
  `name` varchar(128) NOT NULL,
  `sex` tinyint(1) NOT NULL,
  `in_year` int(11) NOT NULL,
  `edu_background` varchar(128) DEFAULT NULL,
  `title` varchar(128) NOT NULL,
  `description` longtext,
  `college_id` int(11) NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  KEY `teacher_college_id_e9e59ee9_fk_college_id` (`college_id`),
  CONSTRAINT `teacher_college_id_e9e59ee9_fk_college_id` FOREIGN KEY (`college_id`) REFERENCES `college` (`id`),
  CONSTRAINT `teacher_user_ptr_id_d6fc1667_fk_auth_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_schedule_result`
--

DROP TABLE IF EXISTS `teacher_schedule_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `teacher_schedule_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(128) NOT NULL,
  `current_number` int(11) NOT NULL,
  `MAX_number` int(11) NOT NULL,
  `state` varchar(128) NOT NULL,
  `tno_id` int(11) NOT NULL,
  `where_id` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Teacher_Schedule_result_tno_id_where_id_time_ecb7184e_uniq` (`tno_id`,`where_id`,`time`),
  KEY `Teacher_Schedule_result_where_id_1a8b61f8_fk_class_room_crno` (`where_id`),
  CONSTRAINT `Teacher_Schedule_result_tno_id_e09bc484_fk_teaching_table_id` FOREIGN KEY (`tno_id`) REFERENCES `teaching_table` (`id`),
  CONSTRAINT `Teacher_Schedule_result_where_id_1a8b61f8_fk_class_room_crno` FOREIGN KEY (`where_id`) REFERENCES `class_room` (`crno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_schedule_result`
--

LOCK TABLES `teacher_schedule_result` WRITE;
/*!40000 ALTER TABLE `teacher_schedule_result` DISABLE KEYS */;
/*!40000 ALTER TABLE `teacher_schedule_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teaching_table`
--

DROP TABLE IF EXISTS `teaching_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `teaching_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `weight` double NOT NULL,
  `mcno_id` int(11) NOT NULL,
  `tno_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `teaching_table_tno_id_mcno_id_9e0448d3_uniq` (`tno_id`,`mcno_id`),
  KEY `teaching_table_mcno_id_5a823ce0_fk_major_courses_id` (`mcno_id`),
  CONSTRAINT `teaching_table_mcno_id_5a823ce0_fk_major_courses_id` FOREIGN KEY (`mcno_id`) REFERENCES `major_courses` (`id`),
  CONSTRAINT `teaching_table_tno_id_89c5ebe0_fk_teacher_user_ptr_id` FOREIGN KEY (`tno_id`) REFERENCES `teacher` (`user_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teaching_table`
--

LOCK TABLES `teaching_table` WRITE;
/*!40000 ALTER TABLE `teaching_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `teaching_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-15 11:20:16
