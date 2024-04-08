import pytest
from src.repositories.movie_repository import get_movie_repository
from app import app, get_single_movie
from flask.testing import FlaskClient

# TODO: Feature 4

@pytest.fixture(scope='function', autouse=True)
def reset_movies():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    yield
    movie_repository.clear_db()

def test_app():
    with app.app_context():
        yield app.test_client()
    
    

    
def test_get_movie_by_id(test_app: FlaskClient): 
    # Creates movie with id 1
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    movie = movie_repository.create_movie("Daddys home 3", "Daddy", 5)

    # Asserts the movie is made 
    assert movie is not None
    assert movie.movie_id is not None

    # Asserts response has status code 200
    response = test_app.get(f"/movies/{movie.movie_id}")
    response.data = response.data.decode("utf-8")
    assert response.status_code == 200
    
    
    
def test_get_movie_by_nonexistent_id(test_app: FlaskClient): 
    # Makes sure there is no movie
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    # Asserts response has status code 404
    response = test_app.get(f"/movies/{999}")
    response.data = response.data.decode("utf-8")
    assert response.status_code == 404


def test_get_movie_by_invalid_id(test_app: FlaskClient): 
    # Makes sure there is no movie
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    # Asserts response has status code 404
    response = test_app.get(f"/movies/{"This Is a String"}")
    response.data = response.data.decode("utf-8")
    assert response.status_code == 404
