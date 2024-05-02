# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE


POST /albums
  title: string
  release_year: number (str)
  artist_id: number (str)
```
GET /albums

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE
# Scenario 1
    # POST /albums
    #  Parameters:
    #    title: goodbye
    #    release_year: 2008
    #    artist_id: 1
    #  Expected response (200 OK):
    """
    """ (no content)

    # GET /albums
    #  Expected response (200 OK):
    """
    Album(1, hello bob, 2008, 1)
    Album(2, goodbye, 2008, 1)
    """

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
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```

