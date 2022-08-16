CREATE TABLE IF NOT EXISTS collections (
		id SERIAL PRIMARY KEY,
		collection_name VARCHAR(60) UNIQUE NOT NULL,
		collection_year SMALLINT NOT NULL
		);
			
CREATE TABLE IF NOT EXISTS albums (
		id SERIAL PRIMARY KEY,
		album_name VARCHAR(60) UNIQUE NOT NULL,
		album_year SMALLINT NOT NULL
		);
		
CREATE TABLE IF NOT EXISTS artists (
		id SERIAL PRIMARY KEY,
		artist_name VARCHAR(60) UNIQUE NOT NULL
		);
		
CREATE TABLE IF NOT EXISTS genres (
		id SERIAL PRIMARY KEY,
		genre_name VARCHAR(60) UNIQUE NOT NULL
		);
	
CREATE TABLE IF NOT EXISTS tracks (
		id SERIAL PRIMARY KEY,
		track_name VARCHAR(60) UNIQUE NOT NULL,
		duration SMALLINT NOT NULL,
		album_id SMALLINT REFERENCES albums(id)
		);
			
CREATE TABLE IF NOT EXISTS artists_genres (
		artist_id INTEGER REFERENCES artists(id),
		genre_id SMALLINT REFERENCES genres(id),
		CONSTRAINT pk_artists_genres PRIMARY KEY (artist_id, genre_id)
		);
	
CREATE TABLE IF NOT EXISTS artists_albums (
		artist_id INTEGER REFERENCES artists(id),
		album_id INTEGER REFERENCES albums(id),
		CONSTRAINT pk_artists_albums PRIMARY KEY (artist_id, album_id)
		);
		
CREATE TABLE IF NOT EXISTS tracks_collections (
		track_id INTEGER REFERENCES tracks(id),
		collection_id INTEGER REFERENCES collections(id),
		CONSTRAINT pk PRIMARY KEY (track_id, collection_id)
		);