--https://www.hackerrank.com/challenges/asian-population/problem?isFullScreen=true

-- Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

SELECT SUM(city.population)
FROM city
inner join country
ON city.countrycode = country.code
WHERE continent='Asia';


/*
Improved version

使用别名提高可读性
简化查询：表名可能较长，使用别名会让查询更加简洁。
提高可读性：当涉及更多的列或多个表时，别名能够让代码更具可读性。

SELECT SUM(c.population)
FROM city c
INNER JOIN country cn
ON c.countrycode = cn.code
WHERE cn.continent = 'Asia';

*/