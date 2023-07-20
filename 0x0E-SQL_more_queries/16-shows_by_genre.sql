-- Program lists shows and genres linked to the show from the hbtn_0d_tvshows.
-- and are ordered by ascending show title and genre name.
SELECT tv_genres.`title`, genres.`name`
FROM `tv_shows` AS tv_genres
LEFT JOIN `tv_show_genres` AS states
ON tv_genres.`id` = states.`show_id`
LEFT JOIN `tv_genres` AS genres
ON states.`genre_id` = genres.`id`
ORDER BY tv_genres.`title`, genres.`name`;