import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_display_all_movies(client):
    response = client.get('/movies')

    assert response.status_code == 200

    assert b'<table' in response.data
    assert b'Movie Rating App | All Movies' in response.data
