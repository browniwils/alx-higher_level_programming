-- Program list shows from hbtn_0d_tvshows_rate by their rating
-- and are ordered by descending rating.
SELECT `title`, SUM(`rate`) AS `rating`
FROM `tv_shows` AS tv_shows
INNER JOIN `tv_show_ratings` AS ratings
ON tv_shows.`id` = ratings.`show_id`
GROUP BY `title`
ORDER BY `rating` DESC;