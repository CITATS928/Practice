--https://hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true

-- Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer. Note: CITY.CountryCode and COUNTRY.Code are matching key columns.


SELECT country.continent, FLOOR(AVG(city.population))
FROM city
INNER JOIN country
ON city.countrycode = country.code
GROUP BY country.continent

/*
note:
当同时使用aggregate function（ex: avg), select语句中未聚合的其他列必须包含在group by中
*/