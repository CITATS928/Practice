--https://www.hackerrank.com/challenges/revising-aggregations-sum/problem?isFullScreen=true

--Query the total population of all cities in CITY where District is California.

SELECT SUM(population) FROM city
WHERE district='California';