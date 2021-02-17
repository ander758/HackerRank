/*
https://www.hackerrank.com/challenges/weather-observation-station-11/
github.com/ander758/HackerRank

Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
*/


SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^a,e,i,o,u]' OR CITY REGEXP '[^a,e,i,o,u]$';
