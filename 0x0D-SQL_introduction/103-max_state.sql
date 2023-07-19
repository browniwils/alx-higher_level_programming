-- show maximum temperature of states
SELECT `state`, max(value) as `maximum_temperature` FROM `temperatures`
GROUP BY `state` ORDER BY `state`;