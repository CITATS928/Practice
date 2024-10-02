--https://www.hackerrank.com/challenges/weather-observation-station-20/problem

--A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.

WITH ordered_data AS (
    SELECT lat_n, 
           ROW_NUMBER() OVER (ORDER BY lat_n) AS row_num, 
           COUNT(*) OVER () AS total_rows
    FROM station
)
SELECT ROUND(AVG(lat_n), 4)
FROM ordered_data
WHERE row_num IN (
    FLOOR((total_rows + 1) / 2), 
    CEIL((total_rows + 1) / 2)
);
