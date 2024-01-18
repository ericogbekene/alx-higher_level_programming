-- Select cities Subqueries
SELECT * FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
