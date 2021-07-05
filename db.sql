/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - docondoor
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`docondoor` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `docondoor`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) DEFAULT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  `time` varchar(10) DEFAULT NULL,
  `amount` varchar(10) DEFAULT NULL,
  `b_status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`patient_id`,`doctor_id`,`date`,`time`,`amount`,`b_status`) values 
(1,23,17,'23','3:00','3421',NULL);

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `message` varchar(45) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) DEFAULT NULL,
  `complaint` varchar(150) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `reply` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`patient_id`,`complaint`,`date`,`time`,`reply`) values 
(1,23,'NA','23 jan','12:55','good!'),
(2,23,'nice','2021-03-30','14:41:59','pending');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `department_id` int(11) NOT NULL AUTO_INCREMENT,
  `doctor_department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`department_id`,`doctor_department`) values 
(1,'Ortho'),
(2,'Cardiology'),
(3,'Dermetology');

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `doctor_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `hospital_id` int(11) DEFAULT NULL,
  `doctor_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `doctor_qualification` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `zip_code` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `doctor` */

insert  into `doctor`(`doctor_id`,`login_id`,`department_id`,`hospital_id`,`doctor_name`,`email`,`doctor_qualification`,`phone_number`,`gender`,`zip_code`) values 
(1,17,1,NULL,'kochi','marine@lulu.com','checkbox','+97123456775','radiobutton','653432'),
(3,19,3,NULL,'dipa','dipa@123.com','checkbox','+97145726400','radiobutton','17028'),
(4,20,2,NULL,'salim','marine@lulu.com','MBBS','+97123456775','radiobutton','653432'),
(5,21,2,23,'roy','marine@lulu.com','MBBS','+97123456775','radiobutton','653432'),
(6,22,1,NULL,'binod','binu@mn','MS','+97145726400','radiobutton','17028'),
(7,23,3,NULL,'vijay','vijay@gmail.com','MD','+91568654659',NULL,NULL),
(8,24,1,9,'sabir','sabir@gmail.com','MBBS,MD','9899996645','male','456665');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) DEFAULT NULL,
  `feedback` varchar(150) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`patient_id`,`feedback`,`date`,`time`) values 
(1,0,'hshhdhs','2021-03-30','14:09:21'),
(2,23,'haiii','2021-03-30','14:11:52'),
(3,23,'very bad','2021-03-30','14:14:29'),
(4,23,'very good','2021-03-30','14:15:42'),
(5,23,'f gb','2021-03-30','14:31:45');

/*Table structure for table `hospital` */

DROP TABLE IF EXISTS `hospital`;

CREATE TABLE `hospital` (
  `hospital_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `hospital_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `zip_code` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`hospital_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `hospital` */

insert  into `hospital`(`hospital_id`,`login_id`,`hospital_name`,`place`,`email`,`phone_number`,`zip_code`) values 
(1,13,'baby ','calicut','baby@aaa.com','+97145726400','17028'),
(4,NULL,'mims','calicut','mims@gmai.com','98476583647','54763');

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `location` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `logid_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`logid_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`logid_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(9,'baby','baby','hospital'),
(12,'mims','mims','hospital'),
(14,'QWE','QWE','pharmacy'),
(17,'zxc','zxc','doctor'),
(19,'dipa','dipa','doctor'),
(20,'wer','wer','doctor'),
(21,'zxc','zxc','doctor'),
(22,'wer','wer','doctor'),
(23,'dell','dell','patient'),
(24,'sabir','sabir','doctor');

/*Table structure for table `medicine` */

DROP TABLE IF EXISTS `medicine`;

CREATE TABLE `medicine` (
  `medicine_id` int(11) NOT NULL AUTO_INCREMENT,
  `pharmacy_id` int(11) DEFAULT NULL,
  `medicine_name` varchar(50) DEFAULT NULL,
  `medicine_brand` varchar(50) DEFAULT NULL,
  `manufacture_date` varchar(30) DEFAULT NULL,
  `expiry_date` varchar(30) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `rate` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`medicine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `medicine` */

insert  into `medicine`(`medicine_id`,`pharmacy_id`,`medicine_name`,`medicine_brand`,`manufacture_date`,`expiry_date`,`quantity`,`rate`) values 
(2,14,'asd','fed','34','45','43',NULL),
(3,14,'PanaDol','Paracetamol','21/04/2020','20/04/2023','100 nos',NULL),
(4,5,'panadol','panadol','23/01/2020','23/01/2023','100nos','53');

/*Table structure for table `medicine_booking` */

DROP TABLE IF EXISTS `medicine_booking`;

CREATE TABLE `medicine_booking` (
  `medicine_booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) DEFAULT NULL,
  `medicine_id` int(11) DEFAULT NULL,
  `pharmacy_id` int(11) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  `time` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`medicine_booking_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `medicine_booking` */

/*Table structure for table `patient` */

DROP TABLE IF EXISTS `patient`;

CREATE TABLE `patient` (
  `patient_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `date_of_birth` varchar(20) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `patient` */

insert  into `patient`(`patient_id`,`login_id`,`first_name`,`last_name`,`date_of_birth`,`gender`,`email`,`phone_number`,`place`) values 
(1,23,'ham','haskar','12 03 1997','Male','hamcc@gmail.com','9696784979','nilambur'),
(2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(4,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(5,24,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `amount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`booking_id`,`status`,`amount`) values 
(1,1,'paid','5644');

/*Table structure for table `pharmacy` */

DROP TABLE IF EXISTS `pharmacy`;

CREATE TABLE `pharmacy` (
  `medicine_id` int(11) DEFAULT NULL,
  `pharmacy_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `hospital_id` int(11) DEFAULT NULL,
  `pharmacy_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `zip_code` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pharmacy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `pharmacy` */

insert  into `pharmacy`(`medicine_id`,`pharmacy_id`,`login_id`,`hospital_id`,`pharmacy_name`,`email`,`phone_number`,`latitude`,`longitude`,`place`,`zip_code`) values 
(3,1,5,NULL,'wrr','wrr@gmail.com','5594546568456','11.258753','75.780411','kr phrma','None'),
(2,3,NULL,3,'fytr','fytr@gmail.com',NULL,'11.050976','76.071098','malappuram',NULL),
(0,9,14,NULL,'ASQ','SADAS`3434','4545',NULL,NULL,'SSEDF','546'),
(NULL,10,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Table structure for table `prescription` */

DROP TABLE IF EXISTS `prescription`;

CREATE TABLE `prescription` (
  `prescription_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) DEFAULT NULL,
  `medicine_id` int(11) DEFAULT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  `consumption_amount` varchar(100) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`prescription_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `prescription` */

insert  into `prescription`(`prescription_id`,`patient_id`,`medicine_id`,`doctor_id`,`consumption_amount`,`quantity`,`date`,`time`) values 
(1,23,4,6,'3 times','3days','25/12/2020','12:00');

/*Table structure for table `time_schedule` */

DROP TABLE IF EXISTS `time_schedule`;

CREATE TABLE `time_schedule` (
  `time_schedule_id` int(11) NOT NULL AUTO_INCREMENT,
  `doctor_lid` int(11) DEFAULT NULL,
  `from_time` time DEFAULT NULL,
  `to_time` time DEFAULT NULL,
  `day` date DEFAULT NULL,
  PRIMARY KEY (`time_schedule_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `time_schedule` */

insert  into `time_schedule`(`time_schedule_id`,`doctor_lid`,`from_time`,`to_time`,`day`) values 
(1,22,'12:00:00','15:00:00','1970-01-15'),
(2,23,'14:00:00','20:00:00','2021-01-21');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
