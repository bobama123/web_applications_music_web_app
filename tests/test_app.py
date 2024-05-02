# Tests for your routes go here

"""
When i call GET /albums
I get a list of albums back
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, hello bob, 2008, 1)"

"""
When i call GET /artists
I get a list of artists back
"""
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Rock)\n" \
        "Artist(2, ABBA, Pop)"
    



# Scenario 1
    # POST /albums
    #  Parameters:
    #    title: goodbye
    #    release_year: 2008
    #    artist_id: 1
    #  Expected response (200 OK):
"""
(no content)
""" 

    # GET /albums
    #  Expected response (200 OK):
"""
Album(1, hello bob, 2008, 1)
Album(2, goodbye, 2008, 1)
"""

"""
When i call POST /albums with album info
That album is now in the list in GET /albums
"""

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums", data={
        'title': 'goodbye',
        'release_year': 2008,
        'artist_id': 1
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, hello bob, 2008, 1)\n" \
        "Album(2, goodbye, 2008, 1)"



# Scenario 2
    # POST /albums
    #  Expected response (404 Bad Request)
    """
    You need to submit a title, release_year and artist_id
    """
    # GET /albums
    #  Expected response (200 OK):
    """
    Album(1, hello bob, 2008, 1)
    """

def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "You need to submit a title, release_year and artist_id"

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, hello bob, 2008, 1)"



def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/artists", data={
        'name': 'Wild Nothing',
        'genre': 'Indie'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Rock)\n" \
        "Artist(2, ABBA, Pop)\n" \
        "Artist(3, Wild Nothing, Indie)"


def test_post_artists_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/artists")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "You need to submit a name and genre"

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Rock)\n" \
        "Artist(2, ABBA, Pop)"

