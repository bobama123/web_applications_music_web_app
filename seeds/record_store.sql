DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('hello bob', 2008, 1);

INSERT INTO artists (name, genre) VALUES ('Pixies', 'Rock');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'Pop');
