/*
https://www.hackerrank.com/challenges/weather-observation-station-4/problem
github.com/ander758/HackerRank

Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
*/

SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION;