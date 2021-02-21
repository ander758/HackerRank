/*
https://www.hackerrank.com/challenges/weather-observation-station-20/problem
github.com/ander758/HackerRank

A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.

https://www.geeksforgeeks.org/calculate-median-in-mysql/
*/

SET @rowindex := -1;

SELECT
   ROUND(AVG(d.LAT_N), 4) as Median
FROM
   (SELECT @rowindex:=@rowindex + 1 AS rowindex,
           STATION.LAT_N AS LAT_N
    FROM STATION
    ORDER BY STATION.LAT_N) AS d
WHERE
d.rowindex IN (FLOOR(@rowindex / 2), CEIL(@rowindex / 2));