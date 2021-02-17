/*
https://www.hackerrank.com/challenges/weather-observation-station-6/
github.com/ander758/HackerRank

Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
*/

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[a,e,i,o,u]';