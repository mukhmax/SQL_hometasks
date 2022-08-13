INSERT INTO artists(artist_name) VALUES
	('Imagine Dragons'),
	('The Cranberries'),
	('Red Hot Chili Peppers'),
	('Metallica'),
	('Bob Dylin'),
	('Pharell Williams'),
	('Ed Sheeran'),
	('Linkin Park'),
	('Nirvana'),
	('David Guetta')
ON CONFLICT DO NOTHING;

INSERT INTO genres(genre_name) VALUES
	('Rock'),
	('Heavy Metall'),
	('Hardcore'),
	('Techno'),
	('Pop'),
	('Disco')
ON CONFLICT DO NOTHING;

INSERT INTO albums(album_name, album_year) VALUES
	('G I R L', 2014),
	('The Getaway', 2016),
	('Something Else', 2017),
	('Mercury - Act 1', 2021),
	('Californication', 1999),
	('Evolve', 2017),
	('Metallica Through The Never', 2013),
	('Lulu', 2011),
	('House of the Risin Sun', 2022),
	('=', 2021),
	('One More Light', 2017),
	('In Utero', 1993),
	('7', 2018)
ON CONFLICT DO NOTHING;

INSERT INTO tracks(track_name, duration, album_id) VALUES
	('Flames', 194, 13),
	('Like I Do', 201, 13),
	('Heart-Shaped Box', 281, 12),
	('Very Ape', 114, 12),
	('Talking To Myself', 231, 11),
	('Sorry for Now', 203, 11),
	('Bad Habits', 230, 10),
	('Stop The Rain', 203, 10),
	('Man of Constant Sorrow', 190, 9),
	('Freight Train Blues ', 138, 9),
	('Man of Constant Sorrow', 190, 9),
	('The View', 320, 8),
	('Cheat On Me', 686, 8),
	('For Whom The Bell Tolls', 279, 7),
	('One', 504, 7),
	('Believer', 204, 6),
	('Yesterday', 205, 6),
	('Parallel Universe', 269, 5),
	('Easily', 231, 5),
	('My Life', 224, 4),
	('Giants', 210, 4),
	('The Glory', 314, 3),
	('Rupture', 254, 3),
	('We Turn Red', 200, 2),
	('Go Robot', 263, 2),
	('Hunter', 240, 1),
	('Lost Queen', 476, 1)
ON CONFLICT DO NOTHING;

INSERT INTO collections(collection_name, collection_year) VALUES
	('APRES SKI PARTY', 2022),
	('chill songs that everyone knows', 2022),
	('smells like the 90s', 2022),
	('Rock Hits', 2022),
	('Aussie Camping Music', 2022),
	('The Bridge School Concerts 25th Anniversary Edition', 2011),
	('Retro essenziale', 2022),
	('Latinas Arriba', 2022),
	('Winter Acoustic 2022', 2022),
	('Thunderhits', 2019),
	('Best Of The Best', 2010),
	('Dance Pop 2022', 2022)
ON CONFLICT DO NOTHING;

INSERT INTO artists_genres(artist_id, genre_id) VALUES
	(1, 1),
	(1, 3),
	(7, 1),
	(10, 1),
	(10, 3),
	(11, 1),
	(11, 2),
	(11, 3),
	(12, 1),
	(12, 5),
	(13, 5),
	(13, 6),
	(14, 1),
	(14, 5),
	(15, 1),
	(15, 3),
	(16, 1),
	(17, 4),
	(17, 5),
	(17, 6)
ON CONFLICT DO NOTHING;

INSERT INTO artists_albums(artist_id, album_id) VALUES
	(1, 4),
	(1, 6),
	(7, 3),
	(10, 2),
	(10, 5),
	(11, 7),
	(11, 8),
	(12, 9),
	(13, 1),
	(14, 6),
	(14, 10),
	(15, 11),
	(15, 8),
	(16, 12),
	(17, 13)
ON CONFLICT DO NOTHING;

INSERT INTO tracks_collections(track_id, collection_id) VALUES
	(1, 5),
	(2, 12),
	(2, 7),
	(3, 1),
	(3, 11),
	(4, 2),
	(5, 5),
	(6, 8),
	(6, 10),
	(7, 7),
	(7, 9),
	(7, 2),
	(8, 5),
	(9, 1),
	(10, 3),
	(10, 7),
	(12, 10),
	(12, 6),
	(13, 11),
	(14, 8),
	(15, 12),
	(16, 9),
	(16, 7),
	(17, 3),
	(18, 5),
	(19, 2),
	(19, 7),
	(20, 11),
	(20, 5),
	(21, 5),
	(22, 8),
	(23, 12),
	(23, 10),
	(24, 8),
	(25, 1),
	(26, 6),
	(26, 9),
	(27, 7)
ON CONFLICT DO NOTHING;
