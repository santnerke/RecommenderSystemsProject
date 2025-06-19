def recommend_movies_by_duration(movie_id, movie_list, top_n=5, tolerance=15):
    # Find the reference movie by ID
    ref_movie = next((m for m in movie_list if m.get('id') == movie_id), None)
    if not ref_movie:
        raise ValueError(f"Movie ID {movie_id} not found.")

    ref_duration = ref_movie.get('duration')
    if ref_duration is None:
        raise ValueError(f"Reference movie (ID {movie_id}) has no duration.")

    similarity_scores = []

    for movie in movie_list:
        # Skip the reference movie
        if movie.get('id') == movie_id:
            continue

        duration = movie.get('duration')
        if duration is None:
            continue

        # Calculate duration difference
        duration_diff = abs(duration - ref_duration)

        if duration_diff <= tolerance:
            similarity_scores.append({
                'id': movie.get('id'),
                'title': movie.get('title'),
                'duration': duration,
                'duration_diff': duration_diff
            })

    # Sort results by how close their duration is to the reference
    results = sorted(similarity_scores, key=lambda x: x['duration_diff'])

    return results[:top_n]
