-- script lists all records of second_table in DESC score order unless they have no name
-- using MySQL server, database name to be passed
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
