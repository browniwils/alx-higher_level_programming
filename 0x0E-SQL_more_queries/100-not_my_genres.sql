-- Program lists genres of hbtn_0d_tvshows
-- not linked to the show Dexter.
-- and are sorted by ascending genre name.
SELECT DISTINCT `name`
FROM `tv_genres` AS genres
INNER JOIN `tv_show_genres` AS states
ON genres.`id` = states.`genre_id`
INNER JOIN `tv_shows` AS t
ON states.`show_id` = t.`id`
WHERE genres.`name` NOT IN
    (SELECT `name`FROM `tv_genres` 
        AS genres INNER JOIN `tv_show_genres` AS states ON genres.`id` = states.`genre_id`
        INNER JOIN `tv_shows` AS tv_shows
        ON states.`show_id` = tv_shows.`id`
        WHERE tv_shows.`title` = "Dexter")
ORDER BY genres.`name`;