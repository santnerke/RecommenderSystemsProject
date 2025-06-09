import pandas as pd
from similarity_strategies.leadActors import recommend_movies_by_lead_actors

# test data
df_movies = pd.DataFrame([
    {
        'movieId': 1,
        'title': 'Toy Story (1995)',
        'genres': ['Adventure', 'Animation', 'Children', 'Comedy', 'Fantasy'],
        'lead_actors': ['Tom Hanks', 'Tim Allen']
    },
    {
        'movieId': 2,
        'title': 'Jumanji (1995)',
        'genres': ['Adventure', 'Children', 'Fantasy'],
        'lead_actors': ['Robin Williams', 'Tim Allen']
    },
    {
        'movieId': 356,
        'title': 'Forrest Gump (1994)',
        'genres': ['Comedy', 'Drama', 'Romance', 'War'],
        'lead_actors': ['Tom Hanks', 'Robin Wright']
    },
    {
        'movieId': 4022,
        'title': 'Cast Away (2000)',
        'genres': ['Drama'],
        'lead_actors': ['Tom Hanks', 'Helen Hunt']
    },
    {
        'movieId': 9999999999,
        'title': 'Test with Tom Hanks & Tim Allen',
        'genres': ['Documentary'],
        'lead_actors': ['Tom Hanks', 'Tim Allen']
    },
    {
        'movieId': 3,
        'title': 'Grumpier Old Men (1995)',
        'genres': ['Comedy', 'Romance'],
        'lead_actors': ['Walter Matthau', 'Jack Lemmon']
    },
    {
        'movieId': 4,
        'title': 'Waiting to Exhale (1995)',
        'genres': ['Comedy', 'Drama', 'Romance'],
        'lead_actors': ['Whitney Houston', 'Angela Bassett']
    },
])

# test movie with id 1
similar_lead_actor = recommend_movies_by_lead_actors(1, df_movies)

for movie in similar_lead_actor:
    print(f"{movie['title']} – shared actors: {', '.join(movie['shared_actors'])}")