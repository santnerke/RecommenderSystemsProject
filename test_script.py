import pandas as pd
from similarity_strategies.leadActorsBased import recommend_movies_by_lead_actors
from similarity_strategies.genreMatching import recommend_movies_by_genre
from similarity_strategies.embeddingBased import recommend_movies_by_embedding
from similarity_strategies.descriptionMatching import recommend_movies_by_description
from similarity_strategies.database import *

movie_id = 2 #needs to come from GUI
movies = load_movies()

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

recommend_movies_by_description(movie_id, movies)
recommend_movies_by_embedding(movie_id, movies)

similar_lead_actor = recommend_movies_by_lead_actors(movie_id, df_movies)
similar_genre = recommend_movies_by_genre(movie_id, df_movies)

print(f"======= similar lead actors =======")
for movie in similar_lead_actor:
    print(f"{movie['title']} – shared actors: {', '.join(movie['shared_actors'])}")

print(f"======= similar genre =======")
for movie in similar_genre:
    print(f"{movie['title']} - same genres: {movie['shared_genres']})")
