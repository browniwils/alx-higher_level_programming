-- Program lists shows in database hbtn_0d_tvshows without a genre linked sorted in asceding order by tv_shows.title and tv_show_genres.genre_id
SELECT title, genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id = show_id WHERE genre_id IS NULL ORDER BY title, genre_id;