--https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem?isFullScreen=true

--Query a count of the number of cities in CITY having a Population larger than 100,000.

SELECT COUNT(*) FROM city
WHERE population > 100000;