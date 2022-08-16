SELECT genre_id, genre_name, COUNT(g.genre_name) FROM artists_genres ag 
JOIN genres g ON ag.genre_id = g.id
GROUP BY genre_id, genre_name
ORDER BY COUNT(*) DESC;

SELECT COUNT(track_name) FROM tracks t
JOIN albums a ON t.album_id = a.id
WHERE album_year BETWEEN 2019 AND 2020

SELECT album_id, AVG(duration) FROM tracks t
JOIN albums a ON t.album_id = a.id
GROUP BY album_id
ORDER BY AVG(duration);

SELECT artist_name FROM artists
WHERE NOT artist_name IN (SELECT artist_name FROM artists a 
JOIN artists_albums aa ON a.id = aa.artist_id
JOIN albums al ON aa.album_id = al.id
WHERE album_year = 2020);

SELECT DISTINCT collection_name  FROM collections c
JOIN tracks_collections tc ON c.id = tc.collection_id
JOIN tracks t ON tc.track_id = t.id 
JOIN albums a ON t.album_id = a.id
JOIN artists_albums aa ON a.id = aa.album_id
JOIN artists a2 ON aa.artist_id = a2.id
WHERE artist_name = 'Ed Sheeran';

SELECT album_name, COUNT(genre_id)  FROM albums a
JOIN artists_albums aa ON a.id = aa.album_id
JOIN artists a2 ON aa.artist_id = a2.id
JOIN artists_genres ag ON a2.id = ag.artist_id
GROUP BY album_name
HAVING COUNT(genre_id) > 1;

SELECT track_name FROM tracks
WHERE NOT track_name IN (
SELECT track_name FROM tracks t
JOIN tracks_collections tc ON t.id = tc.track_id
);

SELECT artist_name FROM artists a 
JOIN artists_albums aa ON a.id = aa.artist_id 
JOIN albums a2 ON aa.album_id = a2.id 
JOIN tracks t ON a2.id = t.album_id 
WHERE duration IN (
SELECT MIN(duration) FROM tracks
);

SELECT album_name, COUNT(t.id) AS songs_number FROM albums a 
JOIN tracks t ON a.id = t.album_id
GROUP BY album_name
HAVING COUNT(t.id) =  (
SELECT MIN(songs_number) FROM (
SELECT album_name, COUNT(t.id) AS songs_number FROM albums a 
JOIN tracks t ON a.id = t.album_id
GROUP BY album_name) AS lst)
