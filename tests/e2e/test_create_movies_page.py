import pytest
from app import app
from flask import Flask
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_create_movie():
    test_app = app.test_client()

    response = test_app.post('/movies', data={'title': 'Test Movie', 'director': 'Test director', 'rating': 10})

    assert response.status_code == 302

    movie_repository.clear_db()