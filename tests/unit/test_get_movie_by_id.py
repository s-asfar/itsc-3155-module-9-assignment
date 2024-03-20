import pytest
from src.repositories.movie_repository import get_movie_repository

# TODO: Feature 4


def test_empty_movie_repository():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    
    # Check that the movie repository is empty
    assert len(movie_repository.get_all_movies()) == 0
    
    movie_repository.clear_db()


def test_get_single_movie():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    created_movie = movie_repository.create_movie("Daddys home 3", "Daddy", 5)
    
    # Get movie by ID
    movie = movie_repository.get_movie_by_id(created_movie.movie_id)
    
    # Assert that the movie found by ID is the created movie
    assert movie is not None
    assert movie.title == "Daddys home 3"
    assert movie.director == "Daddy"
    assert movie.rating == 5

    movie_repository.clear_db()
    

def test_get_movie_by_nonexistent_id():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    # searches for a nonexistent id
    movie = movie_repository.get_movie_by_id(999)

    # Assert that no movie was found
    assert movie is None
    
    movie_repository.clear_db()
    
def test_get_movie_by_invalid_id():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    # Tries to get movie with an invalid ID
    movie = movie_repository.get_movie_by_id("This is a String")

    # Asserts that no movie was found
    assert movie is None

    movie_repository.clear_db()

