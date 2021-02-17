/*
https://www.hackerrank.com/challenges/weather-observation-station-5/problem
github.com/ander758/HackerRank

Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

Sample Output:
Utah 4
Ontario 7
*/

SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY CHAR_LENGTH(CITY), CITY ASC LIMIT 1;

SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY CHAR_LENGTH(CITY) DESC LIMIT 1;