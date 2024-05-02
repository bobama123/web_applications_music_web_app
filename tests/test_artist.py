from lib.artist import Artist

"""
Constructs with an id, name, genre
"""

def test_constructs():
    artist = Artist(1, 'Pixies', 'Rock')
    assert artist.id == 1
    assert artist.name == 'Pixies'
    assert artist.genre == 'Rock'


"""
Albums with equal contents are equal
"""

def test_equal():
    artist1 = Artist(1, 'Pixies', 'Rock')
    artist2 = Artist(1, 'Pixies', 'Rock')
    assert artist1 == artist2



"""
Albums format to string
"""

def test_format():
    artist = Artist(1, 'Pixies', 'Rock')
    assert str(artist) == "Artist(1, Pixies, Rock)"