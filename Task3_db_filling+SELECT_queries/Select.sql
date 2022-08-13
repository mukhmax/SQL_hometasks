SELECT album_name, album_year FROM albums
WHERE album_year = 2018;

SELECT track_name, duration FROM tracks
ORDER BY duration DESC
LIMIT 1;

SELECT track_name, duration FROM tracks
WHERE duration / 60 >= 3.5

SELECT collection_name, collection_year FROM collections
WHERE collection_year BETWEEN 2018 AND 2020;

SELECT artist_name FROM artists
WHERE artist_name NOT LIKE '% %';

SELECT track_name FROM tracks
WHERE track_name LIKE 'My %' OR track_name LIKE '% My %' OR track_name LIKE '% My' OR track_name LIKE 'Мой %' OR track_name LIKE '% Мой %' OR track_name LIKE '% Мой';