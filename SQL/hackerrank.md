SELECT DISTINCT(CITY)  FROM STATION;

SELECT COUNT (CITY) - COUNT (DISTINCT(CITY)) FROM STATION;

SELECT CITY FROM STATION WHERE lower(SUBSTR(CITY,1,1)) IN ('a','e','i','o','u');


