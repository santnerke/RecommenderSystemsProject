def recommend_movies_by_year(movie_id, df_movies, top_n=5):

    if movie_id not in df_movies['movieId'].values:
        raise ValueError(f"Movie ID {movie_id} not found.")

    # get release year of the reference movie
    ref_year = df_movies[df_movies['movieId'] == movie_id]['year'].values[0]

    similarity_scores = []

    for _, row in df_movies.iterrows():
        # skip the reference movie
        if row['movieId'] == movie_id:
            continue

        # check if movie has same release year
        if row['year'] == ref_year:
            similarity_scores.append({
                'movieId': row['movieId'],
                'title': row['title'],
                'year': int(row['year']) # avoid float output (like 1995.0)
            })

    return similarity_scores[:top_n]
