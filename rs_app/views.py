from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from similarity_strategies.genreMatching import recommend_movies_by_genre
from similarity_strategies.leadActors import recommend_movies_by_lead_actors
import pandas as pd

# test data
df_movies = pd.DataFrame([
    {
        'movieId': 1,
        'title': 'Toy Story (1995)',
        'genres': 'Adventure|Animation|Children|Comedy|Fantasy',
        'lead_actors': ['Tom Hanks', 'Tim Allen']
    },
    {
        'movieId': 2,
        'title': 'Jumanji (1995)',
        'genres': 'Adventure|Children|Fantasy',
        'lead_actors': ['Robin Williams', 'Tim Allen']
    },
    {
        'movieId': 356,
        'title': 'Forrest Gump (1994)',
        'genres': 'Comedy|Drama|Romance|War',
        'lead_actors': ['Tom Hanks', 'Robin Wright']
    },
    {
        'movieId': 4022,
        'title': 'Cast Away (2000)',
        'genres': 'Drama',
        'lead_actors': ['Tom Hanks', 'Helen Hunt']
    },
    {
        'movieId': 3,
        'title': 'Grumpier Old Men (1995)',
        'genres': 'Comedy|Romance',
        'lead_actors': ['Walter Matthau', 'Jack Lemmon']
    },
    {
        'movieId': 9999999999,
        'title': 'Test with Tom Hanks & Tim Allen',
        'genres': 'Documentary',
        'lead_actors': ['Tom Hanks', 'Tim Allen']
    },
    {
        'movieId': 99999999999,
        'title': 'Test with the same genres',
        'genres': 'Adventure|Animation|Children|Comedy|Fantasy',
        'lead_actors': ['xy']
    },
])

def index(request):
    return render(request, 'rs_app/index.html')

def recommend(request):
    movie_id = int(request.GET.get('movie_id'))
    genre_recs = recommend_movies_by_genre(movie_id, df_movies)
    actor_recs = recommend_movies_by_lead_actors(movie_id, df_movies)

    return render(request, 'rs_app/recommend.html', {
        'genre_recommendations': genre_recs,
        'actor_recommendations': actor_recs,
        'movie_id': movie_id,
    })

