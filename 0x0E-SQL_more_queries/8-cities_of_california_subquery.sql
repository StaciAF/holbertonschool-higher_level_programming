-- script lists all the cities of CA in database hbtn_0d_usa
-- using MySQL server, database name will be passed
SELECT `id`, `name` FROM `cities` WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name`='California') ORDER BY id ASC;
