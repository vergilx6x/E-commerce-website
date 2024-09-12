-- MySQL dump 10.13  Distrib 5.7.42, for Linux (x86_64)
--
-- Host: localhost    Database: website_db
-- ------------------------------------------------------
-- Server version	5.7.42-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cart_items`
--

DROP TABLE IF EXISTS `cart_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cart_items` (
  `cart_id` varchar(128) DEFAULT NULL,
  `product_id` varchar(128) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_id` (`cart_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `cart_items_ibfk_1` FOREIGN KEY (`cart_id`) REFERENCES `carts` (`id`),
  CONSTRAINT `cart_items_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_items`
--

LOCK TABLES `cart_items` WRITE;
/*!40000 ALTER TABLE `cart_items` DISABLE KEYS */;
INSERT INTO `cart_items` VALUES (NULL,'0a775b25-9db1-466c-8038-009b641425b8',1,'22e9a879-79f8-4db9-992d-72420a0a5be0','2024-09-10 18:25:27','2024-09-10 18:25:27',NULL),(NULL,'06b077f4-2534-4638-9c29-77b468cb6417',1,'41d69d0a-4f92-48eb-97a6-370949302fd6','2024-09-10 18:20:59','2024-09-10 18:20:59',NULL),(NULL,'07f2a82a-399a-4236-b879-287f18181c4a',1,'96071026-d143-497a-aa33-3d53232a1bc8','2024-09-10 18:22:31','2024-09-10 18:22:31',NULL),(NULL,'06b077f4-2534-4638-9c29-77b468cb6417',1,'988d01ff-6d39-47bd-86dd-dc2caf498ba1','2024-09-10 19:40:24','2024-09-10 19:40:24',NULL);
/*!40000 ALTER TABLE `cart_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carts`
--

DROP TABLE IF EXISTS `carts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carts` (
  `user_id` varchar(128) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `carts_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carts`
--

LOCK TABLES `carts` WRITE;
/*!40000 ALTER TABLE `carts` DISABLE KEYS */;
INSERT INTO `carts` VALUES ('c5bffc84-39fd-4cc1-944e-c66efa4eba86','6e4631c4-2f62-4343-8d02-0af94564716b','2024-09-11 12:02:31','2024-09-11 12:02:31',NULL);
/*!40000 ALTER TABLE `carts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `name` varchar(32) NOT NULL,
  `description` text,
  `image_url` varchar(128) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES ('Electronics','Devices and gadgets','static/images/electronics.jpg','232dd0d6-4479-4410-a203-dc0e2e16ee6e','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Sports','Sports equipment and apparel','static/images/sports.jpg','24f3d60d-a96c-47e0-9ede-db1633c689f1','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Home & Kitchen','Furniture, appliances, and more','static/images/home_kitchen.jpg','5b92520d-eba4-4047-b938-5a0a90476083','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Automotive','Car parts and accessories','static/images/automotive.jpg','61c07310-18ae-4387-b428-e98bb1e2a842','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Clothing','Apparel and accessories','static/images/clothing.jpg','66e2352a-aec9-4da9-a5eb-46d4b9922125','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Beauty','Cosmetics, skincare, and grooming products','static/images/beauty.jpg','768253ed-35fd-44c3-af87-b873b514c93e','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Toys','Fun and educational toys for all ages','static/images/toys.jpg','d1118d4f-2752-470b-bf0b-0008a2532a5c','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Books','Various genres of books','static/images/books.jpg','f5b4e7d4-d734-4b0c-b9aa-06ddcfd86af7','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL);
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favorites`
--

DROP TABLE IF EXISTS `favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `favorites` (
  `user_id` varchar(60) NOT NULL,
  `product_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `favorites_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `favorites_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorites`
--

LOCK TABLES `favorites` WRITE;
/*!40000 ALTER TABLE `favorites` DISABLE KEYS */;
INSERT INTO `favorites` VALUES ('c5bffc84-39fd-4cc1-944e-c66efa4eba86','274d2e19-5e49-4c76-a2d6-f32413ad63dc','0a74cc0d-459f-4200-a59c-74f86d819b36','2024-09-12 14:54:32','2024-09-12 14:54:32',NULL);
/*!40000 ALTER TABLE `favorites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_items`
--

DROP TABLE IF EXISTS `order_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_items` (
  `order_id` varchar(128) DEFAULT NULL,
  `product_id` varchar(128) DEFAULT NULL,
  `price` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  CONSTRAINT `order_items_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_items`
--

LOCK TABLES `order_items` WRITE;
/*!40000 ALTER TABLE `order_items` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `user_id` varchar(128) DEFAULT NULL,
  `status` varchar(64) NOT NULL,
  `total_amount` int(11) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `name` varchar(64) NOT NULL,
  `price` int(11) NOT NULL,
  `description` text,
  `quantity` int(11) NOT NULL,
  `category_id` varchar(128) DEFAULT NULL,
  `image_url` varchar(128) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('Blender',60,'Powerful blender for smoothies and more',60,'5b92520d-eba4-4047-b938-5a0a90476083','/static/uploads/06b077f4-2534-4638-9c29-77b468cb6417.jpg','06b077f4-2534-4638-9c29-77b468cb6417','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Smartphone',699,'Latest model smartphone with high resolution display',50,'232dd0d6-4479-4410-a203-dc0e2e16ee6e','/static/uploads/07f2a82a-399a-4236-b879-287f18181c4a.png','07f2a82a-399a-4236-b879-287f18181c4a','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('The Great Gatsby',15,'Classic novel by F. Scott Fitzgerald',200,'f5b4e7d4-d734-4b0c-b9aa-06ddcfd86af7','/static/uploads/0a775b25-9db1-466c-8038-009b641425b8.jpg','0a775b25-9db1-466c-8038-009b641425b8','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Sleeping Bag',60,'Comfortable sleeping bag for camping trips',30,'24f3d60d-a96c-47e0-9ede-db1633c689f1','/static/uploads/1000c297-e78c-48aa-8b14-21054be3572c.jpg','1000c297-e78c-48aa-8b14-21054be3572c','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Yoga Mat',25,'Non-slip yoga mat for your workout sessions',90,'24f3d60d-a96c-47e0-9ede-db1633c689f1','/static/uploads/16bd444d-102b-4050-a646-c6377d74c402.jpg','16bd444d-102b-4050-a646-c6377d74c402','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Puzzle Set',35,'Challenging puzzles for all ages',70,'d1118d4f-2752-470b-bf0b-0008a2532a5c','/static/uploads/18e764bc-08e4-436d-9de8-b1c8e2ab82fd.jpg','18e764bc-08e4-436d-9de8-b1c8e2ab82fd','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Running Shoes',89,'Durable and comfortable running shoes',70,'66e2352a-aec9-4da9-a5eb-46d4b9922125','/static/uploads/217a8b3b-554b-463c-bf2e-95b246b1bf8e.png','217a8b3b-554b-463c-bf2e-95b246b1bf8e','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('iPhone 14 Pro Max',1099,'The latest iPhone with a 6.7-inch Super Retina XDR display, an A16 Bionic chip, and an advanced camera system.',100,'232dd0d6-4479-4410-a203-dc0e2e16ee6e','/static/uploads/274d2e19-5e49-4c76-a2d6-f32413ad63dc.jpg','274d2e19-5e49-4c76-a2d6-f32413ad63dc','2024-09-11 17:06:52','2024-09-11 17:06:52',NULL),('Shampoo',15,'Gentle shampoo for everyday use',120,'768253ed-35fd-44c3-af87-b873b514c93e','/static/uploads/56005540-72bc-4e58-896d-82107a381844.png','56005540-72bc-4e58-896d-82107a381844','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Motor Oil',30,'High-quality motor oil for smooth engine performance',80,'61c07310-18ae-4387-b428-e98bb1e2a842','/static/uploads/5848f29f-17b6-4345-b53f-9826c08c4019.png','5848f29f-17b6-4345-b53f-9826c08c4019','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Tablet',299,'High-resolution tablet with a sleek design',25,'232dd0d6-4479-4410-a203-dc0e2e16ee6e','/static/uploads/5c2ba9c9-f906-448c-af13-9e18b32e3fc5.jpg','5c2ba9c9-f906-448c-af13-9e18b32e3fc5','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Cookbook',25,'Collection of recipes for various cuisines',100,'f5b4e7d4-d734-4b0c-b9aa-06ddcfd86af7','/static/uploads/666dac28-0f54-40d0-92a7-dcb14463d87a.png','666dac28-0f54-40d0-92a7-dcb14463d87a','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Building Blocks Set',45,'Creative building blocks for kids',150,'d1118d4f-2752-470b-bf0b-0008a2532a5c','/static/uploads/6945de21-f547-4ef6-9ecc-00d008201c41.jpg','6945de21-f547-4ef6-9ecc-00d008201c41','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Car Seat Cover',35,'Protective car seat cover with universal fit',55,'61c07310-18ae-4387-b428-e98bb1e2a842','/static/uploads/7410f6d7-2f27-48c0-a588-70f2704d9989.png','7410f6d7-2f27-48c0-a588-70f2704d9989','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Hair Dryer',60,'High-performance hair dryer with multiple settings',45,'768253ed-35fd-44c3-af87-b873b514c93e','/static/uploads/765acee4-a295-4f02-9b14-d7e636d07264.jpg','765acee4-a295-4f02-9b14-d7e636d07264','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Toaster',40,'Four-slice toaster with adjustable browning control',55,'5b92520d-eba4-4047-b938-5a0a90476083','/static/uploads/7c4cb478-6c42-43b2-95a3-c5b45efead06.png','7c4cb478-6c42-43b2-95a3-c5b45efead06','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Dollhouse',150,'Wooden dollhouse with furniture',40,'d1118d4f-2752-470b-bf0b-0008a2532a5c','/static/uploads/7e6b9c25-f119-416c-a3a5-863d5d9750af.png','7e6b9c25-f119-416c-a3a5-863d5d9750af','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Car Vacuum Cleaner',75,'Portable vacuum cleaner for cars',40,'61c07310-18ae-4387-b428-e98bb1e2a842','/static/uploads/819acf66-0397-40cb-a6ee-d47b762972be.jpg','819acf66-0397-40cb-a6ee-d47b762972be','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Moisturizer',25,'Hydrating moisturizer for all skin types',100,'768253ed-35fd-44c3-af87-b873b514c93e','/static/uploads/820d3166-99d7-4e3f-9f99-fa35344bc895.png','820d3166-99d7-4e3f-9f99-fa35344bc895','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Laptop',999,'High-performance laptop with fast processor',30,'232dd0d6-4479-4410-a203-dc0e2e16ee6e','/static/uploads/ad9d93cf-d85e-45fa-b8ef-8a4dade85c61.jpg','ad9d93cf-d85e-45fa-b8ef-8a4dade85c61','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Basketball',30,'Official size basketball for outdoor play',50,'24f3d60d-a96c-47e0-9ede-db1633c689f1','/static/uploads/b4eda1d1-a2f7-4502-bab2-46abc31b21d4.png','b4eda1d1-a2f7-4502-bab2-46abc31b21d4','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('1984',18,'Dystopian novel by George Orwell',180,'f5b4e7d4-d734-4b0c-b9aa-06ddcfd86af7','/static/uploads/b6ff23bc-170d-49dc-a7ff-75c50376af54.jpg','b6ff23bc-170d-49dc-a7ff-75c50376af54','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Microwave Oven',150,'Compact microwave oven with multiple settings',35,'5b92520d-eba4-4047-b938-5a0a90476083','/static/uploads/b77156a8-fcec-4679-8092-9a1088c4f222.jpg','b77156a8-fcec-4679-8092-9a1088c4f222','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Tent',120,'Spacious camping tent with easy setup',20,'24f3d60d-a96c-47e0-9ede-db1633c689f1','/static/uploads/ba1dcb23-29d6-4931-a258-b32620d39914.jpg','ba1dcb23-29d6-4931-a258-b32620d39914','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('T-Shirt',19,'Comfortable cotton t-shirt in various colors',100,'66e2352a-aec9-4da9-a5eb-46d4b9922125','/static/uploads/bb3c1c85-bfa9-4946-a4e3-f871e98f26d8.png','bb3c1c85-bfa9-4946-a4e3-f871e98f26d8','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Car Battery',120,'Reliable car battery for most vehicles',60,'61c07310-18ae-4387-b428-e98bb1e2a842','/static/uploads/bf442181-dd42-406d-b807-714f7c05b2fa.jpeg','bf442181-dd42-406d-b807-714f7c05b2fa','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Coffee Maker',120,'Automatic coffee maker with programmable settings',40,'5b92520d-eba4-4047-b938-5a0a90476083','/static/uploads/c2a44891-30f2-45d0-9340-661d5bc5a305.jpg','c2a44891-30f2-45d0-9340-661d5bc5a305','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Jacket',89,'Warm and stylish winter jacket',60,'66e2352a-aec9-4da9-a5eb-46d4b9922125','/static/uploads/c5752823-ac7a-4783-b22c-89de79fec9de.jpg','c5752823-ac7a-4783-b22c-89de79fec9de','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Sunglasses',45,'Fashionable sunglasses with UV protection',80,'66e2352a-aec9-4da9-a5eb-46d4b9922125','/static/uploads/c58095ac-a44d-4400-8baf-9a72ad27aad8.jpg','c58095ac-a44d-4400-8baf-9a72ad27aad8','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Face Cream',40,'Nourishing face cream for all skin types',90,'768253ed-35fd-44c3-af87-b873b514c93e','/static/uploads/ee017a6a-3a65-434d-b679-b482550544bf.jpg','ee017a6a-3a65-434d-b679-b482550544bf','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL),('Smart Watch',199,'Stylish smartwatch with health tracking features',40,'232dd0d6-4479-4410-a203-dc0e2e16ee6e','/static/uploads/f378732f-242c-46d8-b8a4-f97d8a5b27f2.jpg','f378732f-242c-46d8-b8a4-f97d8a5b27f2','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `username` varchar(64) NOT NULL,
  `first_name` varchar(128) DEFAULT NULL,
  `last_name` varchar(128) DEFAULT NULL,
  `phone_number` varchar(128) DEFAULT NULL,
  `country` varchar(128) DEFAULT NULL,
  `city` varchar(128) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `postal_code` varchar(60) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `is_admin` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('dan.black@example.com','hashed_password','danblack','Dan','Black','555-876-5432','USA','Austin','303 Cedar Street','73301','10080314-5c86-4569-8363-8dfe81cbc7c1','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL,NULL,0),('jane.doe@example.com','hashed_password','janedoe','Jane','Doe','987-654-3210','USA','Los Angeles','456 Oak Street','90001','11312d9d-cd99-422a-a224-51fd91a48974','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL,NULL,0),('alice.smith@example.com','hashed_password','alicesmith','Alice','Smith','555-123-4567','USA','Chicago','789 Maple Avenue','60601','22c1c3ee-c2ff-441d-97c8-73b46d50032e','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL,NULL,0),('emma.green@example.com','hashed_password','emmagreen','Emma','Green','555-345-6789','USA','Boston','404 Elm Street','02101','70e8eee6-282d-41f0-82f0-d10522236243','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL,NULL,0),('carol.white@example.com','hashed_password','carolwhite','Carol','White','555-234-5678','USA','Seattle','202 Birch Road','98101','880046d0-d7b5-4c5d-8caa-e8f5cac5f7b3','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL,NULL,0),('john.doe@example.com','pbkdf2:sha256:600000$KMrn7D7lAWbqJslT$c1a22b99081172e1a69ecf800132f5a534fca6d33168813e3a4971c87ec1e712','johndoe','John','Doe','123-456-7890','USA','New York','123 Elm Street','10001','c379cdd4-2421-4b1d-9354-ada7d9fd41e2','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL,NULL,0),('test__email@test.com','pbkdf2:sha256:600000$oBY65Tlt6laOxzl4$89a6ef07bc54084222101c00d7ea0c5cc9d261c777f97a50c8cd692c3cd431d7','mohamed_amine','None','None','None','None','None','None','None','c5bffc84-39fd-4cc1-944e-c66efa4eba86','2024-09-11 11:50:23','2024-09-11 11:50:23',NULL,'/static/uploads/c5bffc84-39fd-4cc1-944e-c66efa4eba86.jpg',1),('bob.jones@example.com','hashed_password','bobjones','Bob','Jones','555-987-6543','USA','San Francisco','101 Pine Street','94101','cde3473b-1914-4e13-8833-fa2e88c4799d','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL,NULL,0),('frank.kim@example.com','hashed_password','frankkim','Frank','Kim','555-654-3210','USA','Miami','505 Oak Avenue','33101','f8431ddc-f0fe-4380-8f5f-9d840bf4b893','2024-09-10 18:03:34','2024-09-10 18:03:34',NULL,NULL,0);
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

-- Dump completed on 2024-09-12 15:56:12
