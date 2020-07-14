-- script creates database hbtn_0d_usa and table states, checks for existence with attr constraints
-- using MySQL server, database name will be passed
CREATE TABLE IF NOT EXISTS `states` (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
