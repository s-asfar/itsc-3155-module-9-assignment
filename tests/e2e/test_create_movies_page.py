# TODO: Feature 2
import pytest
from app import create_movie
from flask import Flask
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

@pytest.fixture
def app():
    return Flask(__name__)

def test_create_movie():
    
    # Create a mock request object

    
    # Call create_movie function with mock request
    response = movie_repository.create_movie('Test Movie', 'Test director', 10)
    
    # Check if the function redirects to /movies endpoint
    assert response.status_code == 302
    assert response.location == 'http://localhost/movies'

movie_repository.clear_db()
