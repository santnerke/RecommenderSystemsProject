def recommend_movies_by_duration(movie_id, df_movies, top_n=5, tolerance=15):

    if movie_id not in df_movies['movieId'].values:
        raise ValueError(f"Movie ID {movie_id} not found.")

    ref_duration = df_movies[df_movies['movieId'] == movie_id]['duration'].values[0]

    similarity_scores = []

    for _, row in df_movies.iterrows():
        # skip reference movie
        if row['movieId'] == movie_id:
            continue

        # calculate duration difference
        duration_diff = abs(row['duration'] - ref_duration)

        if duration_diff <= tolerance:
            similarity_scores.append({
                'movieId': row['movieId'],
                'title': row['title'],
                'duration': row['duration'],
                'duration_diff': duration_diff
            })

    # sort by how close the difference of duration is
    results = sorted(similarity_scores, key=lambda x: x['duration_diff'])

    return results[:top_n]