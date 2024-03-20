from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

from flask import request

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page

    title = request.form['title']
    director = request.form['director']
    rating = int(request.form['rating'])

    movie = movie_repository.create_movie(title, director, int(rating))

    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    movie_title = request.args.get('movie_title')
    if movie_title:
        movie = get_movie_repository().get_movie_by_title(movie_title)
        if movie:
            return render_template('search_movies.html', search_active=True, movie=movie)
        else:
            return '''
            <p>No movie found with that title</p> 
            <form action="/movies/search" method="get">
                <input type="submit" value="Back to search">
                </form>
                ''', 404
            
    else:
        return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    """
    This function retrieves a movie with a given id

    Args:
        movie_id (int): The ID of the movie

    Returns:
        If the movie is found it returns the HTML template with the movie data.
        If the movie is not found ir returns with an error message and a 404 error
    """
    movie = movie_repository.get_movie_by_id(movie_id)
    if movie is None:
        return render_template('get_single_movie.html', message="Movie Not Found"), 404
    return render_template('get_single_movie.html', movie=movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass