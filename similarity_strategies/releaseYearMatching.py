def recommend_movies_by_year(movie_id, movie_list, top_n=5):
    # Find the reference movie by ID
    ref_movie = next((m for m in movie_list if m.get('id') == movie_id), None)
    if not ref_movie:
        raise ValueError(f"Movie ID {movie_id} not found.")

    ref_year = ref_movie.get('release_year')
    if ref_year is None:
        raise ValueError(f"Reference movie (ID {movie_id}) has no release year.")

    similarity_scores = []

    for movie in movie_list:
        if movie.get('id') == movie_id:
            continue

        year = movie.get('release_year')
        if year is None:
            continue

        if year == ref_year:
            similarity_scores.append({
                'id': movie.get('id'),
                'title': movie.get('title'),
                'release_year': year
            })

    return similarity_scores[:top_n]
