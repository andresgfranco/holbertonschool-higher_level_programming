-- lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server
-- display both the score and the name (in this ORDER)
-- Records should be ORDERed BY score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
