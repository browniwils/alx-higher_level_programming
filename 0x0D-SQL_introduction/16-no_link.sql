-- List and order records in the second_table
-- which have a blank name in descending order
SELECT `score`, `name` FROM `second_table`
WHERE `name` != "" ORDER BY `score` DESC