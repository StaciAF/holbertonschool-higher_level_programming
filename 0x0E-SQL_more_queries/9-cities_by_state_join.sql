-- script lists all cities contained in hbtn_0d_usa
-- using MySQL server, database name will be passed
SELECT cit.`id`, cit.`name`, st.`name` FROM `cities` AS cit INNER JOIN `states` AS st ON cit.`state_id` = st.`id` ORDER BY cit.`id`;
