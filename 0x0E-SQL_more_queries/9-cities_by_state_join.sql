-- A ript that lists all cities contained in the database hbtn_0d_usa.
    -- Each record should display: cities.id - cities.name - states.name
    -- Results must be sorted in ascending order by cities.id
    -- You can use only one SELECT statement
    -- The database name will be passed as an argument of the mysql command

SELECT cities.id, cities.name, states.name
From cities
JOIN states AS s
WHERE cities.state_id = s.id
ORDER BY cities.id ASC;
