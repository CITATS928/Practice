/*
https://www.hackerrank.com/challenges/weather-observation-station-5/problem

Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

Sample Input
For example, CITY has four entries: DEF, ABC, PQRS and WXY.

Sample Output
ABC 3
PQRS 4
*/

(SELECT city, LENGTH(city) FROM station
WHERE LENGTH(city) = (SELECT MIN(LENGTH(city)) FROM station)
ORDER BY city ASC
LIMIT 1)
UNION
(SELECT city, LENGTH(city) FROM station
WHERE LENGTH(city) = (SELECT MAX(LENGTH(city)) FROM station)
ORDER BY city ASC
LIMIT 1);