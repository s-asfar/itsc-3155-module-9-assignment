# TODO: Feature 2
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_movie(client):
    # Simulate a form submission to create a movie
    response = client.post('/movies', data=dict(
        title='Test Movie',
        director='Test Director',
        rating=8
    ), follow_redirects=True)
