--https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem

--Query the average population of all cities in CITY where District is California.

SELECT AVG(population) FROM city
WHERE district='California';
