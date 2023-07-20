-- Program list shows with no comedy genre in hbtn_0d_tvshows
-- and are ordered by ascending show title.
SELECT DISTINCT `title`
FROM `tv_shows` AS tv_shows
LEFT JOIN `tv_show_genres` AS shows_genres
ON shows_genres.`show_id` = tv_shows.`id`
LEFT JOIN `tv_genres` AS genres
ON genres.`id` = shows_genres.`genre_id`
WHERE tv_shows.`title`
NOT IN (SELECT `title`
        FROM `tv_shows` AS tv_shows
        INNER JOIN `tv_show_genres` AS shows_genres
        ON shows_genres.`show_id` = tv_shows.`id`
        INNER JOIN `tv_genres` AS genres
        ON genres.`id` = shows_genres.`genre_id`
        WHERE genres.`name` = "Comedy")
ORDER BY `title`;