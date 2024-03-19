# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_title():
   movie_repository = get_movie_repository()
   movie_repository.clear_db()
   movie_repository.create_movie('Test Movie', 'Test Director', 5)
   assert movie_repository.get_movie_by_title('Test Movie').title == 'Test Movie'
   assert movie_repository.get_movie_by_title('Test Movie').director == 'Test Director'
