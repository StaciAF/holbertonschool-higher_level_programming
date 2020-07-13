-- script lists all records with a score >=10 in second_table from hbtn_0c_0
-- using MySQL server, database name to be passed
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
