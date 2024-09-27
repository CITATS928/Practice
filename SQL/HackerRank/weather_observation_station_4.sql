--https://www.hackerrank.com/challenges/weather-observation-station-4/problem

--Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.


SELECT COUNT(city) - COUNT(DISTINCT city) FROM station;


--note: 有些时候可能会不支持，还有性能问题和兼容性问题
--count(distinct column)会计算null值，而count(column)不会计算null值

/*
SELECT 
    (SELECT COUNT(city) FROM station) - 
    (SELECT COUNT(DISTINCT city) FROM station);
*/