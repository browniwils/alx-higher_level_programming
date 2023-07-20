-- Program list all show in database  hbtn_0d_tvshows with NULL for shows without genres sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT title, genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id = show_id
ORDER BY title, genre_id;