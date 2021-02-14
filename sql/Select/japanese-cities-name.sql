/*
https://www.hackerrank.com/challenges/japanese-cities-name
github.com/ander758/HackerRank

Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
*/
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'JPN';