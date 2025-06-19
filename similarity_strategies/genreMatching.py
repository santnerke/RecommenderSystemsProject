def recommend_movies_by_genre(movie_id, movie_list, top_n=5):
    # Find reference movie using next()
    ref_movie = next((m for m in movie_list if m.get('id') == movie_id), None)
    if not ref_movie:
        raise ValueError(f"Movie ID {movie_id} not found.")

    ref_genres_str = ref_movie.get('genres', '')
    ref_genres = set(ref_genres_str.split(','))
    similarity_scores = []

    for movie in movie_list:
        if movie.get('id') == movie_id:
            continue

        genres_str = movie.get('genres', '')
        genres = set(genres_str.split(','))
        shared_genres = ref_genres.intersection(genres)
        score = len(shared_genres)

        if score > 0:
            similarity_scores.append({
                'id': movie.get('id'),
                'title': movie.get('title'),
                'shared_genres': score,
                'genres': genres_str
            })

    results = sorted(similarity_scores, key=lambda x: x['shared_genres'], reverse=True)
    return results[:top_n]