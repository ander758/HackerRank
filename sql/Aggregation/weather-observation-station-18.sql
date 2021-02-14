/*
https://www.hackerrank.com/challenges/weather-observation-station-18/
github.com/ander758/HackerRank

Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.
 - a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
 - b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
 - c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
 - d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
Query the Manhattan Distance between points P1 and P2 and round it to a scale of 4 decimal places.
*/
SELECT ROUND(abs(MIN(LAT_N)-MAX(LAT_N)) + abs(MIN(LONG_W)-MAX(LONG_W)), 4) FROM STATION



/*
SET @a = (SELECT MIN(LAT_N) FROM STATION);
SET @b = (SELECT MIN(LONG_W) FROM STATION);
SET @c = (SELECT MAX(LAT_N) FROM STATION);
SET @d = (SELECT MAX(LONG_W) FROM STATION);

SELECT ROUND(@a-@c + @b-@d, 4) FROM STATION;
*/