from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When I call #all
I get all the albums in the albums table
"""

def test_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, "hello bob", 2008, 1)
    ]


"""
When I call #create
I create an album in the database
And I can see it back in #all
"""

def test_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "yoyo", 2020, 2)
    repository.create(album)
    assert repository.all() == [
        Album(1, "hello bob", 2008, 1),
        Album(2, "yoyo", 2020, 2)
    ]
