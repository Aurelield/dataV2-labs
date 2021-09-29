# ************************************************************
# Sequel Pro SQL dump
# Version 5446
#
# https://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 8.0.25)
# Database: lab_mysql
# Generation Time: 2021-09-29 11:08:03 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table cars
# ------------------------------------------------------------

DROP TABLE IF EXISTS `cars`;

CREATE TABLE `cars` (
  `VIN` varchar(20) DEFAULT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `price` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `year` char(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `cars` WRITE;
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;

INSERT INTO `cars` (`VIN`, `name`, `price`, `year`)
VALUES
	('DAM41UDN3CHU2WVF6','Volkswagen','20000','2015'),
	('3K096I98581DHSNUP','Volvo','20000','2007'),
	('ZM8G7BEUQZ97IH46V','Ford','35000','2009'),
	('DAM41UDN3CHU2WVF6','Toyota','50000','2020');

/*!40000 ALTER TABLE `cars` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table customers
# ------------------------------------------------------------

DROP TABLE IF EXISTS `customers`;

CREATE TABLE `customers` (
  `address` varchar(20) DEFAULT NULL,
  `phonenumber` varchar(20) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;

INSERT INTO `customers` (`address`, `phonenumber`, `name`)
VALUES
	('120 SW 8th St','13059077086','Abraham Lincoln'),
	('Madrid, 14','998678','Pablo Picasso'),
	('Paris','9986789','Napoléon Bonaparte'),
	('Private','09876XX89XXX7','Beyonce');

/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table invoices
# ------------------------------------------------------------

DROP TABLE IF EXISTS `invoices`;

CREATE TABLE `invoices` (
  `car` varchar(20) DEFAULT NULL,
  `price` varchar(20) DEFAULT NULL,
  `customersname` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `invoices` WRITE;
/*!40000 ALTER TABLE `invoices` DISABLE KEYS */;

INSERT INTO `invoices` (`car`, `price`, `customersname`)
VALUES
	('Volkswagen','20000','Abraham Lincoln'),
	('Volvo','20000','Pablo Picasso'),
	('Ford','35000','Napoléon Bonaparte'),
	('Toyota','50000','Beyonce');

/*!40000 ALTER TABLE `invoices` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table salespersons
# ------------------------------------------------------------

DROP TABLE IF EXISTS `salespersons`;

CREATE TABLE `salespersons` (
  `store` varchar(20) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `phonenumber` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `salespersons` WRITE;
/*!40000 ALTER TABLE `salespersons` DISABLE KEYS */;

INSERT INTO `salespersons` (`store`, `name`, `phonenumber`)
VALUES
	('Berlin','Petey Cruiser','76545890'),
	('São Paulo','Paige Turner','9865446568'),
	('Amsterdam','Walter Melon','99865678'),
	('Moscow','Anna Sthesia','99775769');

/*!40000 ALTER TABLE `salespersons` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
