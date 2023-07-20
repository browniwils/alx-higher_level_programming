-- Program lists all genres of show Dexter in hbtn_0d_tvshows
-- and are ordered by ascending genre name.
SELECT genre.`name`
FROM `tv_genres` AS genre
INNER JOIN `tv_show_genres` AS states
ON genre.`id` = states.`genre_id`
INNER JOIN `tv_shows` AS tv_genres
ON tv_genres.`id` = states.`show_id`
WHERE tv_genres.`title` = "Dexter"
ORDER BY genre.`name`;