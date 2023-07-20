-- Program lists comedy shows in hbtn_0d_tvshows.
-- and are ordered by descending in show title.
SELECT tv_genres.`title`
FROM `tv_shows` AS tv_genres
INNER JOIN `tv_show_genres` AS states
ON tv_genres.`id` = states.`show_id`
INNER JOIN `tv_genres` AS genres
ON genres.`id` = states.`genre_id`
WHERE genres.`name` = "Comedy"
ORDER BY tv_genres.`title`;