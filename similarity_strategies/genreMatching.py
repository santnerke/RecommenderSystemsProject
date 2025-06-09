def recommend_movies_by_genre(movie_id, df_movies, top_n=5):

    if movie_id not in df_movies['movieId'].values:
        raise ValueError(f"Movie ID {movie_id} not found.")

    ref_genres_str = df_movies[df_movies['movieId'] == movie_id]['genres'].values[0]
    ref_genres = set(ref_genres_str.split('|'))
    similarity_scores = []

    for _, row in df_movies.iterrows():
        if row['movieId'] == movie_id:
            continue

        genres = set(row['genres'].split('|'))
        shared_genres = ref_genres.intersection(genres)
        score = len(shared_genres)

        if score > 0:
            similarity_scores.append({
                'movieId': row['movieId'],
                'title': row['title'],
                'shared_genres': score,
                'genres': row['genres']
            })
    # sort by number of genres
    results = sorted(similarity_scores, key=lambda x: x['shared_genres'], reverse=True)

    return results[:top_n]