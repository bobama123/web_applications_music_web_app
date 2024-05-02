from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When I call #all
I get all the artists in the artists table
"""

def test_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop")
    ]


"""
When I call #create
I create an artist in the database
And I can see it back in #all
"""

def test_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, "water", "lofi")
    repository.create(artist)
    assert repository.all() == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "water", "lofi")
    ]
