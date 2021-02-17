/*
https://www.hackerrank.com/challenges/weather-observation-station-12/
github.com/ander758/HackerRank

*/

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^a,e,i,o,u]' AND CITY REGEXP '[^a,e,i,o,u]$';
