/*
https://www.hackerrank.com/challenges/weather-observation-station-3
github.com/ander758/HackerRank

Query a list of CITY names from STATION for cities that have an even ID number.
Print the results in any order, but exclude duplicates from the answer.
*/

SELECT DISTINCT CITY FROM STATION WHERE (ID%2) = 0;