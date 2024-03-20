# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_title():
   #getting the programs movie repo
   movie_repository = get_movie_repository()
  
   #clearing the db to ensure no movies are present
   movie_repository.clear_db()
   
   #create a test movie
   movie_repository.create_movie('Test Movie', 'Test Director', 5)
   
   #check if the function properly returns the movie
   assert movie_repository.get_movie_by_title('Test Movie').title == 'Test Movie'
   assert movie_repository.get_movie_by_title('Test Movie').director == 'Test Director'
