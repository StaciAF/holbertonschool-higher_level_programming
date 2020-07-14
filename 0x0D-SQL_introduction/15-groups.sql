-- script lits the number of records with same score in second_table of database hbtn_0c_0
-- using MySQL server, database name to be passed
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
