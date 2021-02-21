/*
https://www.hackerrank.com/challenges/average-population/problem
github.com/ander758/HackerRank

Query the average population for all cities in CITY, rounded down to the nearest integer.
*/

SELECT ROUND(AVG(POPULATION), 0) FROM CITY;