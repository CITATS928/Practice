--https://www.hackerrank.com/challenges/weather-observation-station-18/problem

/*
Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.

a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
Query the Manhattan Distance between points P1 and P2 and round it to a scale of  decimal places.
*/

--Manhattan Distance: p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|

SELECT ROUND(ABS(MIN(lat_n)-MAX(lat_n))+ABS(MIN(long_w)-MAX(long_w)),4) FROM station;