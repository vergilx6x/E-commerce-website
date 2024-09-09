-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS website_db;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON `website_db`.* TO 'admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;