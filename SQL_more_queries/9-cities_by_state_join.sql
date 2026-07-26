-- script that lists all cities
SELECT
	cities.id AS city_id,
	cities.name AS city_name,
	states.name AS state_name
	FROM cities
	INNER JOIN states ON cities.state_id = sstates.id
	ORDER BY cities.id ASC;
