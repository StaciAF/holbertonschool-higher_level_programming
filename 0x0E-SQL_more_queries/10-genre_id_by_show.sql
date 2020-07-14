-- scripts lists all shows that have at least one linked genre
-- using MySQL server, database name will be passed
SELECT shows.`title`, gen.`genre_id` FROM `tv_shows` AS shows INNER JOIN `tv_show_genres` AS gen ON shows.`id`= gen.`show_id` ORDER BY shows.`title`, gen.`genre_id` ASC;
