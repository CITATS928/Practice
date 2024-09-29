--https://www.hackerrank.com/challenges/weather-observation-station-15/problem

--Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than . Round your answer to  decimal places.

SELECT ROUND(LONG_W,4) FROM station
WHERE LAT_N<137.2345
ORDER BY LAT_N DESC
LIMIT 1;

/*
ANother way

SELECT ROUND(LONG_W,4) FROM station
WHERE LAT_N = (
    SELECT MAX(LAT_N) FROM station
    WHERE LAT_N<137.2345
)
比起使用order by和limit，使用Max的子查询更高效
更加整洁和逻辑清晰
*/