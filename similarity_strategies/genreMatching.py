def recommend_movies_by_genre(movie_id, movie_list, top_n=5):
    # Find reference movie using next()
    ref_movie = next((m for m in movie_list if m.get('id') == movie_id), None)
    if not ref_movie:
        raise ValueError(f"Movie ID {movie_id} not found.")

    # Ensure genres are lists
    ref_genres = set(ref_movie.get('genres', []))  # Already a list
    similarity_scores = []

    for movie in movie_list:
        if movie.get('id') == movie_id:
            continue

        genres = set(movie.get('genres', []))
        shared_genres = ref_genres.intersection(genres)
        score = len(shared_genres)

        if score > 0:
            similarity_scores.append({
                'id': movie.get('id'),
                'title': movie.get('title'),
                'shared_genres': ", ".join(shared_genres),  # To display in template
                'genres': movie.get('genres', [])
            })

    # Sort by number of shared genres
    results = sorted(similarity_scores, key=lambda x: len(x['shared_genres'].split(', ')), reverse=True)
    return results[:top_n]