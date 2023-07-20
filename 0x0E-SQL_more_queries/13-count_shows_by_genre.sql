-- Program lists genres from the database hbtn_0d_tvshows along with the number of shows linked to each.
-- No not display genres without linked shows is shown sorted in descending order
SELECT genres.`name` AS `genre`, COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS genres
INNER JOIN `tv_show_genres` AS tv_genres
ON genres.`id` = tv_genres.`genre_id`
GROUP BY genres.`name`
ORDER BY `number_of_shows` DESC;