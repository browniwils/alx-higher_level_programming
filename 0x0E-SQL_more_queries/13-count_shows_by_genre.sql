-- Program lists genres from the database hbtn_0d_tvshows along with the number of shows linked to each.
-- No not display genres without linked shows is shown sorted in descending order
SELECT name FROM genre, COUNT(*) AS `number_of_shows` FROM tv_genres
INNER JOIN tv_show_genres ON id = genre_id
GROUP BY name ORDER BY `number_of_shows` DESC;