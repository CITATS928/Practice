--https://www.hackerrank.com/challenges/revising-the-select-query-2/problem?isFullScreen=true
--Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.

select name from city where population > 120000 and countrycode ='USA';