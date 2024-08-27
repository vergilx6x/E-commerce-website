-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS website_db;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'adminpwd';
GRANT ALL PRIVILEGES ON ``.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;