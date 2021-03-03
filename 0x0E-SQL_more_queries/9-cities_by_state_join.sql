-- lists all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT states.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
WHERE state_id = 1
ORDER BY cities.id ASC
