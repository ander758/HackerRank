/*
https://www.hackerrank.com/challenges/revising-aggregations-sum/problem
github.com/ander758/HackerRank

Query the total population of all cities in CITY where District is California.
*/

SELECT SUM(POPULATION) FROM CITY WHERE DISTRICT = 'California';