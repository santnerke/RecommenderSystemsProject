from django.shortcuts import render, get_object_or_404
from .models import Movie  # Your movie model
from similarity_strategies.genreMatching import recommend_movies_by_genre
from similarity_strategies.leadActorsBased import recommend_movies_by_lead_actors
from similarity_strategies.descriptionMatching import recommend_movies_by_description
from similarity_strategies.embeddingBased import recommend_movies_by_embedding
from similarity_strategies.releaseYearMatching import recommend_movies_by_year
from similarity_strategies.durationBased import recommend_movies_by_duration

def index(request):
    movies = Movie.objects.all().values('id', 'title').order_by('title')
    return render(request, 'rs_app/index.html', {'movies': movies})

def recommend(request):
    movie_id = request.GET.get('movie_id')
    movie = get_object_or_404(Movie, id=movie_id)

    # You need to get all movies as a list or queryset for recommendation
    movies = Movie.objects.all()

    # Depending on how your recommendation functions are built,
    # you might need to convert queryset to list/dict or dataframe.
    # Here's a simplistic example converting to list of dicts:

    movies_list = list(movies.values(
        'id', 'title', 'genres', 'actors', 'release_year', 'duration', 'plot_summary'
    ))

    genre_recs = recommend_movies_by_genre(movie.id, movies_list)
    actor_recs = recommend_movies_by_lead_actors(movie.id, movies_list)
    desc_recs = recommend_movies_by_description(movie.id, movies_list)
    embe_recs = recommend_movies_by_embedding(movie.id, movies_list)
    year_recs = recommend_movies_by_year(movie.id, movies_list)
    dur_recs = recommend_movies_by_duration(movie.id, movies_list)

    return render(request, 'rs_app/recommend.html', {
        'movie': movie,
        'genre_recommendations': genre_recs,
        'actor_recommendations': actor_recs,
        'description_recommendations': desc_recs,
        'embedding_recommendations': embe_recs,
        'year_recommendations': year_recs,
        'duration_recommendations': dur_recs,
    })
