from lib.album import Album

"""
Constructs with an id, title, release date and artist id
"""

def test_constructs():
    album = Album(1, "hello bob", 2008, 1)
    assert album.id == 1
    assert album.title == "hello bob"
    assert album.release_year == 2008
    assert album.artist_id == 1


"""
Albums with equal contents are equal
"""

def test_equal():
    album1 = Album(1, "hello bob", 2008, 1)
    album2 = Album(1, "hello bob", 2008, 1)
    assert album1 == album2



"""
Albums format to string
"""

def test_format():
    album = Album(1, "hello bob", 2008, 1)
    assert str(album) == "Album(1, hello bob, 2008, 1)"