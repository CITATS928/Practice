--https://www.hackerrank.com/challenges/weather-observation-station-6/problem

--Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.



SELECT DISTINCT city FROM STATION
WHERE city LIKE 'a%' or city LIKE 'e%' or city LIKE 'i%' or city LIKE 'o%' or city LIKE 'u%';

--WHERE city REGEXP '^[aeiou]'; --REGEXP正则表达式
--WHERE LEFT(city, 1) IN ('A', 'E', 'I', 'O', 'U'); --LEFT函数