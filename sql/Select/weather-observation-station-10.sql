/*
https://www.hackerrank.com/challenges/weather-observation-station-10/
github.com/ander758/HackerRank

Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
*/

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[^a,e,i,o,u]$';