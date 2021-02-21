/*
https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem
github.com/ander758/HackerRank

Query the average population of all cities in CITY where District is California.
*/

SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = 'California';