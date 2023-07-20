-- Program  lists all shows in hbtn_0d_tvshows that have at least one genre linked
SELECT states.`title`, genres.`genre_id`
FROM `tv_shows` AS states
INNER JOIN `tv_show_genres` AS genres
ON states.`id` = genres.`show_id`
ORDER BY states.`title`, genres.`genre_id`;