--https://www.hackerrank.com/challenges/weather-observation-station-14/problem

--Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to 4 decimal places.


SELECT ROUND(lat_N,4) FROM station
WHERE lat_N<137.2345
ORDER BY lat_N DESC
LIMIT 1;