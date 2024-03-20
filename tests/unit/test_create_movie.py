# TODO: Feature 2
import pytest
from app import app
from flask import Flask
from src.repositories.movie_repository import get_movie_repository


movie_repository = get_movie_repository()

def test_create_movie():

    movie_repository.create_movie('Test Movie', 'Test Director', 10)
    assert movie_repository.get_movie_by_title('Test Movie').title == 'Test Movie'
    assert movie_repository.get_movie_by_title('Test Movie').director == 'Test Director'
