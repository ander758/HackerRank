/*
https://www.hackerrank.com/challenges/weather-observation-station-17/
github.com/ander758/HackerRank

Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780. Round your answer to 4 decimal places.
*/

SET @variable = (SELECT MIN(LAT_N) FROM STATION WHERE LAT_N > 38.7780);
SELECT ROUND(LONG_W, 4) FROM STATION WHERE LAT_N = @variable;