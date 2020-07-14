-- script creates database hbtn_0d_usa and table cities, checks for existence, with constraints
-- using MySQL server, database name will be passed
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities` (id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, state_id INT NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL);
