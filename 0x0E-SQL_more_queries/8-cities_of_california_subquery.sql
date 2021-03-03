-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- The states table contains only one record WHERE name = California (but the id can be different, as per the example)
-- Results must be sorted in ascending ORDER BY cities.id
-- The database name will be passed as an argument of the mysql command
SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY cities.id ASC
