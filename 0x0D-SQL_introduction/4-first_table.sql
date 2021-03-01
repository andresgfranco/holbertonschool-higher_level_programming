-- creates a table called first_table in the current database in your MySQL server
-- first_table description: id INT, name VARCHAR(256)
-- database name will be passed as an argument of the mysql command
-- if the table first_table already exists, the script should not fail
CREATE TABLE IF NOT EXISTS first_table(
	`id` int,
	`name` varchar(256)
);
