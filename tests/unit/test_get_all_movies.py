from app import get_movie_repository
from src.models.movie import Movie 

def list_all_movies():
    movie_repo = get_movie_repository()
    
    all_movies = movie_repo.get_all_movies()
    
    return all_movies

def test_get_all_movies_empty_repo():
    movie_repo = get_movie_repository()
    movie_repo.clear_db() 
    response = list_all_movies() 

    assert len(response) == 0


def test_get_all_movies():
    movie_repo = get_movie_repository()

    movie_repo._db[1] = Movie(1, "Movie 1", "Director 1", 7)
    movie_repo._db[2] = Movie(2, "Movie 2", "Director 2", 8)

    response = list_all_movies()

    assert len(response) == 2
    assert any(movie.title == "Movie 1" for movie in response.values())
    assert any(movie.title == "Movie 2" for movie in response.values())
