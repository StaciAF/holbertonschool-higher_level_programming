-- script creates a table unique_id, checks for existence, id must be unique
-- using MySQL server, database name will be passed
CREATE TABLE IF NOT EXISTS `unique_id` (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
