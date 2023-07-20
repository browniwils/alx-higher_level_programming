-- Program lists all cities of California that is found in the database hbtn_0d_usa sorted in ascending order
USE hbtn_0d_usa;
SELECT * FROM `cities` 
WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name` = 'California')
ORDER BY  `id` ASC;