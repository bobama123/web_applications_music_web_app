import os
from flask import Flask, request
from lib.album_repository import AlbumRepository
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['POST'])
def post_albums():
    if has_invalid_album_parameters(request.form):
        return "You need to submit a title, release_year and artist_id", 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None,
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id']
    )
    repository.create(album)
    return '', 200

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return "\n".join(
        f"{album}" for album in albums
    )

def has_invalid_album_parameters(form):
    return 'title' not in form or \
        'release_year' not in form or \
        'artist_id' not in form


@app.route('/artists', methods=['POST'])
def post_artists():
    if has_invalid_artist_parameters(request.form):
        return "You need to submit a name and genre", 400
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(
        None,
        request.form['name'],
        request.form['genre'],
    )
    repository.create(artist)
    return '', 200

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return "\n".join(
        f"{artist}" for artist in artists
    )

def has_invalid_artist_parameters(form):
    return 'name' not in form or \
        'genre' not in form



# """
# When: I make a POST request to /albums
# And: I send a title, release_year and artist_id as body parameters
# Then: I should get a 200 response with the right content
# """

# def test_post_albums(web_client):
#     response = web_client.post('/albums', data={'title': 'Voyaga', 'release_year': '2022', 'artist_id': '2'})
#     assert response.status_code == 200


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

