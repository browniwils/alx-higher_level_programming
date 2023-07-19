-- shows records with a score greater or equal to 10 in the table second_table of the database hbtn_0c_0.
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;