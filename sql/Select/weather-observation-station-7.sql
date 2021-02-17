/*
https://www.hackerrank.com/challenges/weather-observation-station-7/
github.com/ander758/HackerRank

Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
*/

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[a,e,i,o,u]$';