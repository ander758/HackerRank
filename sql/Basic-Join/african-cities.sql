/*
https://www.hackerrank.com/challenges/african-cities/problem
github.com/ander758/HackerRank

Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
*/

SELECT CITY.NAME FROM CITY, COUNTRY WHERE CITY.COUNTRYCODE = COUNTRY.CODE and COUNTRY.CONTINENT = 'Africa';
