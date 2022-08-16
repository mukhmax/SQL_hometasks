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
	('The Getaway', 2019),
	('Something Else', 2017),
	('Mercury - Act 1', 2020),
	('Californication', 1999),
	('Evolve', 2017),
	('Metallica Through The Never', 2013),
	('Lulu', 2011),
	('House of the Risin Sun', 2019),
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
	('Wrecked', 244, 4),
	('Porcelain', 163, 5),
	('Nothing Else Matters', 441, 7),
	('Gospel Plow', 107, 9),
	('Halfway Right ', 217, 11)
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
	(2, 1),
	(3, 1),
	(3, 3),
	(4, 1),
	(4, 2),
	(4, 3),
	(5, 1),
	(5, 5),
	(6, 5),
	(6, 6),
	(7, 1),
	(7, 5),
	(8, 1),
	(8, 3),
	(9, 1),
	(10, 4),
	(10, 5),
	(10, 6)
ON CONFLICT DO NOTHING;

INSERT INTO artists_albums(artist_id, album_id) VALUES
	(1, 4),
	(1, 6),
	(2, 3),
	(3, 2),
	(3, 5),
	(4, 7),
	(4, 8),
	(5, 9),
	(6, 1),
	(7, 6),
	(7, 10),
	(8, 11),
	(8, 8),
	(9, 12),
	(10, 13)
ON CONFLICT DO NOTHING;

INSERT INTO tracks_collections(track_id, collection_id) VALUES
	(1, 5),
	(2, 12),
	(2, 7),
	(3, 1),
	(3, 11),
	(4, 2),
	(4, 5),
	(6, 8),
	(6, 10),
	(7, 7),
	(7, 9),
	(7, 2),
	(8, 5),
	(9, 1),
	(10, 3),
	(10, 7),
	(11, 10),
	(11, 6),
	(12, 11),
	(13, 8),
	(14, 12),
	(15, 9),
	(15, 7),
	(16, 3),
	(17, 5),
	(18, 2),
	(18, 7),
	(19, 11),
	(19, 5),
	(21, 5),
	(21, 8),
	(22, 12),
	(22, 10),
	(23, 8),
	(24, 1),
	(25, 6),
	(25, 9),
	(26, 7)
ON CONFLICT DO NOTHING;

