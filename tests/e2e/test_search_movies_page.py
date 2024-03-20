# TODO: Feature 3
from app import app 
from src.repositories.movie_repository import get_movie_repository

#testing that page properly returns status 200 when movie is found and that the movie is displayed on the new page
def test_search_movies_page_success(): 
    
    #creating the test client to perform the get request
    test_app = app.test_client() 
    
    movie_repo = get_movie_repository() 
    #getting the programs movie repository
    movie_repo.create_movie('Test Movie', 'Test Director', 5)

    #performing the get request on the test client to simulate a user searching for a movie
    response = test_app.get('/movies/search?movie_title=Test Movie') 
    
    #checking that page returns staus 200
    assert response.status_code == 200  
    
    #checking that the movie is displayed on the page
    assert b'Test Movie' in response.data 

#checking that the director is displayed on the page
    assert b'Test Director' in response.data 

    #getting rid of added movie after test
    movie_repo.clear_db() 



#testing that page properly returns 404 when movie is not found
def test_search_movies_page_failure(): 
    test_app = app.test_client()

    response = test_app.get('/movies/search?movie_title=Movie That Does Not Exist')
    assert response.status_code == 404
